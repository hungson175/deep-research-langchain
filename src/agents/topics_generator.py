import asyncio
from dotenv import load_dotenv
load_dotenv()

from ..utils.helpers import get_today_str, tavily_search, think_tool, console, init_xai_model
from ..prompts.persona_prompts import MRT_TOPICS_GENERATOR_PROMPT
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from ..utils.config import BOSS_MODEL, BOSS_TEMPERATURE
from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime
from pathlib import Path

# ============================================================================
# PROMPTS (User/Extraction Messages - MrT prompt moved to persona_prompts.py)
# ============================================================================

# User message template for MrT analysis request
USER_MESSAGE_TEMPLATE = """Please conduct a {period_name} analysis of current market trends, fintech developments, regulatory changes, and competitive landscape. Based on your research, create {num_concerns} complete research briefs that can be directly used by research teams for deep investigation. Each brief should be comprehensive and ready to use."""

# Extraction prompt for structured output
EXTRACTION_PROMPT_TEMPLATE = """Based on the following MrT market analysis, extract exactly {num_concerns} complete research briefs that are ready for deep research investigation.

Market Analysis Content:
{response_content}

Extract the {num_concerns} most critical research briefs from this analysis. Each brief should be COMPLETE and include:
- Clear research objective/question
- Background context explaining why this matters to MoMo
- Specific areas to investigate
- Expected insights or outcomes
- Focus on MoMo's competitive position and future opportunities/threats
- Be actionable for research teams to investigate immediately
- Follow MoMo's strategic framework (financial inclusion, innovation, business growth, regulatory compliance)

Return exactly {num_concerns} complete research briefs ready for the deep research system."""

# System message for extraction agent
EXTRACTION_SYSTEM_MESSAGE = """You are an expert at extracting complete research briefs from market analysis content. Each brief must be comprehensive and ready for immediate use."""

# ============================================================================
# PYDANTIC MODELS
# ============================================================================

class StrategicConcerns(BaseModel):
    """Schema for structured research brief extraction from MrT's analysis."""
    concerns: List[str] = Field(
        description="List of complete research briefs ready for deep research system. Each brief includes research objective, background context, specific areas to investigate, and expected insights.",
        min_items=1
    )

# ============================================================================
# MAIN CLASS
# ============================================================================ 

