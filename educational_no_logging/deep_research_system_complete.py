"""
Deep Research System - Educational Version (Without Logging)
=============================================================

This is a consolidated version of the multi-agent research system built with LangChain.
All logging and visual formatting have been removed for educational clarity.

System Architecture:
1. ResearchBriefCreator: Clarifies user intent and creates research briefs
2. Supervisor: Coordinates multiple research agents
3. Researcher: Individual agents that conduct searches
4. DeepResearch: Main orchestrator that generates final reports

Dependencies:
- langchain
- tavily-python
- anthropic
- xai-sdk (for Grok models)
- python-dotenv
"""

import asyncio
from datetime import datetime
from pathlib import Path
from typing import Union, List
import re
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage, filter_messages
from langchain_core.tools import tool
from tavily import TavilyClient

load_dotenv()

# ===========================
# CACHE STRATEGY MODULE
# ===========================

class MessageCacheStrategy:
    """Base class for message caching strategies."""

    def prepare_system_message(self, content: str) -> SystemMessage:
        return SystemMessage(content=content)

    def prepare_human_message(self, content: str, add_cache: bool = False) -> HumanMessage:
        return HumanMessage(content=content)

    def prepare_tool_message(self, content: str, tool_call_id: str, add_cache: bool = False) -> ToolMessage:
        return ToolMessage(content=content, tool_call_id=tool_call_id)

    def cleanup_messages_after_invoke(self, messages: list) -> list:
        return messages


class AnthropicCacheStrategy(MessageCacheStrategy):
    """Cache strategy for Anthropic models using cache_control."""

    def prepare_system_message(self, content: str) -> SystemMessage:
        return SystemMessage(
            content=[{"type": "text", "text": content, "cache_control": {"type": "ephemeral"}}]
        )

    def prepare_human_message(self, content: str, add_cache: bool = False) -> HumanMessage:
        if add_cache:
            return HumanMessage(
                content=[{"type": "text", "text": content, "cache_control": {"type": "ephemeral"}}]
            )
        return HumanMessage(content=content)

    def prepare_tool_message(self, content: str, tool_call_id: str, add_cache: bool = False) -> ToolMessage:
        if add_cache:
            return ToolMessage(
                content=[{"type": "text", "text": content, "cache_control": {"type": "ephemeral"}}],
                tool_call_id=tool_call_id
            )
        return ToolMessage(content=content, tool_call_id=tool_call_id)

    def cleanup_messages_after_invoke(self, messages: list) -> list:
        cleaned_messages = []
        for msg in messages:
            if isinstance(msg, (SystemMessage, HumanMessage, ToolMessage)):
                if isinstance(msg.content, list):
                    clean_content = []
                    for item in msg.content:
                        if isinstance(item, dict) and "cache_control" in item:
                            clean_item = item.copy()
                            del clean_item["cache_control"]
                            clean_content.append(clean_item)
                        else:
                            clean_content.append(item)

                    if isinstance(msg, SystemMessage):
                        cleaned_messages.append(SystemMessage(content=clean_content))
                    elif isinstance(msg, HumanMessage):
                        cleaned_messages.append(HumanMessage(content=clean_content))
                    elif isinstance(msg, ToolMessage):
                        cleaned_messages.append(ToolMessage(content=clean_content, tool_call_id=msg.tool_call_id))
                else:
                    cleaned_messages.append(msg)
            else:
                cleaned_messages.append(msg)
        return cleaned_messages


class CacheStrategyFactory:
    """Factory for creating appropriate cache strategies based on model."""

    @staticmethod
    def create_strategy(model_name: str) -> MessageCacheStrategy:
        if "anthropic" in model_name.lower() or "claude" in model_name.lower():
            return AnthropicCacheStrategy()
        return MessageCacheStrategy()


# ===========================
# UTILITY FUNCTIONS
# ===========================

def get_today_str() -> str:
    """Get current date in a human-readable format."""
    return datetime.now().strftime("%a %b %-d, %Y")


def get_notes_from_tool_calls(messages: list) -> list[str]:
    """Extract research notes from ToolMessage objects in supervisor message history."""
    return [tool_msg.content for tool_msg in filter_messages(messages, include_types="tool")]


# ===========================
# PROMPTS MODULE
# ===========================

