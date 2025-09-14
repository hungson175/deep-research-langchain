# Load environment variables and set up auto-reload
import asyncio
from dotenv import load_dotenv
load_dotenv()

from researcher import Researcher
from utils import show_prompt, get_notes_from_tool_calls, format_messages
from prompts import lead_researcher_prompt
from cache_strategy import CacheStrategyFactory

from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from utils import get_today_str, think_tool
from langchain.chat_models import init_chat_model

show_prompt(lead_researcher_prompt, "Lead Researcher Prompt")
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
    # Each sub-agent gets 3 iterations to research their specific topic
    researcher = Researcher(max_tool_call_iterations=3)
    return await researcher.start_research(research_brief=research_topic)

class Supervisor:
        
    # System constants
    # Maximum number of tool call iterations for individual researcher agents
    # This prevents infinite loops and controls research depth per topic
    __max_researcher_iterations = 6 # Calls to think_tool + conduct_research

    # Maximum number of concurrent research agents the supervisor can launch
    # This is passed to the lead_researcher_prompt to limit parallel research tasks
    __max_concurrent_researchers = 3
    
    # SUPERVISOR_MODEL = "anthropic:claude-sonnet-4-20250514"
    SUPERVISOR_MODEL = "xai:grok-code-fast-1"
    def __init__(self,
                 research_brief: str,
                 max_researcher_iterations: int = __max_researcher_iterations,
                 max_concurrent_research_units: int = __max_concurrent_researchers):
        # Initialize cache strategy based on model
        self.cache_strategy = CacheStrategyFactory.create_strategy(self.SUPERVISOR_MODEL)

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
        model = init_chat_model(model=self.SUPERVISOR_MODEL)
        self.model_with_tools = model.bind_tools([conduct_research, think_tool])
        
    async def start_supervision(self):
        # Create and append human message with cache strategy
        research_msg = self.cache_strategy.prepare_human_message(
            self.research_brief,
            add_cache=True  # Cache the initial research brief
        )
        self.messages.append(research_msg)

        # Invoke directly - messages already have cache from prepare_human_message
        response = await self.model_with_tools.ainvoke(self.messages)

        # Cleanup and append response
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        self.messages.append(response)
        
        researcher_iteration = 0
        
        # Only handle tool calls and not exceed the maximum number of iterations
        while response.tool_calls:
            # Check if we've hit the iteration limit BEFORE processing
            if researcher_iteration >= self.max_research_iterations:
                # Remove the last AI message with unfulfilled tool calls
                # to avoid OpenAI API error about missing tool responses
                self.messages.pop()
                break

            think_tool_calls = [
                tool_call for tool_call in response.tool_calls 
                if tool_call["name"] == "think_tool"
            ]
            
            conduct_search_calls = [
                tool_call for tool_call in response.tool_calls 
                if tool_call["name"] == "conduct_research"
            ]
            
            # Handle think_tool sync
            for tool_call in think_tool_calls:
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
                coroutines = [
                    conduct_research.ainvoke(tool_call["args"])
                    for tool_call in conduct_search_calls
                ]
                tool_results = await asyncio.gather(*coroutines)
                
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
            
            # Invoke directly - last tool message already has cache if needed
            response = await self.model_with_tools.ainvoke(self.messages)

            # Cleanup and append
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            self.messages.append(response)
            researcher_iteration += 1
        self.notes = get_notes_from_tool_calls(self.messages)
        return response

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
    supervisor = Supervisor(research_brief=BIG_BRIEF)
    result = await supervisor.start_supervision()
    format_messages(supervisor.messages)
        
if __name__ == "__main__":
    asyncio.run(main())