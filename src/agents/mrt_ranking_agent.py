"""
MrT Ranking Agent - MoMo CEO Report Evaluator
Reads final research reports and rates them 0-10 on strategic value, actionability, and quality.
"""

import asyncio
import glob
from typing import List, Literal
from pydantic import BaseModel, Field
from pathlib import Path
from datetime import datetime

from ..utils.helpers import get_today_str, console, init_xai_model
from ..utils.config import BOSS_MODEL, BOSS_TEMPERATURE
from ..prompts.persona_prompts import (
    MRT_RANKING_PERSONA,
    MRT_RANKING_PROMPT,
    MRT_RANKING_EXTRACTION_PROMPT
)
from rich.panel import Panel
from rich.table import Table


# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class ReportEvaluation(BaseModel):
    """Schema for extracting report evaluation from MrT's assessment."""
    overall_score: float = Field(description="Overall score 0-10 (average of 5 criteria)")
    strategic_relevance: int = Field(description="Strategic Relevance score 0-10", ge=0, le=10)
    actionability: int = Field(description="Actionability score 0-10", ge=0, le=10)
    insight_depth: int = Field(description="Insight Depth score 0-10", ge=0, le=10)
    data_quality: int = Field(description="Data Quality score 0-10", ge=0, le=10)
    competitive_advantage: int = Field(description="Competitive Advantage score 0-10", ge=0, le=10)
    justification: str = Field(description="2-3 sentences explaining the assessment")
    key_strengths: List[str] = Field(description="2-3 specific highlights from the report", min_items=2, max_items=3)
    areas_for_improvement: List[str] = Field(description="2-3 constructive suggestions", min_items=2, max_items=3)
    priority: Literal["HIGH", "MEDIUM", "LOW"] = Field(description="Priority level based on overall score")
    recommended_actions: List[str] = Field(description="1-2 specific next steps", min_items=1, max_items=2)


# ============================================================================
# MAIN CLASS
# ============================================================================

