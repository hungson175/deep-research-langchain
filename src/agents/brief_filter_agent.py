"""
Brief Filter Agent - Deduplicates and consolidates similar research briefs
Simple LLM-based agent to identify and merge duplicate/similar research topics
"""

import asyncio
from typing import List
from pydantic import BaseModel, Field
from datetime import datetime
from pathlib import Path

from ..utils.helpers import init_xai_model
from ..utils.config import BOSS_MODEL, BOSS_TEMPERATURE


# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class FilteredBrief(BaseModel):
    """A unique research brief after deduplication."""
    title: str = Field(description="Brief title/summary")
    content: str = Field(description="Full research brief content")
    merged_from: List[str] = Field(description="List of original brief titles that were merged into this one")


class FilteredBriefs(BaseModel):
    """Collection of filtered unique research briefs."""
    briefs: List[FilteredBrief] = Field(description="List of unique research briefs after filtering")
    total_input: int = Field(description="Total number of input briefs")
    total_output: int = Field(description="Total number of unique briefs after filtering")
    duplicates_removed: int = Field(description="Number of duplicates removed")


# ============================================================================
# PROMPTS
# ============================================================================

BRIEF_FILTER_SYSTEM_PROMPT = """You are an expert research brief analyst tasked with identifying and consolidating duplicate or highly similar research briefs.

Your Task:
1. Read all provided research briefs carefully
2. Identify briefs that are duplicates or cover substantially similar topics (>70% overlap)
3. Merge similar briefs into single consolidated briefs
4. Preserve unique briefs as-is
5. Return a deduplicated list of research briefs

Merging Guidelines:
- Briefs are duplicates if they ask the same core question with different wording
- Briefs are similar if they investigate the same topic from slightly different angles
- When merging, combine the best elements from both briefs (clearest objective, most comprehensive investigation areas)
- Preserve strategic context and expected insights from both briefs
- Keep the merged brief comprehensive but concise

Output Requirements:
- Each unique brief should have: title, full content, list of original brief titles merged into it
- If a brief is unique (not merged), merged_from should contain only its own title
- Prioritize quality over quantity - better to have fewer comprehensive briefs than many overlapping ones"""


BRIEF_FILTER_USER_MESSAGE = """Here are {num_briefs} research briefs to analyze and filter:

{briefs_text}

---

Your task: Identify duplicates and similar briefs, then consolidate them into a deduplicated list. Return the filtered briefs with clear indication of which original briefs were merged."""


# ============================================================================
# MAIN CLASS
# ============================================================================

class BriefFilterAgent:
    """Simple LLM agent to filter duplicate/similar research briefs."""

    def __init__(self):
        """Initialize brief filter agent."""
        print("🔍 Initializing Brief Filter Agent")

        # Initialize model for filtering
        self.model = init_xai_model(
            model=BOSS_MODEL,
            temperature=BOSS_TEMPERATURE,
            max_tokens=16000
        )

        # Initialize structured output model
        self.structured_output_model = self.model.with_structured_output(FilteredBriefs)

        print(f"Using model: {BOSS_MODEL}")

    async def filter_duplicates(self, briefs: List[dict]) -> List[dict]:
        """Filter duplicate and similar briefs from a list.

        Args:
            briefs: List of research brief dictionaries (each with 'title' and 'content' keys)

        Returns:
            Filtered list of unique research briefs
        """
        if not briefs:
            print("⚠️ No briefs to filter")
            return []

        print(f"\n🔍 Filtering {len(briefs)} Research Briefs")

        # Format briefs for LLM
        briefs_text = ""
        for i, brief in enumerate(briefs, 1):
            title = brief.get('title', f'Brief {i}')
            content = brief.get('content', brief.get('research_objective', ''))
            briefs_text += f"\n### Brief {i}: {title}\n\n{content}\n\n---\n"

        # Create filtering prompt
        user_message = BRIEF_FILTER_USER_MESSAGE.format(
            num_briefs=len(briefs),
            briefs_text=briefs_text
        )

        messages = [
            {"role": "system", "content": BRIEF_FILTER_SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]

        print("📊 Analyzing briefs for duplicates...")

        try:
            # Get filtered briefs from LLM
            filtered_result = await self.structured_output_model.ainvoke(messages)

            print(f"✅ Filtering complete:")
            print(f"   Input: {filtered_result.total_input} briefs")
            print(f"   Output: {filtered_result.total_output} unique briefs")
            print(f"   Removed: {filtered_result.duplicates_removed} duplicates")

            # Convert back to dict format
            unique_briefs = []
            for brief in filtered_result.briefs:
                unique_briefs.append({
                    'title': brief.title,
                    'content': brief.content,
                    'merged_from': brief.merged_from
                })

            return unique_briefs

        except Exception as e:
            print(f"❌ Error filtering briefs: {e}")
            print("⚠️ Returning original briefs without filtering")
            return briefs


# ============================================================================
# DEMO/TEST FUNCTION
# ============================================================================

async def main():
    """Demo function to test brief filter agent."""
    print("=" * 80)
    print("Brief Filter Agent - Demo Mode")
    print("Testing deduplication with sample briefs")
    print("=" * 80)

    # Sample briefs with some duplicates
    sample_briefs = [
        {
            "title": "Gen Z Payment Preferences in Vietnam",
            "content": "Research Gen Z (ages 18-25) payment app preferences and usage patterns in Vietnam market"
        },
        {
            "title": "Youth Digital Wallet Adoption",
            "content": "Study how young Vietnamese users (18-25) adopt and use digital wallet applications"
        },
        {
            "title": "MoMo Competition from Banking Apps",
            "content": "Analyze competitive threats from traditional banks launching mobile payment apps"
        },
        {
            "title": "Gen Z Payment Behavior Analysis",
            "content": "Investigate payment preferences and digital wallet usage among Vietnamese youth aged 18-25"
        },
        {
            "title": "Cross-border Payment Opportunities",
            "content": "Explore international payment features and remittance services for Vietnamese users"
        }
    ]

    # Initialize filter agent
    agent = BriefFilterAgent()

    # Filter briefs
    filtered_briefs = await agent.filter_duplicates(sample_briefs)

    print("\n" + "=" * 80)
    print(f"✅ Filtered {len(sample_briefs)} briefs → {len(filtered_briefs)} unique briefs")

    for i, brief in enumerate(filtered_briefs, 1):
        print(f"\nUnique Brief {i}: {brief['title']}")
        print(f"  Merged from: {', '.join(brief['merged_from'])}")

    print("=" * 80)


if __name__ == "__main__":
    asyncio.run(main())
