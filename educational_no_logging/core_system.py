"""
Deep Research System - Core Architecture (Minimal Educational Version)
======================================================================
This file contains only the essential classes to understand the system flow.
Utils and prompts are in separate files for clarity.
"""

import asyncio
from typing import Union
from datetime import datetime
from pathlib import Path
import re

from pydantic import BaseModel
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, filter_messages
from langchain_core.tools import tool

from prompts import (
    clarify_instructions, transform_to_brief_prompt,
    research_agent_prompt, lead_researcher_prompt,
    compress_prompt, final_report_prompt
)
from utils import (
    get_today_str, CacheStrategyFactory,
    tavily_search, think_tool
)


# ===========================
# 1. CLARIFIER
# ===========================

# Pydantic models for structured LLM output
class ClarifyWithUser(BaseModel):
    need_clarification: bool
    question: str
    verification: str

class ResearchQuestion(BaseModel):
    research_brief: str

class FlexibleResponse(BaseModel):
    response: Union[ClarifyWithUser, ResearchQuestion]  # Can return either clarification or brief


class ResearchBriefCreator:
    """Phase 1: Clarifies user intent and creates research brief."""

    def __init__(self):
        self.llm = init_chat_model(model="xai:grok-code-fast-1", temperature=0.0)
        self.structured_llm = self.llm.with_structured_output(FlexibleResponse)  # Forces structured response
        self.cache_strategy = CacheStrategyFactory.create_strategy("xai:grok-code-fast-1")

        system_msg = self.cache_strategy.prepare_system_message(
            f"You are a research assistant. Today's date is {get_today_str()}."
        )
        self.messages = [system_msg]

    def clarify_with_user(self, user_input: str):
        # Ask LLM if clarification is needed
        msg = self.cache_strategy.prepare_human_message(
            clarify_instructions.format(user_input=user_input),
            add_cache=True
        )
        self.messages.append(msg)

        while True:
            response = self.structured_llm.invoke(self.messages).response
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

            if isinstance(response, ClarifyWithUser):
                self.messages.append(AIMessage(content=str(response)))
                if not response.need_clarification:
                    return response  # No more questions needed

                # Interactive Q&A with user
                print(f"Q: {response.question}")
                answer = input("A: ")
                self.messages.append(
                    self.cache_strategy.prepare_human_message(answer, add_cache=True)
                )
            else:
                return response

    def write_research_brief(self) -> ResearchQuestion:
        # Transform conversation into structured research brief
        msg = self.cache_strategy.prepare_human_message(
            transform_to_brief_prompt,
            add_cache=True
        )
        self.messages.append(msg)

        response = self.structured_llm.invoke(self.messages).response
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        if isinstance(response, ResearchQuestion):
            return response
        raise ValueError(f"Expected ResearchQuestion, got {type(response)}")

    def run(self, user_input: str):
        self.clarify_with_user(user_input)
        return self.write_research_brief()


# ===========================
# 2. RESEARCHER
# ===========================

class Researcher:
    """Individual research agent that conducts searches."""

    def __init__(self, max_iterations: int = 3):
        self.model = init_chat_model(model="xai:grok-code-fast-1", max_tokens=64000)
        self.tools = [think_tool, tavily_search]  # Available tools: reflection & web search
        self.model_with_tools = self.model.bind_tools(self.tools)
        self.max_iterations = max_iterations  # Limit tool calls to prevent infinite loops
        self.cache_strategy = CacheStrategyFactory.create_strategy("xai:grok-code-fast-1")

        system_msg = self.cache_strategy.prepare_system_message(
            research_agent_prompt.format(date=get_today_str(), max_iterations=max_iterations)
        )
        self.messages = [system_msg]
        self.tools_by_name = {tool.name: tool for tool in self.tools}

    async def compress_research_findings(self) -> str:
        """Compress all research into a concise summary for the supervisor."""
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        msg = self.cache_strategy.prepare_human_message(
            compress_prompt.format(date=get_today_str()),
            add_cache=True
        )
        self.messages.append(msg)

        response = await self.model_with_tools.ainvoke(self.messages)
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        return str(response.content)

    async def start_research(self, research_brief: str):
        msg = self.cache_strategy.prepare_human_message(research_brief, add_cache=True)
        self.messages.append(msg)

        response = await self.model_with_tools.ainvoke(self.messages)
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        self.messages.append(response)

        # Tool-calling loop: LLM decides which tools to use
        iteration = 0
        while response.tool_calls and iteration < self.max_iterations:
            iteration += 1

            # Execute requested tools (search or think)
            observations = []
            for tool_call in response.tool_calls:
                tool = self.tools_by_name[tool_call["name"]]
                observations.append(await tool.ainvoke(tool_call["args"]))

            # Add tool results
            for i, (obs, call) in enumerate(zip(observations, response.tool_calls)):
                tool_msg = self.cache_strategy.prepare_tool_message(
                    obs, call["id"], add_cache=(i == len(observations) - 1)
                )
                self.messages.append(tool_msg)

            response = await self.model_with_tools.ainvoke(self.messages)
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            self.messages.append(response)

        return await self.compress_research_findings()


