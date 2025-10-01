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
# Run the main research system (recommended)
python main.py

# Or run the core system directly
python -m src.deep_research_system

# MrT Generator Pipeline (new) - Automated topic generation + research
python -m src.mrw_explorer D    # Daily analysis (1 research brief)
python -m src.mrw_explorer W    # Weekly analysis (1 research brief)
python -m src.mrw_explorer M    # Monthly analysis (3 research briefs)
python -m src.mrw_explorer Q    # Quarterly analysis (3 research briefs)
python -m src.mrw_explorer Y    # Yearly analysis (5 research briefs)

# Opponent CEO Agent (new) - Competitive intelligence from rival CEOs
python -m src.opp_ceo_agent_topic_generator  # Demo mode (ZaloPay CEO, 3 briefs)

# Run individual components for testing
python -m src.clarifier          # Test clarification phase
python -m src.supervisor         # Test supervisor coordination
python -m src.researcher         # Test individual researcher
python -m src.topics_generator   # Test MrT topic generation (generates research briefs)
python -m src.question_generator # Test MrT question generation (generates strategic questions)
python -m src.opp_ceo_agent_topic_generator  # Test opponent CEO (ZaloPay/VNPay)

# Run tests
python -m pytest tests/   # Run all tests
python tests/simple_test.py   # Run simple integration test

# Run educational version (consolidated, no logging)
cd educational_no_logging
python core_system.py
```

### Development
```bash
# Run tests (avoid testing LLM functionality unless necessary - it's expensive)
python tests/simple_test.py              # Simple integration test
python tests/test_insight_generator.py   # Test insight generation

