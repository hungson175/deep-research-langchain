"""
Opponent CEO Topic Generator - ZaloPay & VNPay CEOs
Simulates competitor CEOs analyzing MoMo's weaknesses to generate strategic attack plans.
"""

import asyncio
from dotenv import load_dotenv
load_dotenv()

from .utils import get_today_str, tavily_search, think_tool, console, init_xai_model
from .supervisor import query_momo_data  # Import from supervisor instead of duplicating
from .persona_prompts import (
    ZALOPAY_CEO_PERSONA,
    VNPAY_CEO_PERSONA,
    get_competitor_ceo_prompt,
    COMPETITOR_USER_MESSAGE_TEMPLATE,
    COMPETITOR_EXTRACTION_PROMPT_TEMPLATE
)
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from .config import BOSS_MODEL, BOSS_TEMPERATURE
from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime
from pathlib import Path

# ============================================================================
# CONFIGURATION - Change this to switch between CEO agents
# ============================================================================

CEO_TYPE: Literal["zalopay", "vnpay"] = "zalopay"  # Change to "zalopay" or "vnpay"
NUM_BRIEFS = 3  # Number of competitive research briefs to generate
MAX_ITERATIONS = 6  # Maximum research iterations

# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class CompetitiveResearchBriefs(BaseModel):
    """Schema for extracting competitive research briefs from CEO analysis."""
    briefs: List[str] = Field(
        description="List of complete strategic research briefs outlining how to compete with or surpass MoMo. Each brief includes: research objective, background context, investigation areas, expected insights, and success metrics.",
        min_items=1
    )

# ============================================================================
# MAIN CLASS
# ============================================================================

