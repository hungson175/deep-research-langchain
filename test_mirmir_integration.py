#!/usr/bin/env python
"""Test script for MirMir Agent integration with Supervisor."""

import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from supervisor import Supervisor
from utils import console
from rich.panel import Panel


async def test_momo_query():
    """Test direct MoMo data query through supervisor."""
    console.print(Panel("[bold yellow]Testing MirMir Integration[/bold yellow]", border_style="yellow"))

    # Create a research brief that asks for MoMo data
    research_brief = """
    I need to analyze MoMo's business performance for Q1 2025.
    Please get me the following data:
    1. GMV (Gross Merchandise Volume) của MoMo từ 1/1/2025 đến 31/3/2025, KHÔNG cần chart
    2. Number of active users trong cùng thời gian
    3. Transaction volume trends

    Also research general Vietnamese fintech market trends for comparison.
    """

    # Initialize supervisor
    supervisor = Supervisor(
        research_brief=research_brief,
        max_researcher_iterations=3,
        max_concurrent_research_units=2
    )

    # Start supervision
    result = await supervisor.start_supervision()

    # Display results
    console.print(Panel("[bold green]✅ Test Complete[/bold green]", border_style="green"))
    console.print(f"\n[bold]Final Response:[/bold]\n{result['final_response']}")
    console.print(f"\n[bold]Research Notes Collected:[/bold] {len(result['notes'])}")

    return result


async def test_direct_agent():
    """Test MirMir Agent directly without supervisor."""
    console.print(Panel("[bold yellow]Testing Direct MirMir Agent[/bold yellow]", border_style="yellow"))

    from mirmir_research_agent import MirMirResearchAgent

    try:
        agent = MirMirResearchAgent()
        query = "GMV của MoMo từ 1/1/2025 đến 31/1/2025, KHÔNG cần chart"

        console.print(f"[cyan]Query: {query}[/cyan]")
        result = agent.query_momo_data(query)

        console.print(Panel("[bold green]✅ Direct Test Complete[/bold green]", border_style="green"))
        console.print(f"\n[bold]Result:[/bold]\n{result}")

        return result
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        return None


async def main():
    """Run all tests."""
    console.print("[bold]═" * 80 + "[/bold]")
    console.print("[bold cyan]MirMir Integration Test Suite[/bold cyan]")
    console.print("[bold]═" * 80 + "[/bold]\n")

    # Test 1: Direct agent test
    console.print("\n[bold]Test 1: Direct MirMir Agent[/bold]")
    console.print("-" * 40)
    direct_result = await test_direct_agent()

    # Test 2: Supervisor integration test
    console.print("\n[bold]Test 2: Supervisor with MirMir Integration[/bold]")
    console.print("-" * 40)
    supervisor_result = await test_momo_query()

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print("[bold cyan]All Tests Complete![/bold cyan]")
    console.print("[bold]═" * 80 + "[/bold]")


if __name__ == "__main__":
    asyncio.run(main())