# Clarification prompts
human_clarify_with_user_instructions = """
The user is asking for a research report on the following topic:
<user_input>
{user_input}
</user_input>

Please analyze this request and determine if you need any clarification before proceeding with the research.
Consider if the scope is clear, if there are any ambiguities, or if additional context would help produce a better report.
"""

human_transform_messages_into_research_topic_prompt = """
Based on our conversation above, please transform the user's request and any clarifications into a single,
comprehensive research brief that will guide the research process. This should be a detailed description
of what needs to be researched, including all relevant context and requirements discussed.
"""

# Research agent prompt
research_agent_prompt = """You are a research agent tasked with gathering comprehensive information on a specific topic.

Current date: {date}

You have access to the following tools:
1. tavily_search: Search the web for current information
2. think_tool: Reflect on your research progress and plan next steps

Research Process:
1. After each search, use think_tool to analyze what you've found and what's still needed
2. Focus on finding concrete, factual information with specific examples
3. Gather information from multiple reputable sources
4. You have a maximum of {max_iterations} iterations to complete your research

Quality Guidelines:
- Prioritize recent, authoritative sources
- Look for specific data, statistics, and real examples
- Ensure comprehensive coverage of the topic
- Verify important claims across multiple sources
"""

# Lead researcher prompt
lead_researcher_prompt = """You are the lead researcher coordinating a team of specialized research agents.

Current date: {date}

Your role is to:
1. Analyze the research brief and break it down into specific research tasks
2. Delegate these tasks to specialized sub-agents using the conduct_research tool
3. Use the think_tool to reflect on progress and plan next steps
4. Synthesize findings from all sub-agents

Guidelines:
- You can launch up to {max_concurrent_research_units} concurrent research agents
- Each agent should have a focused, specific research task
- You have {max_researcher_iterations} total iterations to complete the research
- Ensure comprehensive coverage by assigning complementary research angles
"""

# Compression prompt
compress_research_combined_prompt = """Current date: {date}

Review the research conducted above and create a comprehensive, well-organized summary of all findings.

Requirements:
1. Preserve ALL important information, data, and sources
2. Organize findings into logical sections
3. Maintain specific examples, statistics, and quotes
4. Keep source attributions and URLs
5. Ensure the summary is complete and self-contained

Format the summary in a clear, structured manner that will be useful for report generation."""

# Final report generation prompt
final_report_generation_prompt = """You are a professional report writer tasked with creating a comprehensive research report.

Current date: {date}

Research Brief:
{research_brief}

Research Findings:
{findings}

Please create a well-structured, professional report that:
1. Provides a comprehensive analysis of the topic
2. Is organized with clear sections and subsections
3. Includes all relevant data, examples, and insights from the research
4. Maintains an objective, informative tone
5. Properly attributes sources where mentioned
6. Concludes with key takeaways and insights

Format the report in Markdown with appropriate headers, lists, and emphasis where needed."""

# Webpage summarization prompt (for Tavily)
summarize_webpage_prompt = """Current date: {date}

Please summarize the following webpage content, focusing on extracting:
1. Key information and main points
2. Important data, statistics, or facts
3. Notable quotes or statements
4. Relevant examples or case studies

Webpage content:
{webpage_content}

Provide a concise but comprehensive summary that preserves all important information."""


# ===========================
# SEARCH TOOLS
# ===========================

# Initialize Tavily client
tavily_client = TavilyClient()
SUMMARIZATION_MODEL = "xai:grok-code-fast-1"
summarization_model = init_chat_model(model=SUMMARIZATION_MODEL)


class Summary(BaseModel):
    """Schema for webpage content summarization."""
    summary: str = Field(description="Concise summary of the webpage content")
    key_excerpts: str = Field(description="Important quotes and excerpts from the content")


def summarize_webpage_content(webpage_content: str) -> str:
    """Summarize webpage content using the configured summarization model."""
    try:
        structured_model = summarization_model.with_structured_output(Summary)
        summary = structured_model.invoke([
            HumanMessage(content=summarize_webpage_prompt.format(
                webpage_content=webpage_content,
                date=get_today_str()
            ))
        ])
        formatted_summary = (
            f"<summary>\n{summary.summary}\n</summary>\n\n"
            f"<key_excerpts>\n{summary.key_excerpts}\n</key_excerpts>"
        )
        return formatted_summary
    except Exception as e:
        print(f"Failed to summarize webpage: {str(e)}")
        return webpage_content[:1000] + "..." if len(webpage_content) > 1000 else webpage_content


