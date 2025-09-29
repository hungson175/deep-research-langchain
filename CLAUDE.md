# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

### Setup and Installation
```bash
# Install dependencies (Python 3.13+)
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Then add your API keys to .env file
```

### Running the System
```bash
# Run the main research system
python deep_research_system.py

# Run individual components for testing
python clarifier.py    # Test clarification phase
python supervisor.py   # Test supervisor coordination
python researcher.py   # Test individual researcher

# Run educational version (consolidated, no logging)
cd educational_no_logging
python core_system.py
```

### Development
```bash
# No specific test framework configured - tests are manual
# To test LLM functionality, run individual component files

# Check for Python syntax errors
python -m py_compile *.py
```

## Architecture Overview

This is a multi-agent deep research system built with LangChain (without LangGraph). The system follows a four-phase architecture:

### Phase 1: Clarification (clarifier.py)
- `ResearchBriefCreator` class interacts with users to clarify research intent
- Transforms user input into structured research briefs
- Uses Grok Code Fast model by default

### Phase 2: Supervised Research (supervisor.py)
- `Supervisor` class coordinates multiple parallel research agents
- Uses lead researcher prompt to plan and delegate research tasks
- Launches up to 3 concurrent `Researcher` agents
- Each researcher has 3 iterations to gather information using Tavily search

### Phase 3: Report Generation (deep_research_system.py)
- `DeepResearch` class orchestrates the entire pipeline
- Collects research notes from all agents
- Generates comprehensive final report using Claude Sonnet model
- Automatically saves reports to `./reports/` directory with timestamp-based filenames

### Phase 4: Insight Page Generation (insight_generator.py) - NEW
- `InsightGenerator` class creates interactive HTML insight pages from research notes
- Generates concise 2-4 page visual summaries highlighting key findings
- Uses Claude Code SDK to generate interactive HTML with charts/tabs
- Focuses on actionable insights, not full content (helps users decide if they want to read the full report)
- Requires `claude-code-sdk` package (optional dependency)
- Automatically saves to `./reports/htmls/` directory with timestamp-based filenames

## Key Components

- **Cache Strategy**: `cache_strategy.py` implements caching for Anthropic models to optimize token usage
  - `AnthropicCacheStrategy` for Claude models uses prompt caching
  - `StandardCacheStrategy` for other models (no caching)
  - `CacheStrategyFactory` automatically selects appropriate strategy
- **Prompts**: All system prompts centralized in `prompts.py`
  - Lead researcher prompt (supervisor coordination)
  - Research brief creation prompts
  - Final report generation template
- **Utils**: Helper functions in `utils.py` for formatting, logging, and tool management
  - Tavily search tool wrapper
  - Think tool for researcher reflection
  - Message formatting utilities
- **Reports Directory**: `./reports/` stores saved research reports (gitignored)
  - Auto-generated filenames: `{description}_{YYYYMMDD_HHMM}.md`
  - HTML insight pages: `./reports/htmls/insights_{description}_{YYYYMMDD_HHMM}.html`
- **Insight Generator**: `insight_generator.py` creates interactive HTML summaries (NEW)
  - Extracts key insights from research notes (not final report)
  - Generates 2-4 page visual summaries with charts/tabs
  - Uses Claude Code SDK for HTML generation
  - Optional feature - gracefully disabled if SDK not installed
- **Educational Version**: `./educational_no_logging/` contains consolidated clean code for learning
  - `core_system.py` - All classes in one file (~310 lines)
  - `prompts.py` - Prompts only (~78 lines)
  - `utils.py` - Helpers and cache strategies (~159 lines)
- **Visual Logging**: Rich library provides beautiful console output with progress tracking
- **Models Used**:
  - Clarifier: `xai:grok-code-fast-1`
  - Supervisor: `xai:grok-code-fast-1`
  - Researcher: `xai:grok-code-fast-1`
  - Final Report Writer: `anthropic:claude-sonnet-4-20250514`
  - Insight Page Generator: Claude via `claude-code-sdk` (interactive HTML generation)

## API Keys Required

The system requires the following API keys in `.env`:
- `ANTHROPIC_API_KEY` - For Claude models (final report generation)
- `XAI_API_KEY` - For Grok models (clarifier, supervisor, researchers)
- `TAVILY_API_KEY` - For web search functionality
- Optional: `OPENAI_API_KEY`, `GOOGLE_API_KEY` for alternative models

## Important Notes

- **Do NOT test LLM-related code** without explicit instruction - API calls are expensive
- The system uses async/await throughout - all main functions are coroutines
- Research iteration limits: Supervisor (6 iterations), each Researcher (3 iterations)
- Up to 3 concurrent researchers can be launched in parallel
- Reports are automatically saved with descriptive filenames based on user input
- The educational version in `educational_no_logging/` has identical logic but cleaner presentation
- `mirmir_research_agent.py` exists but is separate from the main research pipeline
- **Insight generation** uses `permission_mode='acceptAll'` to allow Claude full access to all tools (Read, Write, Bash, etc.) for creating interactive HTML pages
- **Performance tracking**: System automatically tracks time and token usage for each phase, displaying a summary table at the end
- **Timeout configuration**: All LLM requests use `request_timeout=240` seconds (4 minutes) to prevent timeouts during long MirMir queries (which can take up to 3 minutes)