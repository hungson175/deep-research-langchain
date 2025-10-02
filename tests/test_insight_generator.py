#!/usr/bin/env python3
"""
Test script for InsightGenerator using the extracted notes from the MoMo vs competitors report.
"""

import asyncio
import json
from pathlib import Path
from src.core.insight_generator import generate_insight_from_notes

async def main():
    """Test the insight generator with the extracted notes."""

    # Load the notes from the JSON file
    notes_file = Path("notes.json")
    if not notes_file.exists():
        print("❌ notes.json file not found!")
        return

    with open(notes_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    research_brief = data["research_brief"]
    research_notes = data["research_notes"]

    print(f"📊 Loaded {len(research_notes)} research notes")
    print(f"📝 Research brief: {research_brief[:100]}...")

    # Generate the insight page
    output_filename = "momo_competitors_insights"
    title = "MoMo vs ZaloPay & VNPay: Business Efficiency Analysis"

    print(f"\n🎨 Generating insight page: {output_filename}.html")
    print(f"📊 Input: {len(research_notes)} notes, {sum(len(note) for note in research_notes):,} characters")

    try:
        success, output_path = await generate_insight_from_notes(
            research_notes=research_notes,
            research_brief=research_brief,
            output_filename=output_filename,
            title=title,
            quiet=False  # Show detailed progress
        )

        if success:
            print(f"\n✅ Success! Insight page saved to: {output_path}")

            # Show file info
            file_path = Path(output_path)
            if file_path.exists():
                file_size = file_path.stat().st_size
                print(f"📊 File size: {file_size:,} bytes")

                # Check if it's valid HTML
                content = file_path.read_text(encoding='utf-8')
                if "<!DOCTYPE" in content and "<html>" in content:
                    print("✅ Valid HTML structure detected")
                    print(f"📄 Content length: {len(content):,} characters")
                else:
                    print("⚠️  File exists but may not be valid HTML")
                    print(f"📄 Content preview: {content[:200]}...")
        else:
            print(f"\n❌ Failed to generate insight page")
            print(f"📍 Expected output path: {output_path}")

    except Exception as e:
        print(f"❌ Error during generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("🚀 Testing InsightGenerator with MoMo competitors analysis")
    asyncio.run(main())