class OpponentCEOTopicGenerator:
    """AI agent simulating competitor CEOs (ZaloPay/VNPay) analyzing MoMo to generate attack strategies."""

    def __init__(self, ceo_type: Literal["zalopay", "vnpay"], max_tool_call_iterations: int = 6, debug_log: bool = False):
        """Initialize opponent CEO agent.

        Args:
            ceo_type: Which CEO to simulate ("zalopay" or "vnpay")
            max_tool_call_iterations: Max research iterations (default 6 for thorough analysis)
            debug_log: Enable debug logging of intermediate results (default False)
        """
        persona = ZALOPAY_CEO_PERSONA if ceo_type == "zalopay" else VNPAY_CEO_PERSONA
        console.print(Panel(
            f"[bold red]⚔️ Initializing Opponent CEO Agent: {persona['name']} ({persona['company']})[/bold red]",
            border_style="red"
        ))

        self.ceo_type = ceo_type
        self.persona = persona
        self.debug_log = debug_log
        self.log_entries = []  # Store log entries for writing later

        # Initialize log file path if debug logging is enabled
        if self.debug_log:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            log_dir = Path(".output/logs")
            log_dir.mkdir(parents=True, exist_ok=True)
            self.log_file_path = log_dir / f"opp_{ceo_type}_briefs_{timestamp}.md"
            console.print(f"[dim yellow]Debug logging enabled: {self.log_file_path}[/dim yellow]")

        self.model = init_xai_model(
            model=BOSS_MODEL,
            temperature=BOSS_TEMPERATURE,
            max_tokens=12000
        )

        # Include MirMir tool for internal MoMo data analysis
        self.tools = [think_tool, tavily_search, query_momo_data]
        self.model_with_tools = self.model.bind_tools(self.tools)
        self.max_tool_call_iterations = max_tool_call_iterations

        # Initialize structured output model for brief extraction
        self.structured_output_model = self.model.with_structured_output(CompetitiveResearchBriefs)

        console.print(f"[dim]CEO: {persona['name']} ({persona['company']})[/dim]")
        console.print(f"[dim]Using model: {BOSS_MODEL}[/dim]")
        console.print(f"[dim]Max iterations: {max_tool_call_iterations}[/dim]")

        self.tools_by_name = {tool.name: tool for tool in self.tools}
        self.generated_briefs = []

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
                f.write(f"# Debug Log - {self.persona['company']} Competitive Intelligence\n\n")
                f.write(f"**CEO:** {self.persona['name']}\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("---\n\n")
                f.write("## Log Entries\n\n")
                for entry in self.log_entries:
                    f.write(f"{entry}\n\n")
            console.print(f"[green]📝 Debug log written to: {self.log_file_path}[/green]")

    async def generate_competitive_briefs(self, num_briefs: int = 3) -> List[str]:
        """Generate strategic research briefs for competing with MoMo.

        Args:
            num_briefs: Number of research briefs to generate (default: 3)

        Returns:
            List of complete research briefs for competing with MoMo
        """
        console.print(Panel(
            f"[bold red]⚔️ {self.persona['name']} Analyzing MoMo for Competitive Advantages[/bold red]\n"
            f"Company: {self.persona['company']}\n"
            f"Target: Generate {num_briefs} strategic attack plans",
            border_style="red"
        ))

        # Create system message with CEO persona
        system_prompt = get_competitor_ceo_prompt(self.ceo_type, num_briefs, get_today_str())

        # Initialize messages
        user_message = COMPETITOR_USER_MESSAGE_TEMPLATE.format(
            company=self.persona['company'],
            num_briefs=num_briefs
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        console.print(f"[dim]{self.persona['name']} starting competitive intelligence gathering...[/dim]")
        self._log(f"Starting competitive intelligence gathering for {num_briefs} briefs")
        self._log(f"System prompt: {system_prompt[:200]}...")

        response = await self.model_with_tools.ainvoke(messages)
        messages.append({"role": "assistant", "content": response.content, "tool_calls": response.tool_calls or []})

        tool_call_iterations = 0

        while response.tool_calls and tool_call_iterations < self.max_tool_call_iterations:
            tool_call_iterations += 1
            console.print(f"\n[cyan]🔄 Intelligence Gathering Iteration {tool_call_iterations}/{self.max_tool_call_iterations}[/cyan]")
            self._log(f"=== ITERATION {tool_call_iterations}/{self.max_tool_call_iterations} ===")

            observations = []
            for tool_call in response.tool_calls:
                tool = self.tools_by_name[tool_call["name"]]
                tool_name = tool_call["name"]

                if tool_name == "think_tool":
                    console.print(f"[magenta]💭 {self.persona['name']} Thinking: {tool_call['args']['reflection'][:100]}...[/magenta]")
                    self._log(f"THINK: {tool_call['args']['reflection']}")
                elif tool_name == "tavily_search":
                    console.print(f"[blue]🔍 {self.persona['name']} Searching: \"{tool_call['args']['query']}\"[/blue]")
                    self._log(f"SEARCH QUERY: {tool_call['args']['query']}")
                elif tool_name == "query_momo_data":
                    console.print(f"[red]🎯 {self.persona['name']} Analyzing MoMo Data: \"{tool_call['args']['query'][:100]}...\"[/red]")
                    self._log(f"MOMO DATA QUERY: {tool_call['args']['query']}", level="QUERY")

                with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                    transient=True,
                ) as progress:
                    task = progress.add_task(f"[cyan]Executing {tool_name}...", total=None)
                    result = await tool.ainvoke(tool_call["args"])
                    progress.update(task, completed=True)
                    observations.append(result)

                # Log tool results
                if tool_name == "tavily_search":
                    console.print(f"[dim green]✅ Market intelligence gathered[/dim green]")
                    self._log(f"SEARCH RESULT (length: {len(str(result))} chars): {str(result)[:500]}...", level="RESULT")
                elif tool_name == "query_momo_data":
                    console.print(f"[dim red]✅ MoMo weakness identified[/dim red]")
                    self._log(f"MOMO DATA RESULT:\n{result}", level="MOMO_DATA")

            # Add tool results to messages
            for observation, tool_call in zip(observations, response.tool_calls):
                messages.append({
                    "role": "tool",
                    "content": str(observation),
                    "tool_call_id": tool_call["id"]
                })

            console.print(f"[dim]{self.persona['name']} synthesizing competitive intelligence...[/dim]")
            self._log("Synthesizing competitive intelligence...")
            response = await self.model_with_tools.ainvoke(messages)
            messages.append({"role": "assistant", "content": response.content, "tool_calls": response.tool_calls or []})
            self._log(f"Model response (length: {len(str(response.content))} chars): {str(response.content)[:500]}...")

        # Extract final briefs using structured output
        final_content = str(response.content)
        console.print(Panel(
            f"[bold red]⚔️ {self.persona['name']} Competitive Analysis Complete[/bold red]\n\n{final_content}",
            border_style="red"
        ))

        # Extract briefs using structured output
        self._log("Extracting competitive research briefs...")
        briefs = await self._extract_briefs_from_response(final_content, num_briefs)
        self.generated_briefs = briefs
        self._log(f"Successfully extracted {len(briefs)} briefs")

        # Save to file
        self._save_briefs_to_file(briefs)

        # Write debug log if enabled
        self._write_log_file()

        return briefs

    async def _extract_briefs_from_response(self, response_content: str, num_briefs: int) -> List[str]:
        """Extract strategic research briefs from the model's response using structured output."""
        console.print("[yellow]📝 Extracting competitive research briefs using structured output...[/yellow]")

        extraction_prompt = COMPETITOR_EXTRACTION_PROMPT_TEMPLATE.format(
            ceo_name=self.persona['name'],
            company=self.persona['company'],
            num_briefs=num_briefs,
            response_content=response_content
        )

        try:
            # Use structured output to extract briefs
            structured_response = await self.structured_output_model.ainvoke([
                {"role": "system", "content": f"You are an expert at extracting strategic competitive research briefs for {self.persona['company']}."},
                {"role": "user", "content": extraction_prompt}
            ])

            extracted_briefs = structured_response.briefs
            console.print(f"[green]✅ Extracted {len(extracted_briefs)} competitive research briefs using structured output[/green]")

            # Ensure we have the right number of briefs
            if len(extracted_briefs) > num_briefs:
                extracted_briefs = extracted_briefs[:num_briefs]
            elif len(extracted_briefs) < num_briefs:
                console.print(f"[yellow]⚠️ Only extracted {len(extracted_briefs)} briefs, expected {num_briefs}[/yellow]")

            return extracted_briefs

        except Exception as e:
            console.print(f"[red]❌ Error in structured extraction: {e}[/red]")
            console.print("[yellow]Falling back to simple text parsing...[/yellow]")

            # Fallback to simple extraction
            return self._simple_extract_briefs(response_content)

    def _simple_extract_briefs(self, response_content: str) -> List[str]:
        """Simple fallback method to extract briefs from text."""
        lines = response_content.split('\n')
        briefs = []
        current_brief = []

        for line in lines:
            line_stripped = line.strip()
            # Look for brief boundaries
            if line_stripped and any(line_stripped.startswith(prefix) for prefix in ['1.', '2.', '3.', '4.', '5.', '##', 'Brief']):
                if current_brief:
                    briefs.append('\n'.join(current_brief))
                    current_brief = []
                current_brief.append(line)
            elif current_brief:
                current_brief.append(line)

        # Add last brief
        if current_brief:
            briefs.append('\n'.join(current_brief))

        return briefs if briefs else [response_content]

    def _save_briefs_to_file(self, briefs: List[str]) -> str:
        """Save generated research briefs to a markdown file.

        Args:
            briefs: List of research briefs

        Returns:
            Path to the saved file
        """
        # Create timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        # Create filename
        filename = f"opponent_{self.ceo_type}_briefs_{timestamp}.md"

        # Ensure .output directory exists
        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)

        # Full path
        file_path = output_dir / filename

        # Save the briefs
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# Competitive Research Briefs - {self.persona['company']}\n\n")
            f.write(f"**CEO:** {self.persona['name']}\n")
            f.write(f"**Company:** {self.persona['company']}\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"**Total Briefs:** {len(briefs)}\n\n")
            f.write("---\n\n")
            f.write(f"## Strategic Mission\n\n")
            f.write(f"These research briefs outline strategic opportunities for {self.persona['company']} to compete with or surpass MoMo based on competitive intelligence analysis.\n\n")
            f.write("---\n\n")

            for i, brief in enumerate(briefs, 1):
                f.write(f"## Competitive Research Brief {i}\n\n")
                f.write(f"{brief}\n\n")
                f.write("---\n\n")

        console.print(f"[green]📁 Competitive research briefs saved to: {file_path}[/green]")
        return str(file_path)


# ============================================================================
# DEMO/TEST FUNCTION
# ============================================================================

async def main():
    """Demo function to test opponent CEO agent.

    Configuration is controlled by constants at the top of this file:
    - CEO_TYPE: "zalopay" or "vnpay"
    - NUM_BRIEFS: Number of research briefs to generate
    - MAX_ITERATIONS: Maximum research iterations
    """
    # Get CEO name for display
    persona = ZALOPAY_CEO_PERSONA if CEO_TYPE == "zalopay" else VNPAY_CEO_PERSONA

    console.print("[bold]═" * 80 + "[/bold]")
    console.print(Panel(
        f"[bold red]Opponent CEO Topic Generator - {persona['company']}[/bold red]\n"
        f"CEO: {persona['name']}\n"
        f"Briefs: {NUM_BRIEFS} | Iterations: {MAX_ITERATIONS}",
        border_style="red"
    ))
    console.print("[bold]═" * 80 + "[/bold]")

    # Initialize agent with configured CEO type (with debug logging enabled)
    console.print(f"\n[bold cyan]Initializing {persona['name']} ({persona['company']}) Agent[/bold cyan]\n")
    agent = OpponentCEOTopicGenerator(ceo_type=CEO_TYPE, max_tool_call_iterations=MAX_ITERATIONS, debug_log=True)
    briefs = await agent.generate_competitive_briefs(num_briefs=NUM_BRIEFS)

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print(Panel(
        f"[bold green]✅ {persona['name']} Generated {len(briefs)} Competitive Research Briefs[/bold green]",
        border_style="green"
    ))

    for i, brief in enumerate(briefs, 1):
        console.print(f"\n[cyan]Brief {i}:[/cyan]")
        console.print(f"{brief[:300]}...\n")

    console.print("\n[dim]These briefs can now be fed to the deep-research system to generate[/dim]")
    console.print(f"[dim]comprehensive competitive strategy reports for {persona['company']}.[/dim]")
    console.print("[bold]═" * 80 + "[/bold]")


if __name__ == "__main__":
    asyncio.run(main())