# ===========================
# 3. SUPERVISOR
# ===========================

@tool
async def conduct_research(research_topic: str) -> str:
    """Delegate research to a sub-agent. Each call spawns a new Researcher."""
    researcher = Researcher(max_iterations=3)
    return await researcher.start_research(research_topic)


class Supervisor:
    """Phase 2: Coordinates multiple research agents."""

    def __init__(self, research_brief: str, max_iterations: int = 6):
        self.research_brief = research_brief
        self.max_iterations = max_iterations  # Total iterations for all research
        self.cache_strategy = CacheStrategyFactory.create_strategy("xai:grok-code-fast-1")

        system_msg = self.cache_strategy.prepare_system_message(
            lead_researcher_prompt.format(
                date=get_today_str(),
                max_researcher_iterations=max_iterations,
                max_concurrent_research_units=3
            )
        )
        self.messages = [system_msg]

        model = init_chat_model(model="xai:grok-code-fast-1")
        self.model_with_tools = model.bind_tools([conduct_research, think_tool])

    async def start_supervision(self):
        msg = self.cache_strategy.prepare_human_message(self.research_brief, add_cache=True)
        self.messages.append(msg)

        response = await self.model_with_tools.ainvoke(self.messages)
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
        self.messages.append(response)

        # Supervisor's tool-calling loop
        iteration = 0
        while response.tool_calls and iteration < self.max_iterations:
            iteration += 1

            # Separate tool calls by type
            think_calls = [c for c in response.tool_calls if c["name"] == "think_tool"]
            research_calls = [c for c in response.tool_calls if c["name"] == "conduct_research"]

            # Handle think_tool synchronously
            for call in think_calls:
                result = think_tool.invoke(call["args"])
                msg = self.cache_strategy.prepare_tool_message(result, call["id"], add_cache=False)
                self.messages.append(msg)

            # Handle conduct_research in parallel (up to 3 concurrent)
            if research_calls:
                results = await asyncio.gather(*[
                    conduct_research.ainvoke(call["args"]) for call in research_calls
                ])

                for i, (result, call) in enumerate(zip(results, research_calls)):
                    msg = self.cache_strategy.prepare_tool_message(
                        result, call["id"], add_cache=(i == len(results) - 1)
                    )
                    self.messages.append(msg)

            response = await self.model_with_tools.ainvoke(self.messages)
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)
            self.messages.append(response)

        # Extract compressed research notes from all tool messages
        notes = [msg.content for msg in filter_messages(self.messages, include_types="tool")]
        return {"final_response": response.content, "notes": notes}


# ===========================
# 4. MAIN SYSTEM
# ===========================

class DeepResearch:
    """Phase 3: Orchestrates the pipeline and generates final report."""

    def __init__(self):
        self.writer_model = init_chat_model(model="anthropic:claude-sonnet-4-20250514", max_tokens=32000)
        self.cache_strategy = CacheStrategyFactory.create_strategy("anthropic:claude-sonnet-4-20250514")

    async def generate_final_report(self, research_brief: str, research_notes: list) -> str:
        findings = "\n\n".join(research_notes)
        prompt = final_report_prompt.format(
            research_brief=research_brief,
            findings=findings,
            date=get_today_str()
        )

        msg = self.cache_strategy.prepare_human_message(prompt, add_cache=False)
        response = await self.writer_model.ainvoke([msg])
        return response.content

    def save_report(self, report: str, user_input: str) -> str:
        # Create descriptive filename from user input
        short_desc = re.sub(r'[^a-zA-Z0-9_]+', '_', user_input[:50]).strip('_').lower()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"{short_desc}_{timestamp}.md"

        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        file_path = reports_dir / filename

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# Research Report\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"**Query:** {user_input}\n\n---\n\n")
            f.write(report)

        return str(file_path)

    async def run(self, user_input: str, save_to_file: bool = True) -> str:
        # Phase 1: Clarification - understand what user wants
        brief_creator = ResearchBriefCreator()
        result = brief_creator.run(user_input)
        research_brief = result.research_brief

        # Phase 2: Supervised Research - gather information
        supervisor = Supervisor(research_brief=research_brief)
        result = await supervisor.start_supervision()
        research_notes = result["notes"]  # Compressed findings from all researchers

        # Phase 3: Report Generation - create final document
        report = await self.generate_final_report(research_brief, research_notes)

        if save_to_file:
            self.save_report(report, user_input)

        return report


# ===========================
# EXAMPLE USAGE
# ===========================

async def main():
    system = DeepResearch()
    report = await system.run("What is LangChain and how does it work?")
    print(report)

if __name__ == "__main__":
    asyncio.run(main())