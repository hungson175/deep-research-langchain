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
Create an interactive single-page HTML insight summary that highlights KEY FINDINGS and ACTIONABLE INSIGHTS from research notes using MoMo's design system.

IMPORTANT CONTEXT:
- This is NOT a full report - it's a visual executive summary (2-3 pages when printed)
- Purpose: Help users quickly understand key insights and decide if they want to read the full report
- Focus: Patterns, trends, surprising findings, actionable recommendations
- Format: Modern, visual, interactive with charts/tabs/sections using MoMo design system

RESEARCH BRIEF:
{research_brief}

RESEARCH NOTES FROM MULTIPLE RESEARCHERS:
{combined_notes}

YOUR TASK:
1. Analyze all research notes and identify:
   - Top 3-5 key insights
   - Important trends or patterns
   - Surprising or counterintuitive findings
   - Actionable recommendations

2. Create a self-contained HTML file with MoMo design system:
   - Professional MoMo-style navigation with logo
   - Executive summary (2-3 sentences)
   - Key insights section with visual emphasis
   - Data visualizations (charts, comparison tables) where appropriate
   - Tabbed sections for different aspects if needed
   - Actionable recommendations highlighted
   - Modern, responsive design with smooth interactions
   - MoMo footer with company information
   - All CSS/JS inline (Chart.js from CDN is allowed)

3. MANDATORY MoMo Design System Requirements:
   - Use MoMo color palette: Primary Pink #a50064, Secondary Pink #d82f8b, Light Pink #f9b5c3
   - Use Tailwind CSS from CDN: https://cdn.tailwindcss.com
   - Include MoMo logo: https://homepage.momocdn.net/fileuploads/svg/momo-file-240411162904.svg
   - Follow MoMo CSS classes and patterns from the design system
   - Use MoMo shadows, typography, and component styles
   - Professional fintech aesthetic with trustworthy design

4. Required Structure with MoMo Components:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Research Insights{f': {title}' if title else ''}</title>
     <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
     <script src="https://cdn.tailwindcss.com"></script>
     <style>
       :root {{
         --momo-pink-primary: #a50064;
         --momo-pink-secondary: #d82f8b;
         --momo-pink-light: #f9b5c3;
         --momo-gray-900: #1c171a;
         --momo-gray-600: #574d56;
         --momo-gray-100: #f5f4f5;
         --momo-shadow-sm: 0px 0px 5px 0px rgba(0, 0, 0, 0.02), 0px 2px 10px 0px rgba(0, 0, 0, 0.06);
         --momo-shadow-md: 0px 0px 15px 0px rgba(0, 0, 0, 0.03), 0px 2px 30px 0px rgba(0, 0, 0, 0.08);
       }}
       /* Add custom MoMo styles here */
     </style>
   </head>
   <body class="bg-gray-50">
     <!-- MoMo Navigation -->
     <nav class="bg-white shadow-sm border-b border-gray-100 sticky top-0 z-50">
       <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
         <div class="flex items-center space-x-3">
           <img src="https://homepage.momocdn.net/fileuploads/svg/momo-file-240411162904.svg" alt="MoMo" class="h-8 w-auto" />
         </div>
       </div>
     </nav>

     <!-- Main Content -->
     <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
       <!-- Executive Summary -->
       <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-8 mb-8">
         <h1 class="text-3xl sm:text-4xl font-bold text-gray-900 mb-4">Research Insights</h1>
         <p class="text-lg text-gray-600 leading-relaxed">Executive summary...</p>
       </div>

       <!-- Key Insights -->
       <section class="mb-8">
         <h2 class="text-2xl font-semibold text-gray-900 mb-6">🎯 Key Insights</h2>
         <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
           <!-- Insight cards with MoMo styling -->
         </div>
       </section>

       <!-- Data Visualizations -->
       <section class="mb-8">
         <h2 class="text-2xl font-semibold text-gray-900 mb-6">📊 Data Visualizations</h2>
         <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
           <!-- Charts and graphs -->
         </div>
       </section>

       <!-- Recommendations -->
       <section class="mb-8">
         <h2 class="text-2xl font-semibold text-gray-900 mb-6">💡 Recommendations</h2>
         <div class="space-y-4">
           <!-- Recommendation cards -->
         </div>
       </section>
     </main>

     <!-- MoMo Footer -->
     <footer class="bg-gray-50 border-t border-gray-200 py-8 mt-12">
       <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
         <div class="flex items-center space-x-3 mb-4">
           <img src="https://homepage.momocdn.net/fileuploads/svg/momo-file-240411162904.svg" alt="MoMo" class="h-8 w-auto" />
           <span class="font-semibold text-gray-900">MoMo</span>
         </div>
         <div class="text-sm text-gray-600 leading-relaxed">
           <p class="font-semibold text-gray-900">CÔNG TY CỔ PHẦN DỊCH VỤ DI ĐỘNG TRỰC TUYẾN</p>
           <p>Trụ sở chính: Tầng 6, Tòa nhà Phú Mỹ Hưng, Số 8, đường Hoàng Văn Thái, Phường Tân Mỹ, Thành phố Hồ Chí Minh</p>
           <p><strong>Tên thương hiệu:</strong> MoMo</p>
         </div>
         <div class="text-xs text-gray-500 mt-4">
           <p>©Copyright M_Service 2025</p>
         </div>
       </div>
     </footer>
   </body>
   </html>
   ```

5. MoMo Component Guidelines:
   - Use .card-momo classes for insight cards
   - Use .btn-primary for primary actions with MoMo pink
   - Use .service-card pattern for key insights
   - Implement proper spacing with .section-spacing
   - Use MoMo typography classes (.heading-1, .heading-2, .text-body)
   - Apply MoMo shadows (--momo-shadow-sm, --momo-shadow-md)

SAVE THE HTML FILE TO: {output_path}

Remember: This is an INSIGHT PAGE using MoMo's professional fintech design system. Focus on what matters most with MoMo's trustworthy aesthetic!
"""

        options = ClaudeCodeOptions(
            permission_mode='bypassPermissions',
            max_turns=50,
            system_prompt="You are an expert data analyst and web designer specializing in MoMo's design system. Create concise, visual HTML insight pages that highlight key findings and actionable recommendations using MoMo's professional fintech aesthetic. Use MoMo's color palette (#a50064, #d82f8b, #f9b5c3), Tailwind CSS, official MoMo logo, and component patterns. Focus on trustworthy, modern design with charts and interactive elements that reflect MoMo's brand identity."
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