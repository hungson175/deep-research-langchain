"""
Example: Generate Insight Page from Research Notes

This demonstrates how to generate interactive HTML insight pages from research notes.
The insight page is a concise 2-4 page visual summary highlighting key findings.
"""

import asyncio
from insight_generator import generate_insight_from_notes

async def main():
    sample_research_notes = [
        """
        Research Note 1: Market Analysis
        - MoMo has 25M+ active users in Vietnam
        - Market share: ~40% in mobile payments
        - Main competitors: ZaloPay (VNG), ShopeePay (Sea Group)
        - Revenue grew 45% YoY in 2024
        """,
        """
        Research Note 2: Competitive Advantages
        - Strong brand recognition in Vietnam
        - Extensive merchant network (500K+ merchants)
        - Diverse product portfolio (payments, loans, insurance)
        - User engagement: 8-10 sessions/week average
        """,
        """
        Research Note 3: Challenges
        - Increasing competition from e-commerce platforms
        - Regulatory uncertainty around digital banking
        - Customer acquisition cost rising 20% annually
        - Profitability still not achieved
        """
    ]

    research_brief = "Analyze MoMo's business performance and competitive position in Vietnam"

    print("Generating insight page from research notes...")
    print(f"Notes: {len(sample_research_notes)}")
    print(f"Brief: {research_brief}\n")

    success, output_path = await generate_insight_from_notes(
        research_notes=sample_research_notes,
        research_brief=research_brief,
        output_filename="example_momo_insights",
        title="MoMo Business Analysis - Key Insights",
        quiet=False
    )

    if success:
        print(f"\n✅ Success! Insight page generated at: {output_path}")
        print("\nOpen the HTML file in your browser to view the interactive insights.")
    else:
        print(f"\n❌ Failed to generate insight page")
        print("Check if claude-code-sdk is installed: pip install claude-code-sdk")

if __name__ == "__main__":
    asyncio.run(main())