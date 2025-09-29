# Load environment variables and set up auto-reload
import asyncio
from dotenv import load_dotenv
load_dotenv()

from .researcher import Researcher
from .utils import show_prompt, get_notes_from_tool_calls, format_messages, console, init_xai_model
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from .prompts import lead_researcher_prompt
from .cache_strategy import CacheStrategyFactory
from .config import (SUPERVISOR_MODEL, SUPERVISOR_TEMPERATURE, MIRMIR_API_SERVER_BASE_URL, MIRMIR_TIMEOUT_SECONDS,
                    RESEARCHER_MAX_TOOL_CALL_ITERATIONS, SUPERVISOR_MAX_RESEARCHER_ITERATIONS,
                    SUPERVISOR_MAX_CONCURRENT_RESEARCHERS)

from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from .utils import get_today_str, think_tool

# Uncomment to show the prompt during development
# show_prompt(lead_researcher_prompt, "Lead Researcher Prompt")
# Notes: change tools names: 
# 1. **ConductResearch**: Delegate research tasks to specialized sub-agents                                                                                                                                         │
# 2. **ResearchComplete**: Indicate that research is complete  
# Those names are wrong for this codebase (not using LangGraph)

@tool
async def conduct_research(research_topic: str) -> str:
    """
    Tool for delegating a research task to a specialized sub-agent.

    Args:
        research_topic: The topic to research. Should be a single topic, and should be described in high detail (at least a paragraph).

    Returns:
        The research findings.
    """
    console.print(f"[dim cyan]└── Launching sub-researcher for: {research_topic[:100]}...[/dim cyan]")
    researcher = Researcher(max_tool_call_iterations=RESEARCHER_MAX_TOOL_CALL_ITERATIONS)
    result = await researcher.start_research(research_brief=research_topic)
    console.print(f"[dim green]└── Sub-researcher completed: {research_topic[:50]}...[/dim green]")
    return result


@tool
async def query_momo_data(query: str) -> str:
    """
    Query MoMo's internal business data: GMV, transactions, users, revenue, engagement metrics
    across 43+ domains (payments, financial services, commerce, analytics).

    USE FOR: MoMo operational metrics and business data
    DON'T USE FOR: Public info, real-time data, technical architecture, competitor research

    Examples:
    - "tình hình sản phẩm Moni trong năm 2025 ntn?"
    - "GMV của MoMo từ 1/1/2025 đến 31/1/2025"

    Note: Takes 1-4 minutes - so if possible, use it ALONE , not mixed with web-search tool. Ask naturally in Vietnamese or English.

    Args:
        query: Your question about MoMo data

    Returns:
        Business data from MoMo's data warehouse
    """
    import requests

    console.print(f"[dim cyan]└── Querying MoMo data: {query[:100]}...[/dim cyan]")

    try:
        api_url = f"{MIRMIR_API_SERVER_BASE_URL}/auto_query"
        payload = {
            "query": query,
            "execute": True,
            "verbose": True
        }

        response = requests.post(api_url, json=payload, timeout=MIRMIR_TIMEOUT_SECONDS)
        response.raise_for_status()

        result = response.json()

        if result["success"]:
            formatted_response = f"MoMo Data Query Results ({result['queries_with_answers']}/{result['total_queries']} answered):\n\n"

            for i, sq in enumerate(result['sub_queries'], 1):
                formatted_response += f"{i}. Domain: {sq['domain_name']}\n"
                formatted_response += f"   Question: {sq['question']}\n"
                if sq['answer']:
                    formatted_response += f"   Answer: {sq['answer']}\n"
                else:
                    formatted_response += f"   Answer: (No answer received)\n"
                formatted_response += "\n"

            console.print(f"[dim green]└── MoMo data query completed: {result['queries_with_answers']} answers retrieved[/dim green]")
            return formatted_response
        else:
            error_msg = f"MirMir API Error: {result.get('error', 'Unknown error')}"
            console.print(f"[dim red]└── MoMo data query failed: {error_msg}[/dim red]")
            return error_msg

    except requests.exceptions.ConnectionError:
        error_msg = "Cannot connect to MirMir API at localhost:8001. Please ensure the API server is running: uv run python api_server.py"
        console.print(f"[dim red]└── {error_msg}[/dim red]")
        return error_msg
    except requests.exceptions.Timeout:
        error_msg = "MirMir API request timed out after 5 minutes. Query may be too complex."
        console.print(f"[dim red]└── {error_msg}[/dim red]")
        return error_msg
    except Exception as e:
        error_msg = f"Unexpected error querying MoMo data: {str(e)}"
        console.print(f"[dim red]└── {error_msg}[/dim red]")
        return error_msg


