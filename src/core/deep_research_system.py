"""
Full Multi-Agent Research System (Non-LangGraph Implementation)
"""

import asyncio
import re
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from ..agents.clarifier import ResearchBriefCreator
from ..agents.supervisor import Supervisor
from ..utils.helpers import get_today_str, console, init_xai_model
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, TimeElapsedColumn
from rich.markdown import Markdown
from rich.table import Table
from ..prompts.system_prompts import final_report_generation_prompt
from ..utils.cache_strategy import CacheStrategyFactory
from ..utils.config import WRITER_MODEL, WRITER_TEMPERATURE, WRITER_MAX_TOKENS
USER_INPUT = "So sánh hiệu quả hiệu quả business của MoMo với cách đối thủ mạnh nhất ở Việt Nam: Zalo Pay, VNPay , và đưa ra giải pháp để phát triển, dựa trên bài học từ chính các đối thủ đó, và các công ty thành công khác ở Trung Quốc"

class DeepResearch:

    def __init__(self):
        console.print(Panel("[bold magenta]🚀 Initializing Deep Research System[/bold magenta]", border_style="magenta"))
        console.print(f"[dim]Writer model: {WRITER_MODEL}[/dim]")

        self.writer_model = init_xai_model(model=WRITER_MODEL, temperature=WRITER_TEMPERATURE, max_tokens=WRITER_MAX_TOKENS)
        self.cache_strategy = CacheStrategyFactory.create_strategy(f"xai:{WRITER_MODEL}")
        console.print(f"[dim]Cache strategy: {self.cache_strategy.__class__.__name__}[/dim]")

        self.metrics = {
            "phase_times": {},
            "phase_tokens": {},
            "total_tokens": 0,
            "total_time": 0
        }

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
            if hasattr(response, 'usage_metadata') and response.usage_metadata:
                phase3_tokens = response.usage_metadata.get('total_tokens', 0)
                self.metrics["phase_tokens"]["Phase 3: Report"] = phase3_tokens
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

    async def run(
        self,
        user_input: str,
        save_to_file: bool = True,
        generate_insights: bool = True,
        skip_clarifier: bool = False,
        research_brief: str = None
    ) -> str:
        """Run the deep research system.

        Args:
            user_input: User's research query or brief description
            save_to_file: Whether to save the final report to a file
            generate_insights: Whether to generate HTML insight page
            skip_clarifier: If True, skip Phase 1 clarification and use research_brief directly
            research_brief: Pre-formed research brief (required if skip_clarifier=True)

        Returns:
            The final research report as a string
        """
        total_start_time = time.time()

        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel("[bold cyan]🎯 DEEP RESEARCH SYSTEM - STARTING[/bold cyan]", border_style="cyan"))
        console.print("[bold]═" * 80 + "[/bold]\n")

        # Phase 1: Clarify and get research brief (optional)
        if skip_clarifier:
            if not research_brief:
                raise ValueError("research_brief must be provided when skip_clarifier=True")
            console.print(Panel("[bold blue]PHASE 1: CLARIFICATION - SKIPPED[/bold blue]\n[dim]Using pre-formed research brief[/dim]", border_style="blue"))
            console.print(f"\n[cyan]Research Brief:[/cyan]\n{research_brief[:500]}...\n")
        else:
            console.print(Panel("[bold blue]PHASE 1: CLARIFICATION & BRIEF CREATION[/bold blue]", border_style="blue"))
            phase1_start = time.time()
            brief_creator = ResearchBriefCreator()
            result = brief_creator.run(user_input)
            research_brief = result.research_brief
            self.metrics["phase_times"]["Phase 1: Clarification"] = time.time() - phase1_start
            self.metrics["phase_tokens"]["Phase 1: Clarification"] = getattr(brief_creator, 'total_tokens', 0)

        # Phase 2: Conduct supervised research
        console.print("\n" + "=" * 80 + "\n")
        console.print(Panel("[bold yellow]PHASE 2: SUPERVISED RESEARCH[/bold yellow]", border_style="yellow"))
        phase2_start = time.time()
        supervisor = Supervisor(research_brief=research_brief)
        result = await supervisor.start_supervision()
        research_notes = result["notes"]
        self.metrics["phase_times"]["Phase 2: Research"] = time.time() - phase2_start
        self.metrics["phase_tokens"]["Phase 2: Research"] = getattr(supervisor, 'total_tokens', 0)

        # Phase 3: Generate final report
        console.print("\n" + "=" * 80 + "\n")
        console.print(Panel("[bold magenta]PHASE 3: REPORT GENERATION[/bold magenta]", border_style="magenta"))
        phase3_start = time.time()
        report = await self.generate_final_report(research_brief, research_notes)
        self.metrics["phase_times"]["Phase 3: Report"] = time.time() - phase3_start

        # Save report to file if requested
        if save_to_file:
            self._save_report_to_file(report, user_input)

        # Phase 4: Generate insight page
        if generate_insights:
            console.print("\n" + "=" * 80 + "\n")
            console.print(Panel("[bold cyan]PHASE 4: INSIGHT PAGE GENERATION[/bold cyan]", border_style="cyan"))
            phase4_start = time.time()
            await self._generate_insight_page(research_notes, research_brief, user_input)
            self.metrics["phase_times"]["Phase 4: Insights"] = time.time() - phase4_start

        self.metrics["total_time"] = time.time() - total_start_time
        self.metrics["total_tokens"] = sum(self.metrics["phase_tokens"].values())

        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel("[bold green]✨ DEEP RESEARCH COMPLETE[/bold green]", border_style="green"))
        self._display_metrics()
        console.print("[bold]═" * 80 + "[/bold]\n")

        return report

    def _display_metrics(self):
        """Display performance metrics in a nice table."""
        table = Table(title="📊 Performance Metrics", show_header=True, header_style="bold cyan")
        table.add_column("Phase", style="white", width=30)
        table.add_column("Time", style="yellow", justify="right")
        table.add_column("Tokens", style="green", justify="right")

        for phase_name, phase_time in self.metrics["phase_times"].items():
            tokens = self.metrics["phase_tokens"].get(phase_name, 0)
            time_str = f"{phase_time:.2f}s"
            token_str = f"{tokens:,}" if tokens > 0 else "N/A"
            table.add_row(phase_name, time_str, token_str)

        table.add_row("─" * 30, "─" * 10, "─" * 10, style="dim")
        table.add_row(
            "[bold]TOTAL",
            f"[bold]{self.metrics['total_time']:.2f}s",
            f"[bold]{self.metrics['total_tokens']:,}" if self.metrics['total_tokens'] > 0 else "[bold]N/A"
        )

        console.print("\n")
        console.print(table)
        console.print("\n")

    async def _generate_insight_page(self, research_notes: list, research_brief: str, user_input: str):
        """Generate interactive HTML insight page from research notes."""
        try:
            from ..core.insight_generator import generate_insight_from_notes

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

