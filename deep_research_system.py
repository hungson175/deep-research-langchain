"""
Full Multi-Agent Research System (Non-LangGraph Implementation)
"""

import asyncio
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


class DeepResearch:

    WRITER_MODEL = "anthropic:claude-sonnet-4-20250514"

    def __init__(self):
        console.print(Panel("[bold magenta]🚀 Initializing Deep Research System[/bold magenta]", border_style="magenta"))
        console.print(f"[dim]Writer model: {self.WRITER_MODEL}[/dim]")

        self.writer_model = init_chat_model(model=self.WRITER_MODEL, max_tokens=32000)
        self.cache_strategy = CacheStrategyFactory.create_strategy(self.WRITER_MODEL)
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

    async def run(self, user_input: str) -> str:
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

        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel("[bold green]✨ DEEP RESEARCH COMPLETE[/bold green]", border_style="green"))
        console.print("[bold]═" * 80 + "[/bold]\n")

        return report

async def main():
    console.print("[bold]█" * 80 + "[/bold]")
    console.print(Panel("[bold cyan]DEEP RESEARCH SYSTEM - DEMO MODE[/bold cyan]", border_style="cyan", padding=(1, 2)))
    console.print("[bold]█" * 80 + "[/bold]")

    system = DeepResearch()

    # user_input = "Compare Deep Research products from OpenAI vs Google"
    user_input = "Impact of Gen AI coding tools on software engineering jobs, especially juniors - and solutions for team/tech companies"
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