@tool(parse_docstring=True)
def tavily_search(query: str, max_results: int = 3, topic: str = "general") -> str:
    """Fetch results from Tavily search API with content summarization.

    Args:
        query: A single search query to execute
        max_results: Maximum number of results to return
        topic: Topic to filter results by ('general', 'news', 'finance')

    Returns:
        Formatted string of search results with summaries
    """
    # Execute search
    search_result = tavily_client.search(
        query,
        max_results=max_results,
        include_raw_content=True,
        topic=topic
    )

    # Process results
    unique_results = {}
    for result in search_result['results']:
        url = result['url']
        if url not in unique_results:
            unique_results[url] = result

    # Summarize content
    summarized_results = {}
    for url, result in unique_results.items():
        if not result.get("raw_content"):
            content = result['content']
        else:
            content = summarize_webpage_content(result['raw_content'])

        summarized_results[url] = {
            'title': result['title'],
            'content': content
        }

    # Format output
    if not summarized_results:
        return "No valid search results found. Please try different search queries."

    formatted_output = "Search results: \n\n"
    for i, (url, result) in enumerate(summarized_results.items(), 1):
        formatted_output += f"\n\n--- SOURCE {i}: {result['title']} ---\n"
        formatted_output += f"URL: {url}\n\n"
        formatted_output += f"SUMMARY:\n{result['content']}\n\n"
        formatted_output += "-" * 80 + "\n"

    return formatted_output


@tool(parse_docstring=True)
def think_tool(reflection: str) -> str:
    """Tool for strategic reflection on research progress and decision-making.

    Use this tool after each search to analyze results and plan next steps systematically.

    Args:
        reflection: Your detailed reflection on research progress, findings, gaps, and next steps

    Returns:
        Confirmation that reflection was recorded for decision-making
    """
    return f"Reflection recorded: {reflection}"


# ===========================
# CLARIFIER MODULE
# ===========================

class ClarifyWithUser(BaseModel):
    """Response for user clarification."""
    need_clarification: bool = Field(
        description="Whether the user needs to be asked a clarifying question."
    )
    question: str = Field(
        description="A question to ask the user to clarify the report scope"
    )
    verification: str = Field(
        description="Verify message that we will start research after the user has provided the necessary information."
    )


class ResearchQuestion(BaseModel):
    """Schema for structured research brief generation."""
    research_brief: str = Field(
        description="A research question that will be used to guide the research."
    )


class FlexibleResponse(BaseModel):
    """Flexible response that can be either clarification or research brief."""
    response: Union[ClarifyWithUser, ResearchQuestion]


class ResearchBriefCreator:
    """Handles user interaction to clarify research intent and create research briefs."""

    CLARIFIER_MODEL = "xai:grok-code-fast-1"
    SYSTEM_PROMPT = """
    You are a research assistant that is helping the user to clarify their request for a research report then write a research brief.
    Today's date is {date}.
    """

    def __init__(self):
        self.llm = init_chat_model(model=self.CLARIFIER_MODEL, temperature=0.0)
        self.structured_output_model = self.llm.with_structured_output(FlexibleResponse)
        self.cache_strategy = CacheStrategyFactory.create_strategy(self.CLARIFIER_MODEL)

        system_msg = self.cache_strategy.prepare_system_message(
            self.SYSTEM_PROMPT.format(date=get_today_str())
        )
        self.messages = [system_msg]

    def clarify_with_user(self, user_input: str):
        clarify_msg = self.cache_strategy.prepare_human_message(
            human_clarify_with_user_instructions.format(user_input=user_input),
            add_cache=True
        )
        self.messages.append(clarify_msg)

        while True:
            flexible_response = self.structured_output_model.invoke(self.messages)
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            response = flexible_response.response

            if isinstance(response, ClarifyWithUser):
                self.messages.append(AIMessage(
                    content=f"Need clarification: {response.need_clarification}\n"
                           f"Question: {response.question}\n"
                           f"Verification: {response.verification}"
                ))

                if not response.need_clarification:
                    return response

                print(f"Clarification needed: {response.question}")
                user_answer = input("Your answer: ")

                answer_msg = self.cache_strategy.prepare_human_message(
                    user_answer,
                    add_cache=True
                )
                self.messages.append(answer_msg)
            else:
                return response

    def write_research_brief(self) -> ResearchQuestion:
        transform_msg = self.cache_strategy.prepare_human_message(
            human_transform_messages_into_research_topic_prompt,
            add_cache=True
        )
        self.messages.append(transform_msg)

        flexible_response = self.structured_output_model.invoke(self.messages)
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        response = flexible_response.response

        if isinstance(response, ResearchQuestion):
            self.messages.append(AIMessage(content=f"Research brief: {response.research_brief}"))
            return response
        else:
            raise ValueError(f"Expected ResearchQuestion, got {type(response)}")

    def run(self, user_input: str):
        self.clarify_with_user(user_input)
        research_brief = self.write_research_brief()
        return research_brief


