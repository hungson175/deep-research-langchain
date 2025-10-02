import asyncio
from dotenv import load_dotenv
load_dotenv()

from ..utils.helpers import show_prompt, get_today_str, tavily_search, think_tool, console, init_xai_model
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from ..prompts.system_prompts import compress_research_combined_prompt, research_agent_prompt
from ..utils.cache_strategy import CacheStrategyFactory
from ..utils.config import RESEARCHER_MODEL, RESEARCHER_TEMPERATURE, RESEARCHER_MAX_TOOL_CALL_ITERATIONS

# Uncomment to show the prompt during development
# show_prompt(research_agent_prompt, "Research Agent Instructions")
class Researcher:

    def __init__(self, max_tool_call_iterations: int = RESEARCHER_MAX_TOOL_CALL_ITERATIONS):
        console.print(Panel("[bold green]🔍 Initializing Researcher Agent[/bold green]", border_style="green"))

        self.model = init_xai_model(
            model=RESEARCHER_MODEL,
            temperature=RESEARCHER_TEMPERATURE,
            max_tokens=64000
        )
        self.tools = [think_tool, tavily_search]
        self.model_with_tools = self.model.bind_tools(self.tools)
        self.max_tool_call_iterations = max_tool_call_iterations

        # Initialize cache strategy based on model
        self.cache_strategy = CacheStrategyFactory.create_strategy(f"xai:{RESEARCHER_MODEL}")
        console.print(f"[dim]Using model: {RESEARCHER_MODEL}[/dim]")
        console.print(f"[dim]Cache strategy: {self.cache_strategy.__class__.__name__}[/dim]")
        console.print(f"[dim]Max iterations: {max_tool_call_iterations}[/dim]")

        # Create initial system message with caching if supported
        system_msg = self.cache_strategy.prepare_system_message(
            research_agent_prompt.format(
                date=get_today_str(),
                max_iterations=max_tool_call_iterations
            )
        )
        self.messages = [system_msg]

        self.tools_by_name = {tool.name: tool for tool in self.tools}
        self.compressed_research = ""

    async def compress_research_findings(self) -> str:
        """Compress research findings while preserving all relevant information.

        Uses a single combined prompt that merges system and human messages
        to maintain conversation context and leverage cached prompts.
        """
        console.print("[yellow]📝 Compressing research findings...[/yellow]")

        # IMPORTANT: Clean up any lingering cache_control from messages first
        # This handles the case where we hit max iterations and broke early
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        # Use the pre-combined prompt with only the date to format
        combined_compression_prompt = compress_research_combined_prompt.format(date=get_today_str())

        # Create human message with cache strategy
        compression_msg = self.cache_strategy.prepare_human_message(
            combined_compression_prompt,
            add_cache=True  # Add cache for compression prompt
        )
        self.messages.append(compression_msg)

        # Use the SAME model instance (with tools) to leverage caching!
        # Even though we won't call tools, using the same instance preserves cache
        # Messages already have cache from prepare_human_message, so invoke directly
        response = await self.model_with_tools.ainvoke(self.messages)

        # Cleanup messages after invoke
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        # Store the compressed research
        self.compressed_research = str(response.content)
        self.messages.append(response)

        console.print("[green]✅ Research compression complete[/green]")
        return self.compressed_research
    async def start_research(self, research_brief: str):
        console.print(Panel(f"[bold green]🔎 Starting Research[/bold green]\n\nBrief: {research_brief[:150]}...", border_style="green"))

        # Create and append human message with cache strategy
        research_msg = self.cache_strategy.prepare_human_message(
            research_brief,
            add_cache=True  # Cache the initial research brief
        )
        self.messages.append(research_msg)

        console.print("[dim]Researcher analyzing brief and planning approach...[/dim]")
        # Invoke directly - messages already have cache from prepare_human_message
        response = await self.model_with_tools.ainvoke(self.messages)

        # Cleanup and append response
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        self.messages.append(response)
        
        tool_call_iterations = 0

        while response.tool_calls:
            # Check if we've hit the iteration limit BEFORE processing
            if tool_call_iterations >= self.max_tool_call_iterations:
                console.print(f"[yellow]⚠️ Reached maximum iterations ({self.max_tool_call_iterations}). Finalizing research...[/yellow]")
                # Remove the last AI message with unfulfilled tool calls
                # to avoid OpenAI API error about missing tool responses
                self.messages.pop()
                break

            tool_call_iterations += 1
            console.print(f"\n[cyan]🔄 Research Iteration {tool_call_iterations}/{self.max_tool_call_iterations}[/cyan]")

            observations = []
            for tool_call in response.tool_calls:
                tool = self.tools_by_name[tool_call["name"]]
                tool_name = tool_call["name"]

                if tool_name == "think_tool":
                    console.print(f"[magenta]💭 Thinking: {tool_call['args']['reflection'][:100]}...[/magenta]")
                elif tool_name == "tavily_search":
                    console.print(f"[blue]🔍 Searching: \"{tool_call['args']['query']}\"[/blue]")

                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                    transient=True,
                ) as progress:
                    task = progress.add_task(f"[cyan]Executing {tool_name}...", total=None)
                    result = await tool.ainvoke(tool_call["args"])
                    progress.update(task, completed=True)
                    observations.append(result)

                if tool_name == "tavily_search":
                    # Show brief summary of search results
                    result_preview = result[:200] + "..." if len(result) > 200 else result
                    console.print(f"[dim green]✅ Found relevant information[/dim green]")

            # Create tool messages with cache strategy
            tool_outputs = []
            for i, (observation, tool_call) in enumerate(zip(observations, response.tool_calls)):
                # Cache the last tool message for better performance
                is_last = (i == len(observations) - 1)
                tool_msg = self.cache_strategy.prepare_tool_message(
                    observation,
                    tool_call["id"],
                    add_cache=is_last
                )
                tool_outputs.append(tool_msg)

            self.messages.extend(tool_outputs)

            console.print("[dim]Analyzing findings and planning next steps...[/dim]")
            # Invoke directly - last tool message already has cache
            response = await self.model_with_tools.ainvoke(self.messages)

            # Cleanup and append
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            self.messages.append(response)

        # Compress findings
        self.compressed_research = await self.compress_research_findings()
        console.print(Panel("[bold green]✨ Research Complete[/bold green]", border_style="green"))
        return self.compressed_research


RESEARCH_BRIEF = """
I want to research the best specialty coffee shops in Ho Chi Minh City, 
focusing on criteria such as coffee quality (including bean sourcing, roasting methods, and 
brewing techniques), ambiance, customer reviews, and location accessibility within the city, 
while considering all price ranges unless cost constraints are specified, and prioritizing 
direct sources like official shop websites, Google Maps, and reputable review platforms such 
as TripAdvisor or local Vietnamese review sites for authentic insights.
"""
async def main():
    console.print("[bold]═" * 80 + "[/bold]")
    console.print(Panel("[bold green]Researcher Agent - Demo Mode[/bold green]", border_style="green"))
    console.print("[bold]═" * 80 + "[/bold]")

    # Test the researcher
    researcher = Researcher(max_tool_call_iterations=3)
    research_brief = RESEARCH_BRIEF
    result = await researcher.start_research(research_brief)

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print(Panel(f"[bold cyan]📋 Compressed Research Results[/bold cyan]\n\n{result}", border_style="cyan"))
    console.print("[bold]═" * 80 + "[/bold]")  
if __name__ == "__main__":
    asyncio.run(main())