RESEARCH_BRIEF = """
 Enhancing Gen Z Engagement Through Social Payment Features
Clear Research Objective: How can ZaloPay (VNG Corporation) leverage Zalo's social graph to capture Gen Z and millennial users from MoMo by introducing superior social payment features like group gifting and viral P2P transfers?

Background Context: MoMo's internal data reveals fluctuating and declining P2P transfer volumes in 2025 (e.g., drops from 13.7M transactions in January to 10.3M in July), with inconsistent group fund engagement (active users peaking at 2.5M in August but falling to 1.6M in September). Public sentiment shows 90% of Gen Z users (18-24) employ multiple super apps for promotions, indicating low stickiness and underserved social integration needs. ZaloPay can exploit this gap, as Zalo's 75M+ users (dominant for messaging and groups) provide a seamless entry point for viral, social-driven payments that MoMo's standalone app lacks, targeting Gen Z's preference for peer-influenced, FOMO-driven transactions (67% social influence per reviews).

Specific Investigation Areas:

Use query_momo_data to query: "Engagement metrics of MoMo's P2P and group features among users aged 18-35 in Q1-Q3 2025" and "Decline reasons in P2P transaction volumes by month in 2025."
Use tavily_search for: "Gen Z payment preferences Vietnam 2025 social features reviews MoMo vs ZaloPay" and "Viral social payment trends TikTok Zalo integrations 2025."
Analyze ZaloPay internal data on current Zalo-integrated P2P usage; survey 1,000 Gen Z Zalo users on desired features (e.g., in-app gifting tied to chats).
Expected Strategic Insights: This research will identify precise Gen Z pain points in MoMo (e.g., lack of seamless group sharing) and quantify ZaloPay's potential uplift (e.g., 20-30% engagement boost via social virality). It will enable decisions on feature prioritization, such as launching Zalo-chat-embedded payments, and A/B testing viral campaigns to convert 10-15% of MoMo's multi-app Gen Z users.

Success Metrics: Increase ZaloPay's Gen Z active users by 25% within 6 months; achieve 15% higher P2P transaction frequency vs. MoMo benchmarks (measured via internal analytics); track net promoter score (NPS) improvement to 70+ among 18-24 segment through post-launch surveys.
"""
# RESEARCH_BRIEF = """Adoption of AI and Emerging Technologies in MoMo's Payment Innovations

