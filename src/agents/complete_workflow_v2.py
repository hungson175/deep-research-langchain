"""
Complete Workflow V2 - Resumable Implementation
Runs all 5 phases with state tracking and resume capability.
Saves progress after each step to allow resuming from failures.
"""

import asyncio
import json
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field

from .topics_generator import TopicsGenerator
from .opp_ceo_agent_topic_generator import OpponentCEOTopicGenerator
from .mrt_defensive_agent import MrTuongDefensiveAgent
from .brief_filter_agent import BriefFilterAgent
from .mrt_ranking_agent import MrTRankingAgent
from ..core.deep_research_system import DeepResearch
from ..utils.helpers import console, get_today_str
from rich.panel import Panel
from rich.table import Table


# ============================================================================
# STATE MANAGEMENT
# ============================================================================

class WorkflowState(BaseModel):
    """Workflow state for resumability."""
    session_id: str
    period: str
    current_phase: float = 0  # 0, 1, 2, 2.5, 3, 4 N_SONPH: should we hard-code the int or use constant ?
    completed_steps: List[str] = Field(default_factory=list)

    # N_SONPH: where is the state file saved ?
    
    # Phase outputs
    mrt_topics_file: Optional[str] = None
    opponent_attacks_files: Dict[str, str] = Field(default_factory=dict)  # {ceo_type: file_path}
    defensive_briefs_files: Dict[str, str] = Field(default_factory=dict)  # {opponent: file_path}
    filtered_briefs: List[dict] = Field(default_factory=list)  # In-memory after Phase 2.5
    completed_reports: List[str] = Field(default_factory=list)
    rankings_file: Optional[str] = None

    # Phase 3 granular tracking
    total_briefs: int = 0
    current_brief_index: int = 0
    pending_briefs: List[dict] = Field(default_factory=list)

    # Metadata
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())


# ============================================================================
# STATE PERSISTENCE
# ============================================================================

def get_state_dir() -> Path:
    """Get state directory."""
    state_dir = Path(".output/workflow_states")
    state_dir.mkdir(parents=True, exist_ok=True)
    return state_dir


def get_state_file(session_id: str) -> Path:
    """Get state file path."""
    return get_state_dir() / f"{session_id}.json"


def save_state(state: WorkflowState):
    """Save workflow state to disk."""
    state.updated_at = datetime.now().isoformat()
    state_file = get_state_file(state.session_id)

    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(state.model_dump(), f, indent=2, ensure_ascii=False)

    console.print(f"[dim]💾 State saved: {state_file}[/dim]")


