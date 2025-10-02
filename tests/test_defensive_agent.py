"""
Test script for Mr Tường Defensive Agent
Reads ZaloPay attack strategies and generates defensive briefs with logging
"""

import asyncio
import sys
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.agents.mrt_defensive_agent import MrTuongDefensiveAgent
from src.utils.helpers import console
from rich.panel import Panel
import re


async def test_defensive_agent():
    """Test Mr Tường defensive agent with ZaloPay attack strategies."""

    # Log file setup
    log_file = Path("test.log")

    def log(message: str):
        """Write to both console and log file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"

        # Write to log file
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)

        # Print to console
        print(log_entry, end='')

    # Clear log file
    log_file.write_text("", encoding='utf-8')

    log("=" * 80)
    log("Mr Tường Defensive Agent - Test Mode")
    log("=" * 80)

    # Read ZaloPay attack strategies
    attack_file = Path(".output/opponent_zalopay_attacks_20251002_1759.md")

    if not attack_file.exists():
        log(f"ERROR: Attack strategies file not found: {attack_file}")
        return

    log(f"Reading attack strategies from: {attack_file}")

    with open(attack_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract opponent name
    opponent_match = re.search(r'\*\*Company:\*\* (.+)', content)
    opponent_name = opponent_match.group(1) if opponent_match else "ZaloPay"
    log(f"Opponent: {opponent_name}")

    # Extract attack strategies
    strategies = []
    sections = content.split("## Exploitation Plan")
    for section in sections[1:]:
        strategy_text = section.split("---")[0].strip()
        if strategy_text:
            strategies.append(strategy_text)

    log(f"Extracted {len(strategies)} attack strategies")

    # Initialize defensive agent with debug logging
    log("\nInitializing Mr Tường Defensive Agent...")
    agent = MrTuongDefensiveAgent(max_tool_call_iterations=6, debug_log=True)

    # Generate defensive briefs
    log("\nGenerating defensive research briefs...")
    try:
        briefs = await agent.generate_defensive_briefs(
            opponent_name=opponent_name,
            attack_strategies=strategies
        )

        log(f"\nSUCCESS: Generated {len(briefs)} defensive research briefs")

        for i, brief in enumerate(briefs, 1):
            log(f"\n--- Defensive Brief {i} ---")
            log(brief[:500] + "..." if len(brief) > 500 else brief)

        log("\n" + "=" * 80)
        log("Test completed successfully!")
        log("=" * 80)

    except Exception as e:
        log(f"\nERROR: {str(e)}")
        import traceback
        log(traceback.format_exc())


if __name__ == "__main__":
    asyncio.run(test_defensive_agent())
