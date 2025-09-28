"""
Full Multi-Agent Research System (Non-LangGraph Implementation)
"""

import asyncio
import re
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from clarifier import ResearchBriefCreator
from supervisor import Supervisor
from utils import get_today_str, console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.markdown import Markdown
from prompts import final_report_generation_prompt
from cache_strategy import CacheStrategyFactory
from config import WRITER_MODEL
USER_INPUT = "So sánh hiệu quả hiệu quả business của MoMo với cách đối thủ mạnh nhất ở Việt Nam: Zalo Pay, VNPay , và đưa ra giải pháp để phát triển, dựa trên bài học từ chính các đối thủ đó, và các công ty thành công khác ở Trung Quốc"

class DeepResearch:

    def __init__(self):
        console.print(Panel("[bold magenta]🚀 Initializing Deep Research System[/bold magenta]", border_style="magenta"))
        console.print(f"[dim]Writer model: {WRITER_MODEL}[/dim]")

        self.writer_model = init_chat_model(model=WRITER_MODEL, max_tokens=32000)
        self.cache_strategy = CacheStrategyFactory.create_strategy(WRITER_MODEL)
        console.print(f"[dim]Cache strategy: {self.cache_strategy.__class__.__name__}[/dim]")

    async def generate_final_report(self, research_brief: str, research_notes: list) -> str:
        console.print(Panel(f"[bold magenta]📝 Generating Final Report[/bold magenta]\n\nUsing {len(research_notes)} research notes", border_style="magenta"))

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

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("[magenta]Writing comprehensive report...", total=None)
            response = await self.writer_model.ainvoke([report_msg])
            progress.update(task, completed=True)

        console.print("[green]✅ Final report generation complete[/green]")
        return response.content

    def _save_report_to_file(self, report: str, user_input: str) -> str:
        """Save the report to a markdown file in the reports directory.

        Args:
            report: The generated report content
            user_input: The original user input to create a descriptive filename

        Returns:
            The path to the saved report file
        """
        # Create a short description from user input (first 50 chars, alphanumeric only)
        short_desc = re.sub(r'[^a-zA-Z0-9_]+', '_', user_input[:50]).strip('_').lower()

        # Create timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        # Create filename
        filename = f"{short_desc}_{timestamp}.md"

        # Ensure reports directory exists
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)

        # Full path
        file_path = reports_dir / filename

        # Save the report
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# Research Report\n\n")
            f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"**Query:** {user_input}\n\n")
            f.write("---\n\n")
            f.write(report)

        console.print(f"[green]📁 Report saved to: {file_path}[/green]")
        return str(file_path)

    async def run(self, user_input: str, save_to_file: bool = True, generate_insights: bool = True) -> str:
        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel("[bold cyan]🎯 DEEP RESEARCH SYSTEM - STARTING[/bold cyan]", border_style="cyan"))
        console.print("[bold]═" * 80 + "[/bold]\n")

        # Phase 1: Clarify and get research brief
        console.print(Panel("[bold blue]PHASE 1: CLARIFICATION & BRIEF CREATION[/bold blue]", border_style="blue"))
        brief_creator = ResearchBriefCreator()
        result = brief_creator.run(user_input)
        research_brief = result.research_brief

        # Phase 2: Conduct supervised research
        console.print("\n" + "=" * 80 + "\n")
        console.print(Panel("[bold yellow]PHASE 2: SUPERVISED RESEARCH[/bold yellow]", border_style="yellow"))
        supervisor = Supervisor(research_brief=research_brief)
        result = await supervisor.start_supervision()
        research_notes = result["notes"]

        # Phase 3: Generate final report
        console.print("\n" + "=" * 80 + "\n")
        console.print(Panel("[bold magenta]PHASE 3: REPORT GENERATION[/bold magenta]", border_style="magenta"))
        report = await self.generate_final_report(research_brief, research_notes)

        # Save report to file if requested
        if save_to_file:
            self._save_report_to_file(report, user_input)

        # Phase 4: Generate insight page
        if generate_insights:
            console.print("\n" + "=" * 80 + "\n")
            console.print(Panel("[bold cyan]PHASE 4: INSIGHT PAGE GENERATION[/bold cyan]", border_style="cyan"))
            await self._generate_insight_page(research_notes, research_brief, user_input)

        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel("[bold green]✨ DEEP RESEARCH COMPLETE[/bold green]", border_style="green"))
        console.print("[bold]═" * 80 + "[/bold]\n")

        return report

    async def _generate_insight_page(self, research_notes: list, research_brief: str, user_input: str):
        """Generate interactive HTML insight page from research notes."""
        try:
            from insight_generator import generate_insight_from_notes

            short_desc = re.sub(r'[^a-zA-Z0-9_]+', '_', user_input[:50]).strip('_').lower()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            filename = f"insights_{short_desc}_{timestamp}"

            success, output_path = await generate_insight_from_notes(
                research_notes=research_notes,
                research_brief=research_brief,
                output_filename=filename,
                title=user_input[:100]
            )

            if success:
                console.print(f"[green]🎨 Insight page saved to: {output_path}[/green]")
            else:
                console.print(f"[yellow]⚠️ Insight page generation encountered issues[/yellow]")

        except ImportError:
            console.print("[yellow]⚠️ Insight generation unavailable: claude-code-sdk not installed[/yellow]")
            console.print("[dim]Install with: pip install claude-code-sdk[/dim]")
        except Exception as e:
            console.print(f"[red]❌ Error generating insight page: {e}[/red]")

async def main():
    console.print("[bold]█" * 80 + "[/bold]")
    console.print(Panel("[bold cyan]DEEP RESEARCH SYSTEM - DEMO MODE[/bold cyan]", border_style="cyan", padding=(1, 2)))
    console.print("[bold]█" * 80 + "[/bold]")

    system = DeepResearch()

    # user_input = "Compare Deep Research products from OpenAI vs Google"
    user_input = USER_INPUT
    console.print(f"\n[bold]User Input:[/bold] {user_input}\n")

    report = await system.run(user_input)

    # Display the final report in a nice panel
    console.print("\n" + "=" * 80 + "\n")
    console.print(Panel("[bold green]📄 FINAL RESEARCH REPORT[/bold green]", border_style="green"))
    console.print("\n")

    # Use Markdown rendering for better formatting
    md = Markdown(report)
    console.print(md)

    console.print("\n[bold]█" * 80 + "[/bold]")


if __name__ == "__main__":
    asyncio.run(main())