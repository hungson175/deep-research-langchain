"""
Base CEO Agent - Abstract base class for all CEO persona agents.
Provides common functionality for research, logging, and output generation.
"""

import asyncio
from abc import ABC, abstractmethod
from typing import List, Optional, Any
from datetime import datetime
from pathlib import Path
from pydantic import BaseModel

from ..utils.helpers import get_today_str, tavily_search, think_tool, console, init_xai_model
from ..utils.config import BOSS_MODEL, BOSS_TEMPERATURE
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn


class BaseCEOAgent(ABC):
    """Abstract base class for CEO persona agents with common functionality."""

    def __init__(
        self,
        persona: dict,
        max_tool_call_iterations: int,
        tools: List[Any],
        structured_output_schema: type[BaseModel],
        debug_log: bool = False,
        agent_type: str = "ceo"
    ):
        """Initialize base CEO agent.

        Args:
            persona: Dict containing CEO persona details (name, title, company, etc.)
            max_tool_call_iterations: Max research iterations
            tools: List of tools available to the agent
            structured_output_schema: Pydantic schema for structured output extraction
            debug_log: Enable debug logging (default False)
            agent_type: Agent type identifier for logging (default "ceo")
        """
        self.persona = persona
        self.max_tool_call_iterations = max_tool_call_iterations
        self.debug_log = debug_log
        self.agent_type = agent_type
        self.log_entries = []
        self.generated_outputs = []

        # Initialize log file path if debug logging is enabled
        if self.debug_log:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            log_dir = Path(".output/logs")
            log_dir.mkdir(parents=True, exist_ok=True)
            self.log_file_path = log_dir / f"{agent_type}_{timestamp}.md"
            console.print(f"[dim yellow]Debug logging enabled: {self.log_file_path}[/dim yellow]")

        # Initialize model
        self.model = init_xai_model(
            model=BOSS_MODEL,
            temperature=BOSS_TEMPERATURE,
            max_tokens=12000
        )

        # Setup tools
        self.tools = tools
        self.model_with_tools = self.model.bind_tools(self.tools)
        self.tools_by_name = {tool.name: tool for tool in self.tools}

        # Initialize structured output model
        self.structured_output_model = self.model.with_structured_output(structured_output_schema)

        console.print(f"[dim]Using model: {BOSS_MODEL}[/dim]")
        console.print(f"[dim]Max iterations: {max_tool_call_iterations}[/dim]")

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
                f.write(f"# Debug Log - {self.get_log_title()}\n\n")
                f.write(f"**Agent Type:** {self.agent_type}\n")
                f.write(f"**CEO:** {self.persona.get('name', 'N/A')}\n")
                f.write(f"**Company:** {self.persona.get('company', 'N/A')}\n")
                f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write("---\n\n")
                f.write("## Log Entries\n\n")
                for entry in self.log_entries:
                    f.write(f"{entry}\n\n")
            console.print(f"[green]📝 Debug log written to: {self.log_file_path}[/green]")

    async def _execute_tool_call_loop(
        self,
        messages: List[dict],
        response: Any,
        iteration_label: str = "Research"
    ) -> tuple[List[dict], Any]:
        """Execute tool call loop until max iterations or no more tool calls.

        Args:
            messages: Message history
            response: Initial model response
            iteration_label: Label for iteration display (default "Research")

        Returns:
            Tuple of (updated messages, final response)
        """
        tool_call_iterations = 0

        while response.tool_calls and tool_call_iterations < self.max_tool_call_iterations:
            tool_call_iterations += 1
            console.print(f"\n[cyan]🔄 {iteration_label} Iteration {tool_call_iterations}/{self.max_tool_call_iterations}[/cyan]")
            self._log(f"=== ITERATION {tool_call_iterations}/{self.max_tool_call_iterations} ===")

            observations = []
            for tool_call in response.tool_calls:
                tool = self.tools_by_name[tool_call["name"]]
                tool_name = tool_call["name"]

                # Display tool call
                self._display_tool_call(tool_name, tool_call)

                # Execute tool
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

                # Log and display results
                self._log_tool_result(tool_name, result)

            # Add tool results to messages
            for observation, tool_call in zip(observations, response.tool_calls):
                messages.append({
                    "role": "tool",
                    "content": str(observation),
                    "tool_call_id": tool_call["id"]
                })

            console.print(f"[dim]{self.get_synthesis_message()}[/dim]")
            self._log("Synthesizing analysis...")
            response = await self.model_with_tools.ainvoke(messages)
            messages.append({"role": "assistant", "content": response.content, "tool_calls": response.tool_calls or []})
            self._log(f"Model response (length: {len(str(response.content))} chars): {str(response.content)[:500]}...")

        return messages, response

    def _display_tool_call(self, tool_name: str, tool_call: dict):
        """Display tool call to console (can be overridden by subclasses)."""
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

    def _log_tool_result(self, tool_name: str, result: Any):
        """Log and display tool results (can be overridden by subclasses)."""
        if tool_name == "tavily_search":
            console.print(f"[dim green]✅ Market intelligence gathered[/dim green]")
            self._log(f"SEARCH RESULT (length: {len(str(result))} chars): {str(result)[:500]}...", level="RESULT")
        elif tool_name == "query_momo_data":
            console.print(f"[dim red]✅ MoMo intelligence gathered[/dim red]")
            self._log(f"MOMO DATA RESULT:\n{result}", level="MOMO_DATA")

    def _simple_extract_items(self, response_content: str, prefixes: List[str]) -> List[str]:
        """Simple fallback method to extract items from text.

        Args:
            response_content: Raw text content
            prefixes: List of prefixes to look for (e.g., ['1.', '2.', '##'])

        Returns:
            List of extracted items
        """
        lines = response_content.split('\n')
        items = []
        current_item = []

        for line in lines:
            line_stripped = line.strip()
            # Look for item boundaries
            if line_stripped and any(line_stripped.startswith(prefix) for prefix in prefixes):
                if current_item:
                    items.append('\n'.join(current_item))
                    current_item = []
                current_item.append(line)
            elif current_item:
                current_item.append(line)

        # Add last item
        if current_item:
            items.append('\n'.join(current_item))

        return items if items else [response_content]

    def _save_outputs_to_file(
        self,
        outputs: List[str],
        filename_prefix: str,
        title: str,
        description: str
    ) -> str:
        """Save generated outputs to a markdown file.

        Args:
            outputs: List of output items to save
            filename_prefix: Prefix for filename (e.g., "mrt_topics")
            title: Title for the markdown file
            description: Description text for the file

        Returns:
            Path to the saved file
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"{filename_prefix}_{timestamp}.md"

        output_dir = Path(".output")
        output_dir.mkdir(exist_ok=True)
        file_path = output_dir / filename

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**CEO:** {self.persona.get('name', 'N/A')}\n")
            f.write(f"**Company:** {self.persona.get('company', 'N/A')}\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
            f.write(f"**Total Items:** {len(outputs)}\n\n")
            f.write("---\n\n")
            f.write(f"## {description}\n\n")
            f.write("---\n\n")

            for i, output in enumerate(outputs, 1):
                f.write(f"## Item {i}\n\n")
                f.write(f"{output}\n\n")
                f.write("---\n\n")

        console.print(f"[green]📁 Outputs saved to: {file_path}[/green]")
        return str(file_path)

    # Abstract methods that subclasses must implement
    @abstractmethod
    def get_log_title(self) -> str:
        """Return title for debug log file."""
        pass

    @abstractmethod
    def get_synthesis_message(self) -> str:
        """Return message to display during synthesis phase."""
        pass

    @abstractmethod
    async def generate(self, *args, **kwargs) -> List[str]:
        """Main generation method - must be implemented by subclasses."""
        pass