# ===========================
# RESEARCHER MODULE
# ===========================

class Researcher:
    """Individual research agent that conducts searches and gathers information."""

    __RESEARCHER_MODEL = "xai:grok-code-fast-1"

    def __init__(self, max_tool_call_iterations: int = 3):
        self.model = init_chat_model(model=self.__RESEARCHER_MODEL, max_tokens=64000)
        self.tools = [think_tool, tavily_search]
        self.model_with_tools = self.model.bind_tools(self.tools)
        self.max_tool_call_iterations = max_tool_call_iterations

        self.cache_strategy = CacheStrategyFactory.create_strategy(self.__RESEARCHER_MODEL)

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
        """Compress research findings while preserving all relevant information."""
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        combined_compression_prompt = compress_research_combined_prompt.format(date=get_today_str())
        compression_msg = self.cache_strategy.prepare_human_message(
            combined_compression_prompt,
            add_cache=True
        )
        self.messages.append(compression_msg)

        response = await self.model_with_tools.ainvoke(self.messages)
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        self.compressed_research = str(response.content)
        self.messages.append(response)

        return self.compressed_research

    async def start_research(self, research_brief: str):
        research_msg = self.cache_strategy.prepare_human_message(
            research_brief,
            add_cache=True
        )
        self.messages.append(research_msg)

        response = await self.model_with_tools.ainvoke(self.messages)
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        self.messages.append(response)

        tool_call_iterations = 0

        while response.tool_calls:
            if tool_call_iterations >= self.max_tool_call_iterations:
                self.messages.pop()
                break

            tool_call_iterations += 1
            observations = []
            for tool_call in response.tool_calls:
                tool = self.tools_by_name[tool_call["name"]]
                observations.append(await tool.ainvoke(tool_call["args"]))

            tool_outputs = []
            for i, (observation, tool_call) in enumerate(zip(observations, response.tool_calls)):
                is_last = (i == len(observations) - 1)
                tool_msg = self.cache_strategy.prepare_tool_message(
                    observation,
                    tool_call["id"],
                    add_cache=is_last
                )
                tool_outputs.append(tool_msg)

            self.messages.extend(tool_outputs)

            response = await self.model_with_tools.ainvoke(self.messages)
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            self.messages.append(response)

        self.compressed_research = await self.compress_research_findings()
        return self.compressed_research


# ===========================
# SUPERVISOR MODULE
# ===========================

@tool
async def conduct_research(research_topic: str) -> str:
    """Tool for delegating a research task to a specialized sub-agent.

    Args:
        research_topic: The topic to research. Should be a single topic, described in high detail.

    Returns:
        The research findings.
    """
    researcher = Researcher(max_tool_call_iterations=3)
    return await researcher.start_research(research_brief=research_topic)