class TopicsGenerator:
    """AI agent that acts as MrT, searches current news/trends, and generates strategic concerns for research."""

    def __init__(self, max_tool_call_iterations: int = 5):
        console.print(Panel("[bold green]📰 Initializing MrT Topics Generator[/bold green]", border_style="green"))

        self.model = init_xai_model(
            model=BOSS_MODEL,
            temperature=BOSS_TEMPERATURE,
            max_tokens=12000
        )
        self.tools = [think_tool, tavily_search]
        self.model_with_tools = self.model.bind_tools(self.tools)
        self.max_tool_call_iterations = max_tool_call_iterations

        # Initialize separate structured output model for concern extraction
        self.structured_output_model = self.model.with_structured_output(StrategicConcerns)

        console.print(f"[dim]Using model: {BOSS_MODEL}[/dim]")
        console.print(f"[dim]Max iterations: {max_tool_call_iterations}[/dim]")

        self.tools_by_name = {tool.name: tool for tool in self.tools}
        self.generated_concerns = []

    def _get_concern_count(self, period: Literal["D", "W", "M", "Q", "Y"]) -> int:
        """Get number of concerns based on period."""
        period_mapping = {
            "D": 1,  # Daily: 1 concern
            "W": 1,  # Weekly: 1 concern
            "M": 3,  # Monthly: 3 concerns
            "Q": 3,  # Quarterly: 3 concerns
            "Y": 5,  # Yearly: 5 concerns 
        }
        return period_mapping.get(period, 5)

    def _get_period_name(self, period: Literal["D", "W", "M", "Q", "Y"]) -> str:
        """Get human-readable period name."""
        period_mapping = {
            "D": "daily",
            "W": "weekly",
            "M": "monthly",
            "Q": "quarterly",
            "Y": "yearly"
        }
        return period_mapping.get(period, "daily")

    async def generate_topics(self, period: Literal["D", "W", "M", "Q", "Y"]) -> List[str]:
        """Generate strategic research briefs based on current market trends.

        Args:
            period: Time period - 'D' (daily, 1 brief), 'W' (weekly, 1 brief), 'M' (monthly, 3 briefs), 'Q' (quarterly, 3 briefs), 'Y' (yearly, 5 briefs)

        Returns:
            List of complete research briefs that can be directly used by the deep research system
        """
        num_concerns = self._get_concern_count(period)
        period_name = self._get_period_name(period)

        console.print(Panel(
            f"[bold green]📰 Generating {num_concerns} Strategic Concerns ({period_name.title()} Analysis)[/bold green]",
            border_style="green"
        ))

        # Create system message with MrT persona
        system_prompt = MRT_TOPICS_GENERATOR_PROMPT.format(
            period_type=period_name,
            num_concerns=num_concerns,
            date=get_today_str()
        )

        # Initialize messages
        user_message = USER_MESSAGE_TEMPLATE.format(
            period_name=period_name,
            num_concerns=num_concerns
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]

        console.print(f"[dim]MrT conducting {period_name} market analysis...[/dim]")
        response = await self.model_with_tools.ainvoke(messages)
        messages.append({"role": "assistant", "content": response.content, "tool_calls": response.tool_calls or []})

        tool_call_iterations = 0

        while response.tool_calls and tool_call_iterations < self.max_tool_call_iterations:
            tool_call_iterations += 1
            console.print(f"\n[cyan]🔄 Research Iteration {tool_call_iterations}/{self.max_tool_call_iterations}[/cyan]")

            observations = []
            for tool_call in response.tool_calls:
                tool = self.tools_by_name[tool_call["name"]]
                tool_name = tool_call["name"]

                if tool_name == "think_tool":
                    console.print(f"[magenta]💭 MrT Analyzing: {tool_call['args']['reflection'][:100]}...[/magenta]")
                elif tool_name == "tavily_search":
                    console.print(f"[blue]🔍 MrT Searching: \"{tool_call['args']['query']}\"[/blue]")

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

                if tool_name == "tavily_search":
                    console.print(f"[dim green]✅ Found market intelligence[/dim green]")

            # Add tool results to messages
            for observation, tool_call in zip(observations, response.tool_calls):
                messages.append({
                    "role": "tool",
                    "content": str(observation),
                    "tool_call_id": tool_call["id"]
                })

            console.print("[dim]MrT analyzing market intelligence and identifying concerns...[/dim]")
            response = await self.model_with_tools.ainvoke(messages)
            messages.append({"role": "assistant", "content": response.content, "tool_calls": response.tool_calls or []})

        # Extract final concerns using structured output
        final_content = str(response.content)
        console.print(Panel(
            f"[bold green]✨ MrT {period_name.title()} Analysis Complete[/bold green]\n\n{final_content}",
            border_style="green"
        ))

        # Extract concerns using structured output
        concerns = await self._extract_concerns_from_response(final_content, num_concerns)
        self.generated_concerns = concerns

        # Save to file
        self._save_topics_to_file(concerns, period)

        return concerns

    async def _extract_concerns_from_response(self, response_content: str, num_concerns: int) -> List[str]:
        """Extract strategic research briefs from the model's response using structured output."""
        console.print("[yellow]📝 Extracting research briefs using structured output...[/yellow]")

        extraction_prompt = EXTRACTION_PROMPT_TEMPLATE.format(
            num_concerns=num_concerns,
            response_content=response_content
        )

        try:
            # Use structured output to extract concerns
            structured_response = await self.structured_output_model.ainvoke([
                {"role": "system", "content": EXTRACTION_SYSTEM_MESSAGE},
                {"role": "user", "content": extraction_prompt}
            ])

            extracted_concerns = structured_response.concerns
            console.print(f"[green]✅ Extracted {len(extracted_concerns)} research briefs using structured output[/green]")

            # Ensure we have the right number of concerns
            if len(extracted_concerns) > num_concerns:
                extracted_concerns = extracted_concerns[:num_concerns]
            elif len(extracted_concerns) < num_concerns:
                console.print(f"[yellow]⚠️ Only extracted {len(extracted_concerns)} briefs, expected {num_concerns}[/yellow]")

            return extracted_concerns

        except Exception as e:
            console.print(f"[red]❌ Error in structured extraction: {e}[/red]")
            console.print("[yellow]Falling back to simple text parsing...[/yellow]")

            # Fallback to simple extraction
            return self._simple_extract_concerns(response_content)

    def _simple_extract_concerns(self, response_content: str) -> List[str]:
        """Simple fallback method to extract concerns from text."""
        lines = response_content.split('\n')
        concerns = []

        for line in lines:
            line = line.strip()
            # Look for lines that are concerns or numbered/bulleted items
            if line and any(line.startswith(prefix) for prefix in ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '•', '-', 'Concern:']):
                # Clean up numbering and bullet points
                cleaned = line
                for prefix in ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '•', '-', 'Concern:']:
                    if cleaned.startswith(prefix):
                        cleaned = cleaned[len(prefix):].strip()
                        break
                if cleaned and len(cleaned) > 20:  # Ensure it's a substantial concern
                    concerns.append(cleaned)

        return concerns

    def _save_topics_to_file(self, concerns: List[str], period: str) -> str:
        """Save generated research briefs to a markdown file.

        Args:
            concerns: List of research briefs
            period: Time period (D/W/M/Q/Y)

        Returns:
            Path to the saved file
        """
        # Create timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")

        # Create filename
        filename = f"mrT_topics_{timestamp}.md"

        # Ensure .output directory exists
        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)

        # Full path
        file_path = output_dir / filename

        # Save the briefs
        period_name = self._get_period_name(period)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# MrT Research Topics - {period_name.title()} Analysis\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"**Period:** {period_name.title()} ({period})\n")
            f.write(f"**Total Briefs:** {len(concerns)}\n\n")
            f.write("---\n\n")

            for i, concern in enumerate(concerns, 1):
                f.write(f"## Research Brief {i}\n\n")
                f.write(f"{concern}\n\n")
                f.write("---\n\n")

        console.print(f"[green]📁 Research briefs saved to: {file_path}[/green]")
        return str(file_path)


# Demo/Test function
async def main():
    console.print("[bold]═" * 80 + "[/bold]")
    console.print(Panel("[bold green]MrT Topics Generator - Demo Mode[/bold green]", border_style="green"))
    console.print("[bold]═" * 80 + "[/bold]")

    # Test the topics generator with different periods
    generator = TopicsGenerator(max_tool_call_iterations=4)

    # Test Yearly analysis (5 concerns)
    test_period = "Y"
    concerns = await generator.generate_topics(test_period)

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print(Panel(f"[bold cyan]📰 Generated {len(concerns)} Strategic Concerns ({test_period} - Weekly)[/bold cyan]", border_style="cyan"))

    for i, concern in enumerate(concerns, 1):
        console.print(f"[cyan]{i}.[/cyan] {concern}")

    console.print("\n[dim]These concerns can now be fed to QuestionGenerator to create research questions,[/dim]")
    console.print("[dim]which in turn can be used with the deep-research system.[/dim]")
    console.print("[bold]═" * 80 + "[/bold]")

if __name__ == "__main__":
    asyncio.run(main())