# **Research Objective/Question:** Examine the integration of AI, blockchain, and RTPs in Vietnam's fintech ecosystem, and develop a strategy for MoMo to adopt these for productivity gains and disruption resilience amid SEA's digital payment surge.

# **Background Context:** SEA's digital payments are set to hit $789B in 2025, with RTPs reaching $11T by 2028 and AI driving 7-9% cost savings for firms like MoMo. As mobile wallets surpass cards (66% POS share by 2027), technologies like AI for fraud prevention (e.g., Visa's $3B investments) and blockchain for cross-border QR payments (e.g., with Thailand) offer MoMo opportunities to enhance efficiency and user experience. However, lagging adoption could expose MoMo to transformational disruption from tech-savvy competitors like VNG's ZaloPay, especially in a market with 32.77M e-wallet users and rapid ecommerce growth, while talent challenges and regulatory hurdles (e.g., AI labeling from 2025) pose risks to innovation.

# **Specific Areas to Investigate:**
# - Tech trends: 2025 adoption rates of AI in credit scoring, blockchain for interoperability, and RTPs in Vietnam/SEA, including MoMo's current vs. competitor implementations (e.g., VNPAY's QR integrations).
# - Productivity impacts: Case studies on AI-driven savings (e.g., 9% revenue growth in SEA) and blockchain's role in reducing cross-border fees.
# - Regulatory landscape: SBV guidelines on AI in payments, plus ASEAN initiatives like RPC for regional connectivity.
# - Internal capabilities: MoMo's tech stack gaps, talent acquisition needs (e.g., AI specialists), and pilot opportunities via the 2025 sandbox.
# - User shifts: Behavioral data on Gen Z preferences for voice payments, crypto, and AI personalization in transactions.

# **Expected Insights or Outcomes:** A phased adoption roadmap for AI/blockchain to cut operational costs by 15% and boost transaction volumes by 20-25%, with scenarios for leading versus lagging in the 2025-2028 digital payment race."""
async def main():
    console.print("[bold]█" * 80 + "[/bold]")
    console.print(Panel("[bold cyan]DEEP RESEARCH SYSTEM - DEMO MODE[/bold cyan]", border_style="cyan", padding=(1, 2)))
    console.print("[bold]█" * 80 + "[/bold]")

    system = DeepResearch()

    # Example 1: Normal mode with clarifier
    # user_input = "Compare Deep Research products from OpenAI vs Google"
    # report = await system.run(user_input)

    # Example 2: Skip clarifier mode with pre-formed brief
    # Copy-paste a research brief from .output/mrT_topics_*.md here
    

    user_input = "AI and Emerging Tech for MoMo Payments"  # Short description for filename
    console.print(f"\n[bold]Research Mode:[/bold] Skip Clarifier (MrT-generated brief)\n")

    report = await system.run(
        user_input=user_input,
        skip_clarifier=True,
        research_brief=RESEARCH_BRIEF
    )

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