class Supervisor:
    """Coordinates multiple research agents to conduct comprehensive research."""

    __max_researcher_iterations = 6
    __max_concurrent_researchers = 3
    SUPERVISOR_MODEL = "xai:grok-code-fast-1"

    def __init__(self,
                 research_brief: str,
                 max_researcher_iterations: int = __max_researcher_iterations,
                 max_concurrent_research_units: int = __max_concurrent_researchers):

        self.cache_strategy = CacheStrategyFactory.create_strategy(self.SUPERVISOR_MODEL)

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
        research_msg = self.cache_strategy.prepare_human_message(
            self.research_brief,
            add_cache=True
        )
        self.messages.append(research_msg)

        response = await self.model_with_tools.ainvoke(self.messages)
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        self.messages.append(response)

        researcher_iteration = 0

        while response.tool_calls:
            if researcher_iteration >= self.max_research_iterations:
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
                tool_msg = self.cache_strategy.prepare_tool_message(
                    observation,
                    tool_call["id"],
                    add_cache=False
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
                    is_last = (i == len(tool_results) - 1)
                    tool_msg = self.cache_strategy.prepare_tool_message(
                        result,
                        tool_call["id"],
                        add_cache=is_last
                    )
                    research_tool_messages.append(tool_msg)
                self.messages.extend(research_tool_messages)

            response = await self.model_with_tools.ainvoke(self.messages)
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            self.messages.append(response)
            researcher_iteration += 1

        self.notes = get_notes_from_tool_calls(self.messages)
        return {
            "final_response": response.content,
            "notes": self.notes
        }


# ===========================
# MAIN SYSTEM MODULE
# ===========================

class DeepResearch:
    """Main orchestrator for the complete research system."""

    WRITER_MODEL = "anthropic:claude-sonnet-4-20250514"

    def __init__(self):
        self.writer_model = init_chat_model(model=self.WRITER_MODEL, max_tokens=32000)
        self.cache_strategy = CacheStrategyFactory.create_strategy(self.WRITER_MODEL)

    async def generate_final_report(self, research_brief: str, research_notes: list) -> str:
        """Generate the final research report from collected notes."""
        findings = "\n\n".join(research_notes)

        final_prompt = final_report_generation_prompt.format(
            research_brief=research_brief,
            findings=findings,
            date=get_today_str()
        )

        report_msg = self.cache_strategy.prepare_human_message(
            final_prompt,
            add_cache=False
        )

        response = await self.writer_model.ainvoke([report_msg])
        return response.content

    def _save_report_to_file(self, report: str, user_input: str) -> str:
        """Save the report to a markdown file in the reports directory."""
        # Create a short description from user input
        short_desc = re.sub(r'[^a-zA-Z0-9_]+', '_', user_input[:50]).strip('_').lower()

        # Create timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        # Create filename
        filename = f"{short_desc}_{timestamp}.md"

        # Ensure reports directory exists
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        # Full path
        file_path = reports_dir / filename

        # Save the report
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# Research Report\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"**Query:** {user_input}\n\n")
            f.write("---\n\n")
            f.write(report)

        print(f"Report saved to: {file_path}")
        return str(file_path)

    async def run(self, user_input: str, save_to_file: bool = True) -> str:
        """Run the complete research process."""
        print("\n" + "="*80)
        print("DEEP RESEARCH SYSTEM - STARTING")
        print("="*80 + "\n")

        # Phase 1: Clarify and get research brief
        print("PHASE 1: CLARIFICATION & BRIEF CREATION")
        print("-"*40)
        brief_creator = ResearchBriefCreator()
        result = brief_creator.run(user_input)
        research_brief = result.research_brief
        print(f"Research Brief: {research_brief[:200]}...")

        # Phase 2: Conduct supervised research
        print("\n" + "-"*40)
        print("PHASE 2: SUPERVISED RESEARCH")
        print("-"*40)
        supervisor = Supervisor(research_brief=research_brief)
        result = await supervisor.start_supervision()
        research_notes = result["notes"]
        print(f"Collected {len(research_notes)} research notes")

        # Phase 3: Generate final report
        print("\n" + "-"*40)
        print("PHASE 3: REPORT GENERATION")
        print("-"*40)
        report = await self.generate_final_report(research_brief, research_notes)

        # Save report to file if requested
        if save_to_file:
            self._save_report_to_file(report, user_input)

        print("\n" + "="*80)
        print("DEEP RESEARCH COMPLETE")
        print("="*80 + "\n")

        return report


# ===========================
# MAIN EXECUTION
# ===========================

async def main():
    """Example usage of the Deep Research System."""
    system = DeepResearch()

    # Example queries
    user_input = "Impact of Gen AI coding tools on software engineering jobs, especially juniors - and solutions for team/tech companies"
    # user_input = "Compare Deep Research products from OpenAI vs Google"

    print(f"User Input: {user_input}\n")

    report = await system.run(user_input)

    # Display the final report
    print("\n" + "="*80)
    print("FINAL RESEARCH REPORT")
    print("="*80 + "\n")
    print(report)


if __name__ == "__main__":
    asyncio.run(main())