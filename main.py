#!/usr/bin/env python3
"""
Main entry point for the Deep Research System.

Usage:
    python main.py

This will run the complete multi-agent research pipeline including:
1. Clarification phase
2. Supervised research phase
3. Report generation
4. Insight page generation
"""

import asyncio
from src.deep_research_system import DeepResearch

async def main():
    """Run the complete deep research pipeline."""
    system = DeepResearch()

    # Get user input
    user_input = input("🔍 Enter your research topic: ").strip()
    if not user_input:
        print("❌ No research topic provided. Exiting.")
        return

    # Run the research pipeline
    try:
        report = await system.run(user_input)
        print(f"\n✅ Research completed successfully!")
        print(f"📄 Report saved to: {report}")
    except Exception as e:
        print(f"❌ Error during research: {e}")

if __name__ == "__main__":
    asyncio.run(main())