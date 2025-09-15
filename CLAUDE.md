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

# Run educational version (no logging)
cd educational_no_logging
python deep_research_system_complete.py
```

## Architecture Overview

This is a multi-agent deep research system built with LangChain (without LangGraph). The system follows a three-phase architecture:

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

## Key Components

- **Cache Strategy**: `cache_strategy.py` implements caching for Anthropic models to optimize token usage
- **Prompts**: All system prompts centralized in `prompts.py`
- **Utils**: Helper functions in `utils.py` for formatting, logging, and tool management
- **Reports Directory**: `./reports/` stores saved research reports (gitignored)
- **Educational Version**: `./educational_no_logging/` contains consolidated clean code for learning
- **Visual Logging**: Rich library provides beautiful console output with progress tracking
- **Models Used**:
  - Clarifier: `xai:grok-code-fast-1`
  - Supervisor: `xai:grok-code-fast-1`
  - Researcher: `xai:grok-code-fast-1`
  - Final Report Writer: `anthropic:claude-sonnet-4-20250514`

## API Keys Required

The system requires the following API keys in `.env`:
- `ANTHROPIC_API_KEY` - For Claude models
- `XAI_API_KEY` - For Grok models
- `TAVILY_API_KEY` - For web search functionality
- Optional: `OPENAI_API_KEY`, `GOOGLE_API_KEY` for alternative models