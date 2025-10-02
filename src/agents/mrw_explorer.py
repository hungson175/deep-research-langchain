"""
MrW Explorer - Automated Deep Research Pipeline
Generates strategic topics and runs sequential deep research on each.
"""

import asyncio
from typing import Literal
from datetime import datetime
from pathlib import Path
from rich.panel import Panel
from rich.table import Table

from .topics_generator import TopicsGenerator
from ..core.deep_research_system import DeepResearch
from ..utils.helpers import console


class MrWExplorer:
    """Pipeline to generate topics and run deep research sequentially."""

    def __init__(self):
        console.print(Panel(
            "[bold magenta]🔬 MrW Explorer - Automated Research Pipeline[/bold magenta]",
            border_style="magenta"
        ))
        self.topics_generator = None
        self.deep_research = None
        self.results = []

    async def run_pipeline(
        self,
        period: Literal["D", "W", "M", "Q", "Y"],
        save_reports: bool = True,
        generate_insights: bool = True
    ):
        """Run the complete pipeline: generate topics → research each sequentially.

        Args:
            period: Time period for topic generation (D/W/M/Q/Y)
            save_reports: Whether to save reports to files
            generate_insights: Whether to generate HTML insight pages
        """
        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel(
            "[bold cyan]🚀 STARTING MRW EXPLORER PIPELINE[/bold cyan]",
            border_style="cyan"
        ))
        console.print("[bold]═" * 80 + "[/bold]\n")

        # Step 1: Generate Topics
        console.print(Panel(
            "[bold green]STEP 1: GENERATING STRATEGIC TOPICS[/bold green]",
            border_style="green"
        ))

        self.topics_generator = TopicsGenerator(max_tool_call_iterations=5)
        research_briefs = await self.topics_generator.generate_topics(period)

        console.print(f"\n[green]✅ Generated {len(research_briefs)} research briefs[/green]\n")

        # Step 2: Run Deep Research on Each Topic Sequentially
        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel(
            f"[bold yellow]STEP 2: RUNNING DEEP RESEARCH ON {len(research_briefs)} TOPICS[/bold yellow]\n"
            f"[dim]Sequential execution (not parallel)[/dim]",
            border_style="yellow"
        ))
        console.print("[bold]═" * 80 + "[/bold]\n")

        self.deep_research = DeepResearch()

        for idx, research_brief in enumerate(research_briefs, 1):
            console.print(f"\n[bold cyan]{'━' * 80}[/bold cyan]")
            console.print(Panel(
                f"[bold magenta]📊 Research {idx}/{len(research_briefs)}[/bold magenta]",
                border_style="magenta"
            ))
            console.print(f"[cyan]Brief Preview:[/cyan] {research_brief[:200]}...\n")

            try:
                # Generate short description from brief for filename
                brief_title = research_brief.split('\n')[0][:50].strip()
                user_input = f"MrT_Topic_{idx}_{brief_title}"

                # Run deep research with clarifier skipped
                report = await self.deep_research.run(
                    user_input=user_input,
                    skip_clarifier=True,
                    research_brief=research_brief,
                    save_to_file=save_reports,
                    generate_insights=generate_insights
                )

                self.results.append({
                    "brief_number": idx,
                    "brief_preview": brief_title,
                    "status": "success",
                    "report_length": len(report)
                })

                console.print(f"[green]✅ Research {idx}/{len(research_briefs)} completed[/green]")

            except Exception as e:
                console.print(f"[red]❌ Research {idx} failed: {e}[/red]")
                self.results.append({
                    "brief_number": idx,
                    "brief_preview": brief_title if 'brief_title' in locals() else "Unknown",
                    "status": "failed",
                    "error": str(e)
                })

        # Step 3: Display Summary
        console.print("\n\n[bold]═" * 80 + "[/bold]")
        console.print(Panel(
            "[bold green]✨ MRW EXPLORER PIPELINE COMPLETE[/bold green]",
            border_style="green"
        ))
        console.print("[bold]═" * 80 + "[/bold]\n")

        self._display_summary()

    def _display_summary(self):
        """Display pipeline execution summary."""
        table = Table(
            title="📊 Pipeline Execution Summary",
            show_header=True,
            header_style="bold cyan"
        )
        table.add_column("#", style="white", width=5)
        table.add_column("Brief Preview", style="cyan", width=50)
        table.add_column("Status", style="white", width=10)
        table.add_column("Report Size", style="green", width=15, justify="right")

        for result in self.results:
            status_icon = "✅" if result["status"] == "success" else "❌"
            status = f"{status_icon} {result['status']}"

            report_size = (
                f"{result['report_length']:,} chars"
                if result["status"] == "success"
                else "N/A"
            )

            table.add_row(
                str(result["brief_number"]),
                result["brief_preview"][:50],
                status,
                report_size
            )

        console.print(table)
        console.print("\n")

        # Success/Failure counts
        success_count = sum(1 for r in self.results if r["status"] == "success")
        failed_count = len(self.results) - success_count

        console.print(f"[green]✅ Successful: {success_count}[/green]")
        console.print(f"[red]❌ Failed: {failed_count}[/red]")
        console.print(f"[cyan]📁 Reports saved to: ./reports/[/cyan]")
        console.print(f"[cyan]🎨 Insights saved to: ./reports/htmls/[/cyan]\n")


async def main():
    """Demo/CLI entry point for MrW Explorer."""
    import sys

    console.print("[bold]█" * 80 + "[/bold]")
    console.print(Panel(
        "[bold cyan]MrW EXPLORER - DEMO MODE[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    ))
    console.print("[bold]█" * 80 + "[/bold]")

    # Parse CLI args or use default
    period = sys.argv[1] if len(sys.argv) > 1 else "Y"

    if period not in ["D", "W", "M", "Q", "Y"]:
        console.print(f"[red]Invalid period: {period}. Use D/W/M/Q/Y[/red]")
        console.print("[yellow]Usage: python -m src.mrw_explorer [D|W|M|Q|Y][/yellow]")
        console.print("[yellow]Defaulting to Yearly (Y)[/yellow]")
        period = "Y"

    console.print(f"\n[bold]Period:[/bold] {period} (Yearly)\n")

    # Run pipeline
    explorer = MrWExplorer()
    await explorer.run_pipeline(
        period=period,
        save_reports=True,
        generate_insights=True
    )

    console.print("\n[bold]█" * 80 + "[/bold]")


if __name__ == "__main__":
    asyncio.run(main())