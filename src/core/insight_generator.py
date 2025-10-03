"""
InsightGenerator: Generate interactive HTML insights from research notes

This module creates concise, visual HTML insight pages (2-4 pages) highlighting
key findings from research notes. Unlike full reports, these pages focus on
actionable insights with charts and tabs for quick comprehension.
"""

import os
import time
from pathlib import Path
from typing import Optional, Callable, Any, Dict
from dotenv import load_dotenv

load_dotenv()

try:
    from claude_code_sdk import query, ClaudeCodeOptions
    CLAUDE_SDK_AVAILABLE = True
except ImportError:
    CLAUDE_SDK_AVAILABLE = False

from ..utils.helpers import console
from rich.panel import Panel


class InsightGenerator:
    """
    Generates interactive HTML insight pages from research notes.

    This class creates concise, visual summaries (2-4 pages) highlighting key
    insights, patterns, and actionable findings to help users quickly understand
    research results before diving into full reports.
    """

    def __init__(self, output_dir: str = "reports/htmls", stream_callback: Optional[Callable] = None):
        """
        Initialize the InsightGenerator.

        Args:
            output_dir: Directory to save HTML insight pages
            stream_callback: Optional callback for streaming progress updates
        """
        self.output_dir = Path(output_dir)
        self.stream_callback = stream_callback or self._default_stream_callback

        self.output_dir.mkdir(parents=True, exist_ok=True)

        if not CLAUDE_SDK_AVAILABLE:
            raise ImportError(
                "Claude Code SDK not available. Install with: pip install claude-code-sdk"
            )

        if not os.getenv("ANTHROPIC_API_KEY"):
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable is required. "
                "Add it to your .env file: ANTHROPIC_API_KEY=your-api-key-here"
            )

    def _default_stream_callback(self, event_type: str, data: Dict[str, Any]) -> None:
        """Default streaming callback that prints progress to console."""
        timestamp = data.get('timestamp', 0)

        if event_type == 'start':
            console.print(Panel(
                f"[bold cyan]🎨 Generating Interactive Insight Page[/bold cyan]\n\n"
                f"Input: {data['input_size']:,} characters from {data['num_notes']} research notes",
                border_style="cyan"
            ))

        elif event_type == 'thinking':
            text_snippet = data['text'][:100].replace('\n', ' ')
            console.print(f"[dim cyan]💭 [{timestamp:.1f}s] {text_snippet}...[/dim cyan]")

        elif event_type == 'tool_use':
            tool_name = data['tool_name']
            if tool_name == "Write":
                console.print(f"[cyan]📝 [{timestamp:.1f}s] Writing to: {data['output_path']}[/cyan]")

        elif event_type == 'file_progress':
            size = data['current_size']
            console.print(f"[dim]📊 [{timestamp:.1f}s] File size: {size:,} bytes[/dim]")

        elif event_type == 'complete':
            total_time = data['total_time']
            file_size = data['file_size']
            console.print(Panel(
                f"[bold green]✅ Insight page generated in {total_time:.1f}s[/bold green]\n\n"
                f"File size: {file_size:,} characters\n"
                f"Speed: {file_size/total_time:.0f} chars/sec",
                border_style="green"
            ))

        elif event_type == 'success':
            console.print(f"[green]✨ Saved to: {data['output_path']}[/green]")

        elif event_type == 'error':
            console.print(f"[red]❌ Error: {data['error']}[/red]")

    async def generate_insight_page(
        self,
        research_notes: list,
        research_brief: str,
        filename: str,
        title: Optional[str] = None
    ) -> tuple[bool, str]:
        """
        Generate an interactive HTML insight page from research notes.

        Args:
            research_notes: List of research findings from multiple researchers
            research_brief: The original research brief/query
            filename: Output filename (without extension)
            title: Optional custom title for the insight page

        Returns:
            tuple: (success: bool, output_path: str)
        """

        if not filename.endswith('.html'):
            filename = f"{filename}.html"
        output_path = self.output_dir / filename

        num_notes = len(research_notes)
        combined_notes = "\n\n---\n\n".join(research_notes)

        self.stream_callback('start', {
            'filename': filename,
            'input_size': len(combined_notes),
            'num_notes': num_notes,
            'output_path': str(output_path)
        })

        insight_prompt = f"""
Create a CONCISE HTML insight page (2 pages max when printed) - focus on VISUALS and KEY INSIGHTS with brief context.

CRITICAL: This is an INSIGHTS PAGE, NOT a full report. Users will read the .md file for details.
Your job: Extract top 3-5 insights and present them with charts/metrics. Keep text brief but informative.

RESEARCH BRIEF:
{research_brief}

RESEARCH NOTES:
{combined_notes}

YOUR TASK:
1. Extract top 3-5 key insights (prioritize most impactful)
2. Present insights with:
   - Visual metrics/numbers (e.g., "65% growth", "$2.3M market size")
   - Charts/graphs (bar, line, pie, doughnut) - use Chart.js
   - Comparison tables or data grids (if relevant)
   - Brief context (1-2 sentences per insight)
3. Keep text concise but informative:
   - Executive summary: 2-3 sentences max
   - Each insight: Title + 2-3 sentences + visual/data
   - Recommendations: Bullet points with brief explanations (5-7 items)

STRUCTURE (balanced layout - scannable in ~1 minute):
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Insights{f': {title}' if title else ''}</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    :root {{
      --momo-pink: #a50064;
      --momo-pink-light: #f9b5c3;
    }}
    body {{ font-family: system-ui; }}
  </style>
</head>
<body class="bg-gray-50">
  <!-- Header with MoMo logo -->
  <nav class="bg-white shadow-sm px-6 py-3 flex items-center">
    <img src="https://homepage.momocdn.net/fileuploads/svg/momo-file-240411162904.svg" alt="MoMo" class="h-8" />
  </nav>

  <!-- Main content -->
  <main class="max-w-6xl mx-auto px-6 py-6">
    <!-- Title & Executive Summary -->
    <h1 class="text-2xl font-bold mb-2">Research Insights</h1>
    <p class="text-gray-600 text-sm mb-6 leading-relaxed">2-3 sentence executive summary highlighting the most critical findings and implications for MoMo.</p>

    <!-- Top metrics banner (4-6 key numbers) -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
      <!-- Metric cards with numbers + labels -->
    </div>

    <!-- Key insights grid (3-5 cards with visuals) -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-5 mb-6">
      <!-- Card 1: Insight with chart/metric -->
      <div class="bg-white p-5 rounded shadow-sm">
        <h3 class="font-bold text-base mb-2 text-[#a50064]">1. Insight Title</h3>
        <p class="text-sm text-gray-600 mb-3">2-3 sentences providing context and key takeaway.</p>
        <canvas id="chart1" class="max-h-52"></canvas>
      </div>
      <!-- Cards 2-6 similar structure -->
    </div>

    <!-- Recommendations section -->
    <div class="bg-white p-5 rounded shadow-sm border-l-4 border-[#a50064]">
      <h3 class="font-bold text-base mb-3">Strategic Recommendations</h3>
      <ul class="list-disc pl-5 text-sm space-y-2">
        <li><strong>Action:</strong> Brief explanation (1 sentence)</li>
        <!-- 5-7 bullet points total -->
      </ul>
    </div>
  </main>

  <!-- Footer -->
  <footer class="text-center py-4 text-xs text-gray-500 border-t">
    MoMo © 2025 | Full research details available in .md report
  </footer>

  <!-- Chart.js scripts -->
</body>
</html>
```

DESIGN RULES:
- Use MoMo pink (#a50064) for highlights and accents
- Use Tailwind utility classes (minimal custom CSS)
- Charts: 2-4 charts total (use varied types: bar, line, doughnut, radar)
- Text: Keep paragraphs to 2-3 sentences max
- Each insight needs: title + brief context + visual element
- Balance between visual impact and informative content
- Target reading time: ~1 minute

SAVE TO: {output_path}

Remember: INSIGHTS = VISUALS + METRICS, not text! Users read .md for details.
"""

        options = ClaudeCodeOptions(
            permission_mode='bypassPermissions',
            max_turns=50,
            system_prompt="You are a data visualization expert. Create concise HTML insight pages (2 pages max, ~1 minute reading time). Balance visuals with brief context: charts, metrics, numbers, and 2-3 sentence explanations per insight. Extract 3-5 key insights with varied chart types (bar, line, doughnut, radar). Use MoMo pink (#a50064) and Tailwind CSS. Keep it informative but scannable - users read .md for full details."
        )

        try:
            start_time = time.time()
            message_count = 0
            tool_uses = []
            last_file_size = 0
            html_generated = False

            async for message in query(prompt=insight_prompt, options=options):
                message_count += 1
                elapsed = time.time() - start_time

                if hasattr(message, 'content') and message.content:
                    for block in message.content:
                        if hasattr(block, 'text'):
                            self.stream_callback('thinking', {
                                'text': block.text,
                                'timestamp': elapsed
                            })
                        elif hasattr(block, 'name'):
                            tool_name = block.name
                            tool_uses.append(tool_name)
                            self.stream_callback('tool_use', {
                                'tool_name': tool_name,
                                'output_path': str(output_path),
                                'timestamp': elapsed
                            })

                if output_path.exists():
                    current_size = output_path.stat().st_size
                    if current_size != last_file_size:
                        self.stream_callback('file_progress', {
                            'current_size': current_size,
                            'size_increment': current_size - last_file_size,
                            'timestamp': elapsed
                        })
                        last_file_size = current_size
                        html_generated = True

                if elapsed > 300:
                    self.stream_callback('timeout', {'timestamp': elapsed})
                    break

            total_time = time.time() - start_time

            self.stream_callback('complete', {
                'total_time': total_time,
                'message_count': message_count,
                'tools_used': tool_uses,
                'file_size': len(output_path.read_text()) if output_path.exists() else 0
            })

            if html_generated and output_path.exists():
                content = output_path.read_text(encoding='utf-8')
                if "<!DOCTYPE" in content or "<html>" in content:
                    self.stream_callback('success', {
                        'output_path': str(output_path)
                    })
                    return True, str(output_path)
                else:
                    self.stream_callback('error', {
                        'error': 'File created but doesn\'t contain valid HTML content',
                        'content_preview': content[:200]
                    })
                    return False, str(output_path)
            else:
                self.stream_callback('error', {
                    'error': 'HTML file was not created. Claude may not have used the Write tool.',
                    'tools_detected': tool_uses
                })
                return False, str(output_path)

        except Exception as e:
            import traceback
            self.stream_callback('error', {
                'error': str(e),
                'traceback': traceback.format_exc()
            })
            return False, str(output_path)

    @staticmethod
    def create_quiet_callback() -> Callable[[str, Dict[str, Any]], None]:
        """Create a minimal callback that only shows major progress."""
        def quiet_callback(event_type: str, data: Dict[str, Any]) -> None:
            if event_type in ['start', 'success', 'error']:
                if event_type == 'start':
                    console.print(f"[cyan]🎨 Generating insight page: {data['filename']}...[/cyan]")
                elif event_type == 'success':
                    console.print(f"[green]✅ Saved to {data['output_path']}[/green]")
                elif event_type == 'error':
                    console.print(f"[red]❌ Error: {data['error']}[/red]")

        return quiet_callback


async def generate_insight_from_notes(
    research_notes: list,
    research_brief: str,
    output_filename: str,
    output_dir: str = "reports/htmls",
    title: Optional[str] = None,
    quiet: bool = False
) -> tuple[bool, str]:
    """
    Quick function to generate an HTML insight page from research notes.

    Args:
        research_notes: List of research findings
        research_brief: Original research query
        output_filename: Output filename (with or without .html extension)
        output_dir: Output directory (default: "reports/htmls")
        title: Optional custom title for the insight page
        quiet: If True, use minimal console output

    Returns:
        tuple: (success: bool, output_path: str)
    """
    callback = InsightGenerator.create_quiet_callback() if quiet else None
    generator = InsightGenerator(output_dir=output_dir, stream_callback=callback)

    return await generator.generate_insight_page(
        research_notes=research_notes,
        research_brief=research_brief,
        filename=output_filename,
        title=title
    )