class MrTRankingAgent:
    """AI agent simulating MrT (MoMo CEO) evaluating research reports for strategic value."""

    def __init__(self, debug_log: bool = False):
        """Initialize MrT ranking agent.

        Args:
            debug_log: Enable debug logging (default False)
        """
        self.persona = MRT_RANKING_PERSONA
        self.debug_log = debug_log
        self.log_entries = []

        console.print(Panel(
            "[bold purple]📊 Initializing MrT Ranking Agent (Research Report Evaluator)[/bold purple]",
            border_style="purple"
        ))

        # Initialize log file path if debug logging is enabled
        if self.debug_log:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            log_dir = Path(".output/logs")
            log_dir.mkdir(parents=True, exist_ok=True)
            self.log_file_path = log_dir / f"mrt_ranking_{timestamp}.md"
            console.print(f"[dim yellow]Debug logging enabled: {self.log_file_path}[/dim yellow]")

        # Initialize model for evaluation (no tools needed)
        self.model = init_xai_model(
            model=BOSS_MODEL,
            temperature=BOSS_TEMPERATURE,
            max_tokens=8000
        )

        # Initialize structured output model
        self.structured_output_model = self.model.with_structured_output(ReportEvaluation)

        console.print(f"[dim]CEO: {self.persona['name']} ({self.persona['company']})[/dim]")
        console.print(f"[dim]Using model: {BOSS_MODEL}[/dim]")

    def _log(self, message: str, level: str = "INFO"):
        """Add log entry if debug logging is enabled."""
        if self.debug_log:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] [{level}] {message}"
            self.log_entries.append(log_entry)

    def _write_log_file(self):
        """Write accumulated log entries to file."""
        if self.debug_log and self.log_entries:
            with open(self.log_file_path, 'w', encoding='utf-8') as f:
                f.write(f"# Debug Log - MrT Report Ranking\n\n")
                f.write(f"**CEO:** {self.persona['name']}\n")
                f.write(f"**Company:** {self.persona['company']}\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("---\n\n")
                f.write("## Log Entries\n\n")
                for entry in self.log_entries:
                    f.write(f"{entry}\n\n")
            console.print(f"[green]📝 Debug log written to: {self.log_file_path}[/green]")

    async def evaluate_report(self, report_path: str, report_content: str) -> ReportEvaluation:
        """Evaluate a single research report.

        Args:
            report_path: Path to the report file
            report_content: Full content of the report

        Returns:
            ReportEvaluation with scores and assessment
        """
        report_name = Path(report_path).name
        console.print(f"\n[cyan]📄 Evaluating:[/cyan] {report_name}")
        self._log(f"Evaluating report: {report_name}")

        # Create evaluation prompt
        system_prompt = MRT_RANKING_PROMPT.format(
            name=self.persona["name"],
            title=self.persona["title"],
            company=self.persona["company"],
            background=self.persona["background"],
            evaluation_expertise=self.persona["evaluation_expertise"],
            date=get_today_str()
        )

        user_message = f"""# Report to Evaluate

**File**: {report_name}
**Path**: {report_path}

---

{report_content}

---

Your Task: Evaluate this research report using the five criteria (Strategic Relevance, Actionability, Insight Depth, Data Quality, Competitive Advantage). Provide detailed scores and assessment."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        self._log(f"Sending evaluation request for {report_name}")

        # Get evaluation from MrT
        response = await self.model.ainvoke(messages)
        response_content = str(response.content)

        self._log(f"Received evaluation response (length: {len(response_content)} chars)")

        # Extract structured evaluation
        extraction_prompt = MRT_RANKING_EXTRACTION_PROMPT.format(
            response_content=response_content
        )

        try:
            evaluation = await self.structured_output_model.ainvoke([
                {"role": "system", "content": "You are an expert at extracting structured evaluation data from MrT's report assessments."},
                {"role": "user", "content": extraction_prompt}
            ])

            # Calculate overall score from individual scores
            evaluation.overall_score = round(
                (evaluation.strategic_relevance +
                 evaluation.actionability +
                 evaluation.insight_depth +
                 evaluation.data_quality +
                 evaluation.competitive_advantage) / 5.0,
                1
            )

            # Determine priority based on overall score
            if evaluation.overall_score >= 8.0:
                evaluation.priority = "HIGH"
            elif evaluation.overall_score >= 6.0:
                evaluation.priority = "MEDIUM"
            else:
                evaluation.priority = "LOW"

            self._log(f"Successfully extracted evaluation for {report_name}: Overall={evaluation.overall_score}/10, Priority={evaluation.priority}")

            console.print(f"[green]✅ Evaluated:[/green] Overall Score = {evaluation.overall_score}/10 | Priority = {evaluation.priority}")

            return evaluation

        except Exception as e:
            console.print(f"[red]❌ Error extracting evaluation for {report_name}: {e}[/red]")
            self._log(f"Error in evaluation extraction: {e}", level="ERROR")
            # Return a default low-score evaluation
            return ReportEvaluation(
                overall_score=0.0,
                strategic_relevance=0,
                actionability=0,
                insight_depth=0,
                data_quality=0,
                competitive_advantage=0,
                justification="Failed to extract evaluation due to error.",
                key_strengths=["Error in evaluation", "Unable to assess"],
                areas_for_improvement=["Requires manual review", "Check evaluation logs"],
                priority="LOW",
                recommended_actions=["Manual review required"]
            )

    async def rank_reports(self, report_paths: List[str] = None) -> List[tuple[str, ReportEvaluation]]:
        """Rank multiple research reports.

        Args:
            report_paths: List of report file paths. If None, auto-discover from reports/

        Returns:
            List of (report_path, evaluation) tuples, sorted by overall_score descending
        """
        # Auto-discover reports if not specified
        if report_paths is None:
            console.print("[cyan]📁 Auto-discovering reports from reports/ directory...[/cyan]")
            report_paths = glob.glob("reports/*.md")

            if not report_paths:
                console.print("[red]❌ No reports found in reports/[/red]")
                return []

        console.print(Panel(
            f"[bold purple]📊 MrT Evaluating {len(report_paths)} Research Reports[/bold purple]",
            border_style="purple"
        ))

        evaluations = []

        for report_path in report_paths:
            try:
                # Read report content
                with open(report_path, 'r', encoding='utf-8') as f:
                    report_content = f.read()

                # Evaluate report
                evaluation = await self.evaluate_report(report_path, report_content)
                evaluations.append((report_path, evaluation))

            except FileNotFoundError:
                console.print(f"[red]❌ Report not found: {report_path}[/red]")
                self._log(f"Report not found: {report_path}", level="ERROR")
            except Exception as e:
                console.print(f"[red]❌ Error evaluating {report_path}: {e}[/red]")
                self._log(f"Error evaluating {report_path}: {e}", level="ERROR")

        # Sort by overall score descending
        evaluations.sort(key=lambda x: x[1].overall_score, reverse=True)

        # Display rankings table
        self._display_rankings_table(evaluations)

        # Save rankings to file
        self._save_rankings_to_file(evaluations)

        # Write debug log if enabled
        self._write_log_file()

        return evaluations

    def _display_rankings_table(self, evaluations: List[tuple[str, ReportEvaluation]]):
        """Display rankings in a pretty table."""
        table = Table(title="📊 MrT Report Rankings", title_style="bold purple")

        table.add_column("Rank", style="cyan", justify="center")
        table.add_column("Report", style="white")
        table.add_column("Overall", style="bold yellow", justify="center")
        table.add_column("Strat", justify="center")
        table.add_column("Action", justify="center")
        table.add_column("Insight", justify="center")
        table.add_column("Data", justify="center")
        table.add_column("Comp", justify="center")
        table.add_column("Priority", justify="center")

        for rank, (report_path, evaluation) in enumerate(evaluations, 1):
            report_name = Path(report_path).name[:40]

            # Color priority
            priority_color = {
                "HIGH": "green",
                "MEDIUM": "yellow",
                "LOW": "red"
            }.get(evaluation.priority, "white")

            table.add_row(
                f"#{rank}",
                report_name,
                f"{evaluation.overall_score}/10",
                str(evaluation.strategic_relevance),
                str(evaluation.actionability),
                str(evaluation.insight_depth),
                str(evaluation.data_quality),
                str(evaluation.competitive_advantage),
                f"[{priority_color}]{evaluation.priority}[/{priority_color}]"
            )

        console.print("\n")
        console.print(table)
        console.print("\n")

    def _save_rankings_to_file(self, evaluations: List[tuple[str, ReportEvaluation]]) -> str:
        """Save rankings to a markdown file.

        Args:
            evaluations: List of (report_path, evaluation) tuples

        Returns:
            Path to the saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"mrt_rankings_{timestamp}.md"

        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)
        file_path = output_dir / filename

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# MrT Report Rankings\n\n")
            f.write(f"**CEO:** {self.persona['name']}\n")
            f.write(f"**Company:** {self.persona['company']}\n")
            f.write(f"**Evaluated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\\n")
            f.write(f"**Total Reports:** {len(evaluations)}\n\n")
            f.write("---\n\n")

            # Summary statistics
            high_priority = sum(1 for _, e in evaluations if e.priority == "HIGH")
            medium_priority = sum(1 for _, e in evaluations if e.priority == "MEDIUM")
            low_priority = sum(1 for _, e in evaluations if e.priority == "LOW")
            avg_score = sum(e.overall_score for _, e in evaluations) / len(evaluations) if evaluations else 0

            f.write(f"## Summary Statistics\n\n")
            f.write(f"- **Average Score**: {avg_score:.1f}/10\n")
            f.write(f"- **HIGH Priority**: {high_priority} reports\n")
            f.write(f"- **MEDIUM Priority**: {medium_priority} reports\n")
            f.write(f"- **LOW Priority**: {low_priority} reports\n\n")
            f.write("---\n\n")

            # Detailed rankings
            for rank, (report_path, evaluation) in enumerate(evaluations, 1):
                report_name = Path(report_path).name

                f.write(f"## Rank #{rank}: {report_name}\n\n")
                f.write(f"**Overall Score**: {evaluation.overall_score}/10\n\n")

                f.write(f"### Detailed Scores\n\n")
                f.write(f"- **Strategic Relevance**: {evaluation.strategic_relevance}/10\n")
                f.write(f"- **Actionability**: {evaluation.actionability}/10\n")
                f.write(f"- **Insight Depth**: {evaluation.insight_depth}/10\n")
                f.write(f"- **Data Quality**: {evaluation.data_quality}/10\n")
                f.write(f"- **Competitive Advantage**: {evaluation.competitive_advantage}/10\n\n")

                f.write(f"### Assessment\n\n")
                f.write(f"**Priority**: {evaluation.priority}\n\n")
                f.write(f"**Justification**: {evaluation.justification}\n\n")

                f.write(f"**Key Strengths**:\n")
                for strength in evaluation.key_strengths:
                    f.write(f"- {strength}\n")
                f.write("\n")

                f.write(f"**Areas for Improvement**:\n")
                for improvement in evaluation.areas_for_improvement:
                    f.write(f"- {improvement}\n")
                f.write("\n")

                f.write(f"**Recommended Actions**:\n")
                for action in evaluation.recommended_actions:
                    f.write(f"- {action}\n")
                f.write("\n")

                f.write(f"**Report Path**: `{report_path}`\n\n")
                f.write("---\n\n")

        console.print(f"[green]📁 Rankings saved to: {file_path}[/green]")
        return str(file_path)