def load_state(session_id: str) -> WorkflowState:
    """Load workflow state from disk."""
    state_file = get_state_file(session_id)

    if not state_file.exists():
        raise FileNotFoundError(f"State file not found: {state_file}")

    with open(state_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return WorkflowState(**data)


def state_exists(session_id: str) -> bool:
    """Check if state file exists."""
    return get_state_file(session_id).exists()


def list_sessions() -> List[str]:
    """List all available sessions."""
    state_dir = get_state_dir()
    return [f.stem for f in state_dir.glob("*.json")]


def generate_session_id() -> str:
    """Generate unique session ID."""
    return f"workflow_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


# ============================================================================
# MAIN WORKFLOW CLASS
# ============================================================================

class CompleteWorkflowV2:
    """
    Resumable end-to-end workflow orchestrator.
    Tracks state after each step and can resume from failures.
    """

    def __init__(self, period: str = "Y", session_id: Optional[str] = None):
        """Initialize workflow.

        Args:
            period: Time period for MrT topics (D/W/M/Q/Y)
            session_id: Optional session ID to resume from
        """
        self.period = period

        # Load existing state or create new
        if session_id and state_exists(session_id):
            console.print(f"[green]📂 Resuming from existing session: {session_id}[/green]")
            self.state = load_state(session_id)
            console.print(f"[yellow]⏭️  Resuming from Phase {self.state.current_phase}[/yellow]")
        else:
            self.session_id = session_id or generate_session_id()
            console.print(f"[cyan]🆕 Creating new session: {self.session_id}[/cyan]")
            self.state = WorkflowState(
                session_id=self.session_id,
                period=period
            )
            save_state(self.state)

    async def run(self) -> Dict[str, Any]:
        """Run complete 5-phase workflow with resume capability.

        Returns:
            Dictionary with all workflow outputs and file paths
        """
        console.print("[bold]═" * 80 + "[/bold]")
        console.print(Panel(
            f"[bold purple]Complete Strategic Intelligence Workflow V2 (Resumable)[/bold purple]\n"
            f"Session: {self.state.session_id} | Period: {self.state.period}\n"
            f"Current Phase: {self.state.current_phase}",
            border_style="purple"
        ))
        console.print("[bold]═" * 80 + "[/bold]")

        try:
            # PHASE 0: MrT Topic Generation
            if self.state.current_phase <= 0:
                await self._phase_0_mrt_topics()

            # PHASE 1: Opponent CEO Attacks
            if self.state.current_phase <= 1:
                await self._phase_1_opponent_attacks()

            # PHASE 2: Mr Tường Defensive Response
            if self.state.current_phase <= 2:
                await self._phase_2_defensive_response()

            # PHASE 2.5: Brief Consolidation & Filtering
            if self.state.current_phase <= 2.5:
                await self._phase_2_5_brief_filtering()

            # PHASE 3: Deep Research Execution
            if self.state.current_phase <= 3:
                await self._phase_3_deep_research()

            # PHASE 4: MrT Report Ranking
            if self.state.current_phase <= 4:
                await self._phase_4_report_ranking()

            # Display final summary
            self._display_summary()

            return self._get_outputs()

        except Exception as e:
            console.print(f"\n[red]❌ Workflow failed at Phase {self.state.current_phase}: {e}[/red]")
            console.print(f"[yellow]💾 Progress saved to: {get_state_file(self.state.session_id)}[/yellow]")
            console.print(f"[yellow]⏭️  Resume with: CompleteWorkflowV2(session_id='{self.state.session_id}').run()[/yellow]")
            raise

    async def _phase_0_mrt_topics(self):
        """Phase 0: MrT Topic Generation."""
        console.print("\n[bold cyan]═" * 80 + "[/bold cyan]")
        console.print(Panel(
            "[bold purple]Phase 0: MrT Topic Generation[/bold purple]",
            border_style="purple"
        ))

        if self.state.mrt_topics_file:
            console.print(f"[green]✅ Phase 0 already completed: {self.state.mrt_topics_file}[/green]")
            return

        # Generate topics - returns List[str]
        topics_gen = TopicsGenerator(max_tool_call_iterations=4)
        mrt_topics = await topics_gen.generate(period=self.state.period)

        # Save to file (workflow is responsible for saving, not relying on agent internals)
        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        topics_file = output_dir / f"mrT_topics_{timestamp}.md"

        with open(topics_file, 'w', encoding='utf-8') as f:
            f.write(f"# MrT Research Topics - {self.state.period}\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"**Total Briefs:** {len(mrt_topics)}\n\n")
            f.write("---\n\n")
            for i, topic in enumerate(mrt_topics, 1):
                f.write(f"### {i}. Research Brief\n\n")
                f.write(f"{topic}\n\n")
                f.write("---\n\n")

        self.state.mrt_topics_file = str(topics_file)
        self.state.completed_steps.append("phase_0_topics_generated")
        self.state.current_phase = 1
        save_state(self.state)

        console.print(f"[green]✅ Phase 0 complete: {topics_file}[/green]")

    async def _phase_1_opponent_attacks(self):
        """Phase 1: Opponent CEO Attacks."""
        console.print("\n[bold cyan]═" * 80 + "[/bold cyan]")
        console.print(Panel(
            "[bold red]Phase 1: Opponent CEO Attacks[/bold red]",
            border_style="red"
        ))

        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)

        for ceo_type in ["zalopay", "vnpay"]:
            if ceo_type in self.state.opponent_attacks_files:
                console.print(f"[green]✅ {ceo_type.upper()} attacks already completed: {self.state.opponent_attacks_files[ceo_type]}[/green]")
                continue

            console.print(f"\n[yellow]Generating {ceo_type.upper()} CEO attacks...[/yellow]")
            agent = OpponentCEOTopicGenerator(ceo_type=ceo_type)
            attacks = await agent.generate(num_strategies=3)  # Returns List[str]

            # Save to file (workflow handles saving)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            attacks_file = output_dir / f"opponent_{ceo_type}_attacks_{timestamp}.md"

            with open(attacks_file, 'w', encoding='utf-8') as f:
                f.write(f"# Opponent {ceo_type.upper()} CEO Attack Strategies\n\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"**Total Strategies:** {len(attacks)}\n\n")
                f.write("---\n\n")
                for i, attack in enumerate(attacks, 1):
                    f.write(f"### {i}. Attack Strategy\n\n")
                    f.write(f"{attack}\n\n")
                    f.write("---\n\n")

            self.state.opponent_attacks_files[ceo_type] = str(attacks_file)
            self.state.completed_steps.append(f"phase_1_{ceo_type}_attacks_generated")
            save_state(self.state)

            console.print(f"[green]✅ {ceo_type.upper()} attacks: {attacks_file}[/green]")

        self.state.current_phase = 2
        save_state(self.state)

        console.print(f"[green]✅ Phase 1 complete: {len(self.state.opponent_attacks_files)} opponent attack files[/green]")

    async def _phase_2_defensive_response(self):
        """Phase 2: Mr Tường Defensive Response."""
        console.print("\n[bold cyan]═" * 80 + "[/bold cyan]")
        console.print(Panel(
            "[bold cyan]Phase 2: Mr Tường Defensive Response[/bold cyan]",
            border_style="cyan"
        ))

        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)

        for opponent, attacks_file in self.state.opponent_attacks_files.items():
            if opponent in self.state.defensive_briefs_files:
                console.print(f"[green]✅ Defensive response vs {opponent.upper()} already completed: {self.state.defensive_briefs_files[opponent]}[/green]")
                continue

            console.print(f"\n[yellow]Generating defensive response vs {opponent.upper()}...[/yellow]")

            # Read opponent attacks (need to parse back to List[str])
            with open(attacks_file, 'r', encoding='utf-8') as f:
                attacks_content = f.read()

            # Parse attacks from markdown file (extract content between ### markers)
            attack_strategies = []
            for section in attacks_content.split("###")[1:]:
                if section.strip():
                    attack_strategies.append(section.strip())

            # Generate defensive briefs - returns List[str]
            defensive_agent = MrTuongDefensiveAgent(max_tool_call_iterations=6)
            defensive_briefs = await defensive_agent.generate(
                opponent_name=opponent,
                attack_strategies=attack_strategies
            )

            # Save to file (workflow handles saving)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            defensive_file = output_dir / f"mrt_defensive_vs_{opponent}_{timestamp}.md"

            with open(defensive_file, 'w', encoding='utf-8') as f:
                f.write(f"# Mr Tường Defensive Briefs vs {opponent.upper()}\n\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                f.write(f"**Total Briefs:** {len(defensive_briefs)}\n\n")
                f.write("---\n\n")
                for i, brief in enumerate(defensive_briefs, 1):
                    f.write(f"### {i}. Defensive Brief\n\n")
                    f.write(f"{brief}\n\n")
                    f.write("---\n\n")

            self.state.defensive_briefs_files[opponent] = str(defensive_file)
            self.state.completed_steps.append(f"phase_2_defensive_vs_{opponent}_generated")
            save_state(self.state)

            console.print(f"[green]✅ Defensive briefs vs {opponent}: {defensive_file}[/green]")

        self.state.current_phase = 2.5
        save_state(self.state)

        console.print(f"[green]✅ Phase 2 complete: {len(self.state.defensive_briefs_files)} defensive brief files[/green]")

    async def _phase_2_5_brief_filtering(self):
        """Phase 2.5: Brief Consolidation & Filtering."""
        console.print("\n[bold cyan]═" * 80 + "[/bold cyan]")
        console.print(Panel(
            "[bold yellow]Phase 2.5: Brief Consolidation & Filtering[/bold yellow]",
            border_style="yellow"
        ))

        if self.state.filtered_briefs:
            console.print(f"[green]✅ Phase 2.5 already completed: {len(self.state.filtered_briefs)} filtered briefs[/green]")
            return

        # Gather all briefs
        all_briefs = []

        # Load MrT topics
        console.print(f"[cyan]Loading MrT topics from {self.state.mrt_topics_file}...[/cyan]")
        with open(self.state.mrt_topics_file, 'r', encoding='utf-8') as f:
            mrt_content = f.read()
            # Simple parsing - each brief separated by "###"
            for section in mrt_content.split("###")[1:]:  # Skip header
                if section.strip():
                    lines = section.strip().split("\n")
                    title = lines[0].strip() if lines else "Untitled"
                    content = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
                    all_briefs.append({"title": title, "content": content})

        console.print(f"[dim]Loaded {len(all_briefs)} MrT topic briefs[/dim]")

        # Load defensive briefs
        for opponent, defensive_file in self.state.defensive_briefs_files.items():
            console.print(f"[cyan]Loading defensive briefs vs {opponent} from {defensive_file}...[/cyan]")
            with open(defensive_file, 'r', encoding='utf-8') as f:
                defensive_content = f.read()
                for section in defensive_content.split("###")[1:]:
                    if section.strip():
                        lines = section.strip().split("\n")
                        title = lines[0].strip() if lines else "Untitled"
                        content = "\n".join(lines[1:]).strip() if len(lines) > 1 else ""
                        all_briefs.append({"title": title, "content": content})

        console.print(f"[cyan]Total briefs collected: {len(all_briefs)}[/cyan]")

        # Filter duplicates
        filter_agent = BriefFilterAgent()
        filtered_briefs = await filter_agent.filter_duplicates(all_briefs)

        self.state.filtered_briefs = filtered_briefs
        self.state.completed_steps.append("phase_2_5_briefs_filtered")
        self.state.current_phase = 3
        save_state(self.state)

        console.print(f"[green]✅ Phase 2.5 complete: Filtered {len(all_briefs)} → {len(filtered_briefs)} unique briefs[/green]")

    async def _phase_3_deep_research(self):
        """Phase 3: Deep Research Execution (with granular tracking)."""
        console.print("\n[bold cyan]═" * 80 + "[/bold cyan]")
        console.print(Panel(
            f"[bold green]Phase 3: Deep Research Execution ({len(self.state.filtered_briefs)} briefs)[/bold green]",
            border_style="green"
        ))

        # Initialize pending briefs if not already done
        if not self.state.pending_briefs and self.state.total_briefs == 0:
            self.state.total_briefs = len(self.state.filtered_briefs)
            self.state.pending_briefs = self.state.filtered_briefs.copy()
            self.state.current_brief_index = 0
            save_state(self.state)

        # Process pending briefs sequentially
        while self.state.pending_briefs:
            brief = self.state.pending_briefs[0]
            current_num = self.state.current_brief_index + 1

            console.print(f"\n[yellow]Researching brief {current_num}/{self.state.total_briefs}: {brief['title']}[/yellow]")

            try:
                # Create fresh DeepResearch instance for each brief
                deep_research = DeepResearch()

                # Run research (use brief content as research objective)
                report = await deep_research.run(brief["content"])

                # Save report
                safe_title = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in brief['title'][:50])
                timestamp = datetime.now().strftime("%Y%m%d_%H%M")
                report_file = Path("reports") / f"{safe_title}_{timestamp}.md"
                report_file.parent.mkdir(exist_ok=True)

                with open(report_file, 'w', encoding='utf-8') as f:
                    f.write(report)

                # Update state AFTER successful completion
                self.state.completed_reports.append(str(report_file))
                self.state.pending_briefs.pop(0)  # Remove completed brief
                self.state.current_brief_index += 1
                self.state.completed_steps.append(f"phase_3_report_{current_num}_completed")
                save_state(self.state)

                console.print(f"[green]✅ Report {current_num}/{self.state.total_briefs} saved: {report_file}[/green]")

            except Exception as e:
                console.print(f"[red]❌ Error researching brief {current_num}: {e}[/red]")
                console.print(f"[yellow]💾 Progress saved. {len(self.state.completed_reports)} reports completed.[/yellow]")
                console.print(f"[yellow]⏭️  Resume with session_id='{self.state.session_id}' to continue[/yellow]")
                raise

        self.state.current_phase = 4
        save_state(self.state)

        console.print(f"\n[green]✅ Phase 3 complete: {len(self.state.completed_reports)} reports generated[/green]")

    async def _phase_4_report_ranking(self):
        """Phase 4: MrT Report Ranking."""
        console.print("\n[bold cyan]═" * 80 + "[/bold cyan]")
        console.print(Panel(
            "[bold purple]Phase 4: MrT Report Ranking[/bold purple]",
            border_style="purple"
        ))

        if self.state.rankings_file:
            console.print(f"[green]✅ Phase 4 already completed: {self.state.rankings_file}[/green]")
            return

        if not self.state.completed_reports:
            console.print("[yellow]⚠️ No reports to rank - skipping Phase 4[/yellow]")
            self.state.current_phase = 5
            save_state(self.state)
            return

        # Rank reports
        ranking_agent = MrTRankingAgent(debug_log=False)
        rankings = await ranking_agent.rank_reports(self.state.completed_reports)

        # Rankings are auto-saved by the agent
        # Find the most recent rankings file
        rankings_files = sorted(Path(".output").glob("mrt_rankings_*.md"), reverse=True)
        if rankings_files:
            self.state.rankings_file = str(rankings_files[0])

        self.state.completed_steps.append("phase_4_rankings_completed")
        self.state.current_phase = 5  # Workflow complete
        save_state(self.state)

        console.print(f"[green]✅ Phase 4 complete: {len(rankings)} reports ranked[/green]")

    def _display_summary(self):
        """Display workflow completion summary."""
        console.print("\n[bold]═" * 80 + "[/bold]")
        console.print(Panel(
            "[bold green]✅ Complete Workflow Finished Successfully![/bold green]",
            border_style="green"
        ))

        # Create summary table
        table = Table(title="Workflow Summary", title_style="bold purple")
        table.add_column("Phase", style="cyan")
        table.add_column("Output", style="white")
        table.add_column("Count", style="yellow", justify="right")

        table.add_row("0. MrT Topics", self.state.mrt_topics_file or "N/A", "1 file")
        table.add_row("1. Opponent Attacks", ", ".join(self.state.opponent_attacks_files.keys()), f"{len(self.state.opponent_attacks_files)} files")
        table.add_row("2. Defensive Briefs", ", ".join(self.state.defensive_briefs_files.keys()), f"{len(self.state.defensive_briefs_files)} files")
        table.add_row("2.5 Filtered Briefs", "In-memory", f"{len(self.state.filtered_briefs)} briefs")
        table.add_row("3. Deep Research", "reports/", f"{len(self.state.completed_reports)} reports")
        table.add_row("4. Rankings", self.state.rankings_file or "N/A", "1 file" if self.state.rankings_file else "0 files")

        console.print("\n")
        console.print(table)
        console.print("\n[bold]═" * 80 + "[/bold]")

        console.print(f"\n[dim]Session ID: {self.state.session_id}[/dim]")
        console.print(f"[dim]State file: {get_state_file(self.state.session_id)}[/dim]")

    def _get_outputs(self) -> Dict[str, Any]:
        """Get workflow outputs as dictionary."""
        return {
            "session_id": self.state.session_id,
            "mrt_topics_file": self.state.mrt_topics_file,
            "opponent_attacks_files": self.state.opponent_attacks_files,
            "defensive_briefs_files": self.state.defensive_briefs_files,
            "filtered_briefs": self.state.filtered_briefs,
            "reports": self.state.completed_reports,
            "rankings_file": self.state.rankings_file
        }


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

async def resume_workflow(session_id: str) -> Dict[str, Any]:
    """Resume workflow from session ID.

    Args:
        session_id: Session ID to resume from

    Returns:
        Workflow outputs dictionary
    """
    workflow = CompleteWorkflowV2(session_id=session_id)
    return await workflow.run()


def show_sessions():
    """Display all available sessions."""
    sessions = list_sessions()

    if not sessions:
        console.print("[yellow]No saved sessions found[/yellow]")
        return

    console.print(f"\n[bold]Available Sessions ({len(sessions)})[/bold]\n")

    for session_id in sorted(sessions, reverse=True):
        state = load_state(session_id)
        console.print(f"[cyan]{session_id}[/cyan]")
        console.print(f"  Phase: {state.current_phase} | Period: {state.period}")
        console.print(f"  Reports: {len(state.completed_reports)}/{state.total_briefs}")
        console.print(f"  Updated: {state.updated_at}")
        console.print()


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

async def main():
    """Run complete workflow."""
    import sys

    # Check for resume command
    if len(sys.argv) > 1 and sys.argv[1] == "resume":
        if len(sys.argv) > 2:
            session_id = sys.argv[2]
            console.print(f"[cyan]Resuming session: {session_id}[/cyan]")
            outputs = await resume_workflow(session_id)
        else:
            console.print("[red]Usage: python -m src.agents.complete_workflow_v2 resume <session_id>[/red]")
            show_sessions()
            sys.exit(1)
    elif len(sys.argv) > 1 and sys.argv[1] == "list":
        show_sessions()
        sys.exit(0)
    else:
        # Parse command line argument for period
        period = sys.argv[1] if len(sys.argv) > 1 else "Y"

        if period not in ["D", "W", "M", "Q", "Y"]:
            console.print("[red]Invalid period. Use D (daily), W (weekly), M (monthly), Q (quarterly), or Y (yearly)[/red]")
            sys.exit(1)

        # Run workflow
        workflow = CompleteWorkflowV2(period=period)
        outputs = await workflow.run()

    console.print("\n[green]Workflow outputs available in the returned dictionary[/green]")


if __name__ == "__main__":
    asyncio.run(main())
