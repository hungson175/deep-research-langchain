"""
Full Multi-Agent Research System (Non-LangGraph Implementation)
"""

import asyncio
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from clarifier import ResearchBriefCreator
from supervisor import Supervisor
from utils import get_today_str
from prompts import final_report_generation_prompt
from cache_strategy import CacheStrategyFactory


class DeepResearch:

    WRITER_MODEL = "anthropic:claude-sonnet-4-20250514"

    def __init__(self):
        self.writer_model = init_chat_model(model=self.WRITER_MODEL, max_tokens=32000)
        self.cache_strategy = CacheStrategyFactory.create_strategy(self.WRITER_MODEL)

    async def generate_final_report(self, research_brief: str, research_notes: list) -> str:
        findings = "\n\n".join(research_notes)

        final_prompt = final_report_generation_prompt.format(
            research_brief=research_brief,
            findings=findings,
            date=get_today_str()
        )

        report_msg = self.cache_strategy.prepare_human_message(
            final_prompt,
            add_cache=False  # No need to cache, it's even more expensive to cache
        )

        response = await self.writer_model.ainvoke([report_msg])
        return response.content

    async def run(self, user_input: str) -> str:
        # Phase 1: Clarify and get research brief
        brief_creator = ResearchBriefCreator()
        result = brief_creator.run(user_input)
        research_brief = result.research_brief

        # Phase 2: Conduct supervised research
        supervisor = Supervisor(research_brief=research_brief)
        result = await supervisor.start_supervision()
        research_notes = result["notes"]

        # Phase 3: Generate final report
        return await self.generate_final_report(research_brief, research_notes)

async def main():
    system = DeepResearch()

    user_input = "Compare Deep Research products from OpenAI vs Google"
    report = await system.run(user_input)

    print(report)


if __name__ == "__main__":
    asyncio.run(main())