# Check for Python syntax errors
python -m py_compile src/*.py
python -m py_compile tests/*.py
python -m py_compile main.py
```

## Project Structure

```
deep_research_langchain/
├── main.py                     # Main entry point for the system
├── src/                        # Core application modules
│   ├── __init__.py            # Package initialization
│   ├── cache_strategy.py      # LLM caching strategies
│   ├── clarifier.py           # Research brief creation
│   ├── config.py              # Configuration and settings
│   ├── deep_research_system.py # Main orchestration system
│   ├── insight_generator.py   # HTML insight page generation
│   ├── prompts.py             # All system prompts
│   ├── researcher.py          # Individual research agent
│   ├── supervisor.py          # Multi-agent coordination
│   ├── utils.py               # Helper functions and tools
│   ├── topics_generator.py    # MrT persona: generates research briefs from market trends
│   ├── question_generator.py  # MrT persona: generates strategic questions from topics
│   ├── mrw_explorer.py        # Automated pipeline: topics → sequential deep research
│   └── opp_ceo_agent_topic_generator.py  # Opponent CEOs: ZaloPay/VNPay competitive intelligence
├── tests/                     # Test files
│   ├── simple_test.py         # Simple integration test
│   └── test_insight_generator.py # Insight generator tests
├── docs/                      # Documentation
│   ├── current_prompt.md      # Development progress notes
│   └── MrT_generator.md       # MrT persona and pipeline documentation
├── educational_no_logging/    # Clean reference implementation
│   ├── core_system.py         # Consolidated system (all classes)
│   ├── prompts.py            # Prompts only
│   ├── utils.py              # Utilities only
│   └── README.md             # Educational documentation
├── reports/                   # Generated research outputs (gitignored)
│   ├── .gitignore            # Ignore all content except this file
│   ├── htmls/                # HTML insight pages
│   └── spas/                 # Single-page applications
├── .output/                   # MrT generated topics (gitignored)
│   ├── mrT_topics_*.md       # Timestamped MrT research briefs
│   └── opponent_{ceo_type}_briefs_*.md  # Timestamped opponent CEO briefs
├── sample_codes/              # Reference code (not part of main system)
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies
└── CLAUDE.md                 # This file
```

## Architecture Overview

This is a multi-agent deep research system built with LangChain (without LangGraph).

### Core Research Pipeline (4 phases)

**Phase 1: Clarification** (`src/clarifier.py`)
- `ResearchBriefCreator` class interacts with users to clarify research intent
- Transforms user input into structured research briefs
- Can be skipped when using MrT-generated briefs

**Phase 2: Supervised Research** (`src/supervisor.py`)
- `Supervisor` coordinates multiple parallel research agents
- Uses lead researcher prompt to plan and delegate tasks
- Launches up to 5 concurrent `Researcher` agents (configurable)
- Each researcher has 4 iterations using Tavily search + think tool

**Phase 3: Report Generation** (`src/deep_research_system.py`)
- `DeepResearch` orchestrates the entire pipeline
- Collects research notes from all agents
- Generates comprehensive final report
- Automatically saves to `./reports/` with timestamp-based filenames

**Phase 4: Insight Page Generation** (`src/insight_generator.py`)
- `InsightGenerator` creates interactive HTML insight pages
- Generates concise 2-4 page visual summaries with charts/tabs
- Uses Claude Code SDK (optional dependency)
- Saves to `./reports/htmls/` with timestamp-based filenames

### MrT Generator Pipeline (NEW)

Automated research pipeline that simulates CEO "Nguyễn Mạnh Tường" (MoMo CEO) to generate strategic research topics and execute research autonomously.

**MrT Topics Generator** (`src/topics_generator.py`)
- Simulates MrT persona analyzing market trends and news
- Searches current developments (fintech, digital banking, regulation, competition)
- Generates complete research briefs based on time period:
  - Daily (D): 1 brief
  - Weekly (W): 1 brief
  - Monthly (M): 3 briefs
  - Quarterly (Q): 3 briefs
  - Yearly (Y): 5 briefs
- Each brief includes: research objective, background, investigation areas, expected insights
- Saves briefs to `.output/mrT_topics_*.md`

**MrT Question Generator** (`src/question_generator.py`)
- Uses MrT persona to generate strategic questions from topics
- Focuses on: financial inclusion, innovation, business growth, regulatory impact
- Uses think tool + Tavily search to research before generating questions
- Outputs structured questions using Pydantic models

**MrW Explorer** (`src/mrw_explorer.py`)
- Automated pipeline: generates topics → runs deep research sequentially
- Combines `TopicsGenerator` + `DeepResearch`
- Executes research on each generated brief sequentially (not parallel)
- Displays summary table of all research results

### Opponent CEO Agent (NEW)

Simulates competitor CEOs (ZaloPay/VNPay) conducting competitive intelligence on MoMo to generate attack strategies.

**Opponent CEO Topic Generator** (`src/opp_ceo_agent_topic_generator.py`)
- Simulates two CEO personas:
  - **ZaloPay CEO (Nguyễn Tuấn Anh)**: Leverages Zalo ecosystem (70M+ users), social payments, Gen Z focus
  - **VNPay CEO (Lê Hồng Minh)**: Leverages 40+ banking partnerships, merchant network, enterprise solutions
- Uses THREE tools for competitive intelligence:
  - `query_momo_data`: Analyzes MoMo's internal metrics (GMV, users, products) to find weaknesses
  - `tavily_search`: Researches public market trends, competitor moves, customer sentiment
  - `think_tool`: Synthesizes intelligence to identify strategic attack vectors
- Generates complete research briefs focused on competing with or surpassing MoMo
- Each brief includes: research objective, MoMo weakness being exploited, investigation areas, expected insights, success metrics
- Saves briefs to `.output/opponent_{ceo_type}_briefs_*.md`
- Output briefs are compatible with deep research pipeline for competitive strategy reports

## Key Components

- **Cache Strategy**: `src/cache_strategy.py` implements caching for Anthropic models to optimize token usage
  - `AnthropicCacheStrategy` for Claude models uses prompt caching
  - `StandardCacheStrategy` for other models (no caching)
  - `CacheStrategyFactory` automatically selects appropriate strategy
- **Prompts**: All system prompts centralized in `src/prompts.py`
  - Lead researcher prompt (supervisor coordination)
  - Research brief creation prompts
  - Final report generation template
- **Utils**: Helper functions in `src/utils.py` for formatting, logging, and tool management
  - Tavily search tool wrapper
  - Think tool for researcher reflection
  - Message formatting utilities
- **Reports Directory**: `./reports/` stores saved research reports (gitignored)
  - Auto-generated filenames: `{description}_{YYYYMMDD_HHMM}.md`
  - HTML insight pages: `./reports/htmls/insights_{description}_{YYYYMMDD_HHMM}.html`
- **Insight Generator**: `src/insight_generator.py` creates interactive HTML summaries (NEW)
  - Extracts key insights from research notes (not final report)
  - Generates 2-4 page visual summaries with charts/tabs
  - Uses Claude Code SDK for HTML generation
  - Optional feature - gracefully disabled if SDK not installed
- **Educational Version**: `./educational_no_logging/` contains consolidated clean code for learning
  - `core_system.py` - All classes in one file (~310 lines)
  - `prompts.py` - Prompts only (~78 lines)
  - `utils.py` - Helpers and cache strategies (~159 lines)
- **Visual Logging**: Rich library provides beautiful console output with progress tracking
- **Models Used** (configurable in `src/config.py`):
  - Clarifier: `grok-4-fast` (0.0 temp)
  - Topics/Question Generator (MrT): `grok-4-fast-reasoning` (0.0 temp)
  - Supervisor: `grok-4-fast-reasoning` (0.0 temp)
  - Researcher: `grok-4-fast` (0.0 temp, 4 iterations)
  - Summarization: `grok-4-fast` (0.0 temp)
  - Final Report Writer: `grok-4-fast-reasoning` (0.0 temp, 32K max tokens)
  - Insight Page Generator: Claude via `claude-code-sdk`
- **MirMir Integration**: Custom API server for specialized research queries
  - Base URL: `http://localhost:8001` (configurable)
  - Timeout: 240 seconds (4 minutes)
  - LLM request timeout matches MirMir timeout to prevent premature termination

## API Keys Required

The system requires the following API keys in `.env`:
- `ANTHROPIC_API_KEY` - For Claude models (final report generation)
- `XAI_API_KEY` - For Grok models (clarifier, supervisor, researchers)
- `TAVILY_API_KEY` - For web search functionality
- Optional: `OPENAI_API_KEY`, `GOOGLE_API_KEY` for alternative models

## Important Notes

- **Do NOT test LLM-related code** without explicit instruction - API calls are expensive
- The system uses async/await throughout - all main functions are coroutines
- **Research iteration limits** (configurable in `src/config.py`):
  - Supervisor: 6 iterations
  - Each Researcher: 4 iterations
  - Question Generator: 3 iterations
  - Topics Generator: 5 iterations
- **Concurrent researchers**: Up to 5 can be launched in parallel (was 3, now configurable)
- **Reports**: Automatically saved with descriptive filenames based on user input
  - Research reports: `./reports/{description}_{timestamp}.md`
  - Insight pages: `./reports/htmls/insights_{description}_{timestamp}.html`
  - MrT topics: `.output/mrT_topics_{timestamp}.md`
- **Educational version**: `educational_no_logging/` has identical logic but cleaner presentation
- **Insight generation**: Uses `permission_mode='acceptAll'` to allow Claude full access to all tools
- **Performance tracking**: Automatically tracks time and token usage for each phase with summary table
- **Timeout configuration**: All LLM requests use 240 seconds to prevent timeouts during long operations
- **MrT Pipeline**: The `mrw_explorer` runs research **sequentially** (not parallel) to avoid overwhelming the system
- **Opponent CEO Agent**: Uses MirMir tool to analyze MoMo's internal data for competitive intelligence - requires MirMir API server running on localhost:8001