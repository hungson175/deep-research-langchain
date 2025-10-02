"""
Opponent CEO Topic Generator - ZaloPay & VNPay CEOs
Simulates competitor CEOs analyzing MoMo's weaknesses to generate strategic attack plans.
"""

import asyncio
from typing import List, Literal
from pydantic import BaseModel, Field
from pathlib import Path
from datetime import datetime

from .base_ceo_agent import BaseCEOAgent
from .supervisor import query_momo_data
from ..utils.helpers import get_today_str, tavily_search, think_tool, console
from ..prompts.persona_prompts import (
    ZALOPAY_CEO_PERSONA,
    VNPAY_CEO_PERSONA,
    get_competitor_ceo_prompt,
    COMPETITOR_USER_MESSAGE_TEMPLATE,
    COMPETITOR_EXTRACTION_PROMPT_TEMPLATE
)
from rich.panel import Panel


# ============================================================================
# CONFIGURATION
# ============================================================================

CEO_TYPE: Literal["zalopay", "vnpay"] = "zalopay"  # Change to "zalopay" or "vnpay"
NUM_STRATEGIES = 3  # Number of attack strategies to generate
MAX_ITERATIONS = 6  # Maximum research iterations


# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class AttackStrategies(BaseModel):
    """Schema for extracting attack strategies from CEO competitive analysis."""
    strategies: List[str] = Field(
        description="List of executive attack plans to exploit MoMo's weaknesses. Each plan is a comprehensive strategy including: identified weakness, exploitation approach, execution steps, expected impact, and success metrics.",
        min_items=1
    )


# ============================================================================
# MAIN CLASS
# ============================================================================

