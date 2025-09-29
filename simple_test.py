#!/usr/bin/env python3
"""
Simple test for InsightGenerator with a more direct approach.
"""

import asyncio
import json
from pathlib import Path
from insight_generator import InsightGenerator

async def main():
    """Test the insight generator with a simpler approach."""

    # Load the notes
    with open("notes.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    research_brief = data["research_brief"]
    research_notes = data["research_notes"]

    print(f"🎨 Testing InsightGenerator")
    print(f"📊 Notes: {len(research_notes)}")
    print(f"📝 Brief: {research_brief[:60]}...")

    # Create generator with quiet mode
    generator = InsightGenerator(
        output_dir="reports/htmls",
        stream_callback=InsightGenerator.create_quiet_callback()
    )

    # Generate insight page
    success, output_path = await generator.generate_insight_page(
        research_notes=research_notes,
        research_brief=research_brief,
        filename="momo_test_insights.html",
        title="MoMo Business Efficiency Analysis"
    )

    print(f"Result: {'✅ Success' if success else '❌ Failed'}")
    print(f"Output: {output_path}")

    # Check if file exists
    if Path(output_path).exists():
        size = Path(output_path).stat().st_size
        print(f"File size: {size:,} bytes")
    else:
        print("File was not created")

if __name__ == "__main__":
    asyncio.run(main())