class Supervisor:

    def __init__(self,
                 research_brief: str,
                 max_researcher_iterations: int = SUPERVISOR_MAX_RESEARCHER_ITERATIONS,
                 max_concurrent_research_units: int = SUPERVISOR_MAX_CONCURRENT_RESEARCHERS):
        console.print(Panel("[bold yellow]🎯 Initializing Research Supervisor[/bold yellow]", border_style="yellow"))

        # Initialize cache strategy based on model
        self.cache_strategy = CacheStrategyFactory.create_strategy(f"xai:{SUPERVISOR_MODEL}")
        console.print(f"[dim]Using model: {SUPERVISOR_MODEL}[/dim]")
        console.print(f"[dim]Cache strategy: {self.cache_strategy.__class__.__name__}[/dim]")
        console.print(f"[dim]Max iterations: {max_researcher_iterations}[/dim]")
        console.print(f"[dim]Max concurrent researchers: {max_concurrent_research_units}[/dim]")

        # Create initial system message with caching if supported
        system_msg = self.cache_strategy.prepare_system_message(
            lead_researcher_prompt.format(
                date=get_today_str(),
                max_researcher_iterations=max_researcher_iterations,
                max_concurrent_research_units=max_concurrent_research_units
            )
        )
        self.messages = [system_msg]

        self.research_brief = research_brief
        self.notes = []
        self.max_research_iterations = max_researcher_iterations
        self.max_concurrent_researchers = max_concurrent_research_units
        self.total_tokens = 0
        model = init_xai_model(model=SUPERVISOR_MODEL, temperature=SUPERVISOR_TEMPERATURE)
        self.model_with_tools = model.bind_tools([conduct_research, query_momo_data, think_tool])
        
    async def start_supervision(self):
        console.print(Panel(f"[bold blue]📋 Starting Supervision[/bold blue]\n\nResearch Brief:\n{self.research_brief[:200]}...", border_style="blue"))

        # Create and append human message with cache strategy
        research_msg = self.cache_strategy.prepare_human_message(
            self.research_brief,
            add_cache=True  # Cache the initial research brief
        )
        self.messages.append(research_msg)

        console.print("[dim]Supervisor analyzing research brief and planning approach...[/dim]")
        # Invoke directly - messages already have cache from prepare_human_message
        response = await self.model_with_tools.ainvoke(self.messages)
        if hasattr(response, 'usage_metadata') and response.usage_metadata:
            self.total_tokens += response.usage_metadata.get('total_tokens', 0)

        # Cleanup and append response
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        self.messages.append(response)
        
        researcher_iteration = 0

        # Only handle tool calls and not exceed the maximum number of iterations
        while response.tool_calls:
            # Check if we've hit the iteration limit BEFORE processing
            if researcher_iteration >= self.max_research_iterations:
                console.print(f"[yellow]⚠️ Reached maximum iterations ({self.max_research_iterations}). Finalizing research...[/yellow]")
                # Remove the last AI message with unfulfilled tool calls
                # to avoid OpenAI API error about missing tool responses
                self.messages.pop()
                break

            console.print(f"\n[bold cyan]🔄 Iteration {researcher_iteration + 1}/{self.max_research_iterations}[/bold cyan]")

            think_tool_calls = [
                tool_call for tool_call in response.tool_calls
                if tool_call["name"] == "think_tool"
            ]

            conduct_search_calls = [
                tool_call for tool_call in response.tool_calls
                if tool_call["name"] == "conduct_research"
            ]

            query_momo_calls = [
                tool_call for tool_call in response.tool_calls
                if tool_call["name"] == "query_momo_data"
            ]

            # Handle think_tool sync
            for tool_call in think_tool_calls:
                console.print(f"[magenta]💭 Supervisor thinking: {tool_call['args']['reflection'][:150]}...[/magenta]")
                observation = think_tool.invoke(tool_call["args"])
                # Use cache strategy for tool messages
                tool_msg = self.cache_strategy.prepare_tool_message(
                    observation,
                    tool_call["id"],
                    add_cache=False  # Don't cache think_tool responses
                )
                self.messages.append(tool_msg)
                
            # Handle conduct_research async
            if conduct_search_calls:
                console.print(f"[cyan]🚀 Launching {len(conduct_search_calls)} parallel research task(s)...[/cyan]")

                # Create a table to show research tasks
                table = Table(title="Research Tasks", show_header=True, header_style="bold cyan")
                table.add_column("#", style="dim", width=3)
                table.add_column("Topic", style="white")

                for i, tool_call in enumerate(conduct_search_calls, 1):
                    topic = tool_call["args"]["research_topic"][:100] + "..."
                    table.add_row(str(i), topic)

                console.print(table)

                coroutines = [
                    conduct_research.ainvoke(tool_call["args"])
                    for tool_call in conduct_search_calls
                ]

                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                ) as progress:
                    task = progress.add_task(f"[cyan]Researchers working...", total=None)
                    tool_results = await asyncio.gather(*coroutines)
                    progress.update(task, completed=True)

                console.print(f"[green]✅ All {len(conduct_search_calls)} research task(s) completed[/green]")

                research_tool_messages = []
                for i, (result, tool_call) in enumerate(zip(tool_results, conduct_search_calls)):
                    # Cache the last research tool message for better performance
                    is_last = (i == len(tool_results) - 1)
                    tool_msg = self.cache_strategy.prepare_tool_message(
                        result,
                        tool_call["id"],
                        add_cache=is_last  # Cache last research result
                    )
                    research_tool_messages.append(tool_msg)
                self.messages.extend(research_tool_messages)

            # Handle query_momo_data async
            if query_momo_calls:
                console.print(f"[cyan]📊 Querying {len(query_momo_calls)} MoMo data request(s)...[/cyan]")

                # Create a table to show MoMo queries
                table = Table(title="MoMo Data Queries", show_header=True, header_style="bold cyan")
                table.add_column("#", style="dim", width=3)
                table.add_column("Query", style="white")

                for i, tool_call in enumerate(query_momo_calls, 1):
                    query_text = tool_call["args"]["query"][:100] + "..."
                    table.add_row(str(i), query_text)

                console.print(table)

                coroutines = [
                    query_momo_data.ainvoke(tool_call["args"])
                    for tool_call in query_momo_calls
                ]

                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                ) as progress:
                    task = progress.add_task(f"[cyan]MirMir Agent processing...", total=None)
                    momo_results = await asyncio.gather(*coroutines)
                    progress.update(task, completed=True)

                console.print(f"[green]✅ All {len(query_momo_calls)} MoMo data queries completed[/green]")

                momo_tool_messages = []
                for i, (result, tool_call) in enumerate(zip(momo_results, query_momo_calls)):
                    # Cache the last MoMo query result
                    is_last = (i == len(momo_results) - 1)
                    tool_msg = self.cache_strategy.prepare_tool_message(
                        result,
                        tool_call["id"],
                        add_cache=is_last  # Cache last MoMo result
                    )
                    momo_tool_messages.append(tool_msg)
                self.messages.extend(momo_tool_messages)

            console.print("[dim]Supervisor analyzing results and planning next steps...[/dim]")
            # Invoke directly - last tool message already has cache if needed
            response = await self.model_with_tools.ainvoke(self.messages)
            if hasattr(response, 'usage_metadata') and response.usage_metadata:
                self.total_tokens += response.usage_metadata.get('total_tokens', 0)

            # Cleanup and append
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            self.messages.append(response)
            researcher_iteration += 1
        self.notes = get_notes_from_tool_calls(self.messages)

        console.print(Panel(f"[bold green]✨ Supervision Complete[/bold green]\n\nCollected {len(self.notes)} research notes", border_style="green"))

        return {
            "final_response": response.content,
            "notes": self.notes
        }