# ============================================================================
# DEMO/TEST FUNCTION
# ============================================================================

async def main():
    """Demo function to test MrT ranking agent."""
    console.print("[bold]═" * 80 + "[/bold]")
    console.print(Panel(
        "[bold purple]MrT Ranking Agent - Demo Mode[/bold purple]\\n"
        "Evaluating all research reports in reports/ directory",
        border_style="purple"
    ))
    console.print("[bold]═" * 80 + "[/bold]")

    # Initialize MrT ranking agent
    agent = MrTRankingAgent(debug_log=True)

    # Rank all reports
    rankings = await agent.rank_reports()

    if rankings:
        console.print("\\n[bold]═" * 80 + "[/bold]")
        console.print(Panel(
            f"[bold green]✅ MrT Evaluated {len(rankings)} Reports[/bold green]",
            border_style="green"
        ))

        # Show top 3 reports
        console.print("\\n[cyan]🏆 Top 3 Reports:[/cyan]\\n")
        for rank, (report_path, evaluation) in enumerate(rankings[:3], 1):
            report_name = Path(report_path).name
            console.print(f"[bold]#{rank}[/bold] {report_name}")
            console.print(f"   Score: {evaluation.overall_score}/10 | Priority: {evaluation.priority}")
            console.print(f"   {evaluation.justification[:100]}...\\n")

        console.print("[dim]Full rankings saved to .output/mrt_rankings_*.md[/dim]")
    else:
        console.print("\\n[yellow]⚠️ No reports found to evaluate[/yellow]")
        console.print("[dim]Generate reports first using: python -m src.agents.mrw_explorer Y[/dim]")

    console.print("[bold]═" * 80 + "[/bold]")


if __name__ == "__main__":
    asyncio.run(main())