class OpponentCEOTopicGenerator(BaseCEOAgent):
    """AI agent simulating competitor CEOs (ZaloPay/VNPay) analyzing MoMo to generate attack strategies."""

    def __init__(self, ceo_type: Literal["zalopay", "vnpay"], max_tool_call_iterations: int = 6, debug_log: bool = False):
        """Initialize opponent CEO agent.

        Args:
            ceo_type: Which CEO to simulate ("zalopay" or "vnpay")
            max_tool_call_iterations: Max research iterations (default 6)
            debug_log: Enable debug logging (default False)
        """
        persona = ZALOPAY_CEO_PERSONA if ceo_type == "zalopay" else VNPAY_CEO_PERSONA

        console.print(Panel(
            f"[bold red]⚔️ Initializing Opponent CEO Agent: {persona['name']} ({persona['company']})[/bold red]",
            border_style="red"
        ))

        self.ceo_type = ceo_type

        super().__init__(
            persona=persona,
            max_tool_call_iterations=max_tool_call_iterations,
            tools=[think_tool, tavily_search, query_momo_data],
            structured_output_schema=AttackStrategies,
            debug_log=debug_log,
            agent_type=f"opp_{ceo_type}"
        )

        console.print(f"[dim]CEO: {persona['name']} ({persona['company']})[/dim]")

    def get_log_title(self) -> str:
        """Return title for debug log file."""
        return f"{self.persona['company']} Competitive Intelligence"

    def get_synthesis_message(self) -> str:
        """Return message to display during synthesis phase."""
        return f"{self.persona['name']} synthesizing competitive intelligence..."

    def _display_tool_call(self, tool_name: str, tool_call: dict):
        """Override to customize display for opponent CEO."""
        persona_name = self.persona.get('name', 'Agent')

        if tool_name == "think_tool":
            console.print(f"[magenta]💭 {persona_name} Thinking: {tool_call['args']['reflection'][:100]}...[/magenta]")
            self._log(f"THINK: {tool_call['args']['reflection']}")
        elif tool_name == "tavily_search":
            console.print(f"[blue]🔍 {persona_name} Searching: \"{tool_call['args']['query']}\"[/blue]")
            self._log(f"SEARCH QUERY: {tool_call['args']['query']}")
        elif tool_name == "query_momo_data":
            console.print(f"[red]🎯 {persona_name} Analyzing MoMo Data: \"{tool_call['args']['query'][:100]}...\"[/red]")
            self._log(f"MOMO DATA QUERY: {tool_call['args']['query']}", level="QUERY")

    def _log_tool_result(self, tool_name: str, result):
        """Override to customize result logging for opponent CEO."""
        if tool_name == "tavily_search":
            console.print(f"[dim green]✅ Market intelligence gathered[/dim green]")
            self._log(f"SEARCH RESULT (length: {len(str(result))} chars): {str(result)[:500]}...", level="RESULT")
        elif tool_name == "query_momo_data":
            console.print(f"[dim red]✅ MoMo weakness identified[/dim red]")
            self._log(f"MOMO DATA RESULT:\n{result}", level="MOMO_DATA")

    async def generate(self, num_strategies: int = NUM_STRATEGIES) -> List[str]:
        """Generate executive attack plans to exploit MoMo's weaknesses.

        Args:
            num_strategies: Number of attack strategies to generate (default: NUM_STRATEGIES)

        Returns:
            List of executive attack plans
        """
        return await self.generate_attack_strategies(num_strategies)

    async def generate_attack_strategies(self, num_strategies: int = NUM_STRATEGIES) -> List[str]:
        """Generate executive attack plans to exploit MoMo's weaknesses.

        Args:
            num_strategies: Number of attack strategies to generate

        Returns:
            List of executive attack plans
        """
        console.print(Panel(
            f"[bold red]⚔️ {self.persona['name']} Analyzing MoMo for Attack Strategies[/bold red]\n"
            f"Company: {self.persona['company']}\n"
            f"Target: Generate {num_strategies} executive exploitation plans",
            border_style="red"
        ))

        # Create system message with CEO persona
        system_prompt = get_competitor_ceo_prompt(self.ceo_type, num_strategies, get_today_str())

        # Initialize messages
        user_message = COMPETITOR_USER_MESSAGE_TEMPLATE.format(
            company=self.persona['company'],
            num_strategies=num_strategies
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        console.print(f"[dim]{self.persona['name']} starting competitive intelligence gathering...[/dim]")
        self._log(f"Starting competitive intelligence gathering for {num_strategies} executive exploitation plans")
        self._log(f"System prompt: {system_prompt[:200]}...")

        response = await self.model_with_tools.ainvoke(messages)
        messages.append({"role": "assistant", "content": response.content, "tool_calls": response.tool_calls or []})

        # Execute tool call loop
        messages, response = await self._execute_tool_call_loop(
            messages, response, iteration_label="Intelligence Gathering"
        )

        # Extract final strategies
        final_content = str(response.content)
        console.print(Panel(
            f"[bold red]⚔️ {self.persona['name']} Competitive Analysis Complete[/bold red]\n\n{final_content}",
            border_style="red"
        ))

        # Extract strategies using structured output
        self._log("Extracting executive exploitation plans...")
        strategies = await self._extract_strategies_from_response(final_content, num_strategies)
        self.generated_outputs = strategies
        self._log(f"Successfully extracted {len(strategies)} executive exploitation plans")

        # Save to file
        self._save_strategies_to_file(strategies)

        # Write debug log if enabled
        self._write_log_file()

        return strategies

    async def _extract_strategies_from_response(self, response_content: str, num_strategies: int) -> List[str]:
        """Extract executive exploitation plans from the model's response using structured output."""
        console.print("[yellow]📝 Extracting executive exploitation plans using structured output...[/yellow]")

        extraction_prompt = COMPETITOR_EXTRACTION_PROMPT_TEMPLATE.format(
            ceo_name=self.persona['name'],
            company=self.persona['company'],
            num_strategies=num_strategies,
            response_content=response_content
        )

        try:
            # Use structured output to extract strategies
            structured_response = await self.structured_output_model.ainvoke([
                {"role": "system", "content": f"You are an expert at extracting strategic attack strategies for {self.persona['company']}."},
                {"role": "user", "content": extraction_prompt}
            ])

            extracted_strategies = structured_response.strategies
            console.print(f"[green]✅ Extracted {len(extracted_strategies)} executive exploitation plans using structured output[/green]")

            # Ensure we have the right number of strategies
            if len(extracted_strategies) > num_strategies:
                extracted_strategies = extracted_strategies[:num_strategies]
            elif len(extracted_strategies) < num_strategies:
                console.print(f"[yellow]⚠️ Only extracted {len(extracted_strategies)} plans, expected {num_strategies}[/yellow]")

            return extracted_strategies

        except Exception as e:
            console.print(f"[red]❌ Error in structured extraction: {e}[/red]")
            console.print("[yellow]Falling back to simple text parsing...[/yellow]")

            # Fallback to simple extraction
            prefixes = ['1.', '2.', '3.', '4.', '5.', '##', 'Strategy', 'Plan']
            return self._simple_extract_items(response_content, prefixes)

    def _save_strategies_to_file(self, strategies: List[str]) -> str:
        """Save generated executive exploitation plans to a markdown file.

        Args:
            strategies: List of executive exploitation plans

        Returns:
            Path to the saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"opponent_{self.ceo_type}_attacks_{timestamp}.md"

        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)
        file_path = output_dir / filename

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# Executive Exploitation Plans - {self.persona['company']} vs MoMo\n\n")
            f.write(f"**CEO:** {self.persona['name']}\n")
            f.write(f"**Company:** {self.persona['company']}\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"**Total Plans:** {len(strategies)}\n\n")
            f.write("---\n\n")
            f.write(f"## Strategic Mission\n\n")
            f.write(f"These executive exploitation plans outline how {self.persona['company']} can exploit MoMo's weaknesses to win market share based on competitive intelligence analysis.\n\n")
            f.write("---\n\n")

            for i, strategy in enumerate(strategies, 1):
                f.write(f"## Exploitation Plan {i}\n\n")
                f.write(f"{strategy}\n\n")
                f.write("---\n\n")

        console.print(f"[green]📁 Executive exploitation plans saved to: {file_path}[/green]")
        return str(file_path)


# ============================================================================
# DEMO/TEST FUNCTION
# ============================================================================

async def main():
    """Demo function to test opponent CEO agent."""
    persona = ZALOPAY_CEO_PERSONA if CEO_TYPE == "zalopay" else VNPAY_CEO_PERSONA

    console.print("[bold]═" * 80 + "[/bold]")
    console.print(Panel(
        f"[bold red]Opponent CEO - Executive Exploitation Plans Generator[/bold red]\n"
        f"CEO: {persona['name']} ({persona['company']})\n"
        f"Plans: {NUM_STRATEGIES} | Iterations: {MAX_ITERATIONS}",
        border_style="red"
    ))
    console.print("[bold]═" * 80 + "[/bold]")

    console.print(f"\n[bold cyan]Initializing {persona['name']} ({persona['company']}) Agent[/bold cyan]\n")
    agent = OpponentCEOTopicGenerator(ceo_type=CEO_TYPE, max_tool_call_iterations=MAX_ITERATIONS, debug_log=True)
    strategies = await agent.generate_attack_strategies(num_strategies=NUM_STRATEGIES)

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print(Panel(
        f"[bold green]✅ {persona['name']} Generated {len(strategies)} Executive Exploitation Plans[/bold green]",
        border_style="green"
    ))

    for i, strategy in enumerate(strategies, 1):
        console.print(f"\n[cyan]Exploitation Plan {i}:[/cyan]")
        console.print(f"{strategy[:300]}...\n")

    console.print("\n[dim]These exploitation plans will be fed to Mr Tường agent to generate[/dim]")
    console.print(f"[dim]defensive research briefs based on his concerns.[/dim]")
    console.print("[bold]═" * 80 + "[/bold]")


if __name__ == "__main__":
    asyncio.run(main())