BIG_BRIEF = """
I want to research the best specialty coffee shops in Vietnam's main cities, such as Hanoi, 
Ho Chi Minh City, Da Nang, and others, focusing on factors that define 'best' like coffee quality 
(including bean sourcing, roasting methods, and brewing techniques), atmosphere, customer reviews,
and unique offerings, while acknowledging that specific preferences for price range, location within 
cities, or other constraints are not specified, so treat these as open considerations; prioritize 
sourcing information from official coffee shop websites, reputable review platforms like TripAdvisor 
or Google Reviews, and local tourism sites in Vietnamese or English.
"""
async def main():
    console.print("[bold]═" * 80 + "[/bold]")
    console.print(Panel("[bold yellow]Research Supervisor - Demo Mode[/bold yellow]", border_style="yellow"))
    console.print("[bold]═" * 80 + "[/bold]")

    supervisor = Supervisor(research_brief=BIG_BRIEF)
    result = await supervisor.start_supervision()

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print(Panel(f"[bold green]📝 Final Response[/bold green]\n\n{result['final_response']}", border_style="green"))

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print(Panel(f"[bold cyan]📚 Research Notes ({len(result['notes'])} total)[/bold cyan]", border_style="cyan"))
    for i, note in enumerate(result['notes'], 1):
        console.print(f"\n[bold]Note {i}:[/bold]")
        console.print(Panel(note[:500] + "..." if len(note) > 500 else note, border_style="dim"))

    # Uncomment to see full message history
    # console.print("\n[bold]═" * 80 + "[/bold]")
    # console.print("[bold]Message History:[/bold]")
    # format_messages(supervisor.messages)
        
if __name__ == "__main__":
    asyncio.run(main())