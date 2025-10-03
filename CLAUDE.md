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

# MrW Explorer Pipeline - Automated topic generation + sequential deep research
python -m src.agents.mrw_explorer D    # Daily analysis (1 research brief)
python -m src.agents.mrw_explorer W    # Weekly analysis (1 research brief)
python -m src.agents.mrw_explorer M    # Monthly analysis (3 research briefs)
python -m src.agents.mrw_explorer Q    # Quarterly analysis (3 research briefs)
python -m src.agents.mrw_explorer Y    # Yearly analysis (5 research briefs)

# Opponent CEO Agent - Competitive intelligence from rival CEOs
python -m src.agents.opp_ceo_agent_topic_generator  # Demo mode (configurable: ZaloPay or VNPay CEO)

# Mr Tường Defensive Agent - Generate defensive strategy against opponent attacks
python -m src.agents.mrt_defensive_agent  # Demo mode (reads latest opponent attacks)

# MrT Ranking Agent - Evaluate research reports for strategic value
python -m src.agents.mrt_ranking_agent  # Demo mode (ranks all reports in reports/)

# Complete Workflow - Full 5-phase pipeline (resumable)
python -m src.agents.complete_workflow_v2 Y                     # New workflow
python -m src.agents.complete_workflow_v2 list                  # List sessions
python -m src.agents.complete_workflow_v2 resume <session_id>   # Resume from failure

# Run individual components for testing
python -m src.agents.clarifier          # Test clarification phase
python -m src.agents.supervisor         # Test supervisor coordination
python -m src.agents.researcher         # Test individual researcher
python -m src.agents.topics_generator   # Test MrT topic generation (generates research briefs)
python -m src.agents.question_generator # Test MrT question generation (generates strategic questions)
python -m src.agents.opp_ceo_agent_topic_generator  # Test opponent CEO (ZaloPay/VNPay)
python -m src.agents.mrt_defensive_agent  # Test Mr Tường defensive agent
python -m src.agents.mrt_ranking_agent  # Test MrT ranking agent (evaluates reports 0-10)

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
│   ├── agents/                # AI agent implementations
│   │   ├── clarifier.py           # Research brief creation
│   │   ├── researcher.py          # Individual research agent
│   │   ├── supervisor.py          # Multi-agent coordination
│   │   ├── topics_generator.py    # MrT persona: generates research briefs from market trends
│   │   ├── question_generator.py  # MrT persona: generates strategic questions from topics
│   │   ├── mrw_explorer.py        # Automated pipeline: topics → sequential deep research
│   │   ├── opp_ceo_agent_topic_generator.py  # Opponent CEOs: ZaloPay/VNPay competitive intelligence
│   │   ├── mrt_defensive_agent.py # Mr Tường: defensive strategy against opponent attacks
│   │   ├── mrt_ranking_agent.py   # MrT: evaluate research reports 0-10 for strategic value
│   │   ├── brief_filter_agent.py  # LLM-based brief deduplication
│   │   ├── complete_workflow_v2.py # Resumable 5-phase workflow (with state tracking)
│   │   └── base_ceo_agent.py      # Base class for all CEO persona agents
│   ├── core/                  # Core orchestration systems
│   │   ├── deep_research_system.py # Main orchestration system
│   │   └── insight_generator.py   # HTML insight page generation
│   ├── prompts/               # All system prompts
│   │   ├── system_prompts.py     # Core system prompts
│   │   └── persona_prompts.py    # CEO persona prompts (MrT, ZaloPay, VNPay)
│   └── utils/                 # Utilities and helpers
│       ├── helpers.py            # Helper functions and tools
│       ├── cache_strategy.py     # LLM caching strategies
│       └── config.py             # Configuration and settings
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
├── .output/                   # Agent-generated outputs (gitignored)
│   ├── mrT_topics_*.md       # Timestamped MrT research briefs
│   ├── opponent_{ceo_type}_attacks_*.md  # Timestamped opponent CEO attack strategies
│   ├── mrt_defensive_vs_{opponent}_*.md  # Timestamped Mr Tường defensive briefs
│   ├── mrt_rankings_*.md     # Timestamped MrT report rankings (0-10 scores)
│   └── logs/                 # Debug logs (if enabled)
├── sample_codes/              # Reference code (not part of main system)
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies
└── CLAUDE.md                 # This file
```

## Architecture Overview

This is a multi-agent deep research system built with LangChain (without LangGraph).

### Core Research Pipeline (4 phases)

**Phase 1: Clarification** (`src/agents/clarifier.py`)
- `ResearchBriefCreator` class interacts with users to clarify research intent
- Transforms user input into structured research briefs
- Can be skipped when using MrT-generated briefs

**Phase 2: Supervised Research** (`src/agents/supervisor.py`)
- `Supervisor` coordinates multiple parallel research agents
- Uses lead researcher prompt to plan and delegate tasks
- Launches up to 5 concurrent `Researcher` agents (configurable)
- Each researcher has 4 iterations using Tavily search + think tool

**Phase 3: Report Generation** (`src/core/deep_research_system.py`)
- `DeepResearch` orchestrates the entire pipeline
- Collects research notes from all agents
- Generates comprehensive final report
- Automatically saves to `./reports/` with timestamp-based filenames

**Phase 4: Insight Page Generation** (`src/core/insight_generator.py`)
- `InsightGenerator` creates interactive HTML insight pages
- Generates concise 2-4 page visual summaries with charts/tabs
- Uses Claude Code SDK (optional dependency)
- Saves to `./reports/htmls/` with timestamp-based filenames

### MrT Generator Pipeline (NEW)

Automated research pipeline that simulates CEO "Nguyễn Mạnh Tường" (MoMo CEO) to generate strategic research topics and execute research autonomously.

**MrT Topics Generator** (`src/agents/topics_generator.py`)
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

**MrT Question Generator** (`src/agents/question_generator.py`)
- Uses MrT persona to generate strategic questions from topics
- Focuses on: financial inclusion, innovation, business growth, regulatory impact
- Uses think tool + Tavily search to research before generating questions
- Outputs structured questions using Pydantic models

**MrW Explorer** (`src/agents/mrw_explorer.py`)
- **Automated end-to-end pipeline**: generates topics → runs deep research sequentially
- Combines `TopicsGenerator` + `DeepResearch`
- **Key feature**: Creates fresh `DeepResearch` instance for each topic to avoid state issues
- Executes research on each generated brief **sequentially** (NOT parallel for stability)
- Automatically saves all reports to `./reports/` with numbered filenames
- Displays comprehensive summary table with success/failure tracking
- Usage: `python -m src.agents.mrw_explorer [D|W|M|Q|Y]`

### Opponent CEO Agent (NEW)

Simulates competitor CEOs (ZaloPay/VNPay) conducting competitive intelligence on MoMo to generate attack strategies.

**Opponent CEO Topic Generator** (`src/agents/opp_ceo_agent_topic_generator.py`)
- Simulates two CEO personas (configurable via CEO_TYPE constant):
  - **ZaloPay CEO (Chi Le)**: Leverages Zalo ecosystem (100M+ users), social payments, Gen Z focus
  - **VNPay CEO (Lê Tánh)**: Leverages 40+ banking partnerships, merchant network, enterprise solutions
- Uses THREE tools for competitive intelligence:
  - `query_momo_data`: Analyzes MoMo's internal metrics (GMV, users, products) to find weaknesses
  - `tavily_search`: Researches public market trends, competitor moves, customer sentiment
  - `think_tool`: Synthesizes intelligence to identify strategic attack vectors
- Generates **executive exploitation plans** (not just briefs) to attack MoMo's weaknesses
- Each plan includes: identified weakness (data-backed), exploitation approach, execution steps (3-5), expected impact, success metrics
- Number of strategies configurable via `NUM_STRATEGIES` constant (default: 3)
- Saves to `.output/opponent_{ceo_type}_attacks_*.md`

**Mr Tường Defensive Agent** (`src/agents/mrt_defensive_agent.py`)
- Reads opponent CEO attack strategies as input
- **NOT one-to-one mapping**: Mr Tường decides how many defensive briefs to create based on strategic concerns
- Uses `tavily_search` to research market dynamics and `think_tool` for strategic analysis
- Generates defensive research briefs for deep research system
- Each brief includes: research objective, strategic context, investigation areas, expected insights
- Saves to `.output/mrt_defensive_vs_{opponent}_*.md`
- Complete pipeline: Opponent attacks → Mr Tường defensive briefs → Deep research reports

**MrT Ranking Agent** (`src/agents/mrt_ranking_agent.py`)
- Evaluates final research reports for strategic value
- Rates each report 0-10 on five criteria:
  - Strategic Relevance (0-10): Alignment with MoMo's priorities
  - Actionability (0-10): Can insights drive business decisions?
  - Insight Depth (0-10): Non-obvious insights vs surface analysis
  - Data Quality (0-10): Evidence-backed conclusions
  - Competitive Advantage (0-10): Edge over competitors
- Provides justification, strengths, improvements, priority (HIGH/MEDIUM/LOW), and recommended actions
- Auto-discovers reports in `reports/` directory or accepts specific file paths
- Saves rankings to `.output/mrt_rankings_*.md` with summary statistics and detailed assessments
- **NOT a BaseCEOAgent**: Simpler agent for evaluation only (no tool-calling loop needed)

**Complete Workflow Orchestrator** (`src/agents/complete_workflow_v2.py`)
- Full state tracking with resume capability
- Runs all 5 phases: MrT Topics → Opponent Attacks → Defensive → Filtering → Deep Research → Ranking
- Saves progress after each step to `.output/workflow_states/{session_id}.json`
- Granular Phase 3 tracking: Saves after each brief completion (longest phase)
- Idempotent: Checks if step already completed before executing
- **Agent independence**: Calls agents via `.generate()`, handles formatting/saving in workflow
- Usage:
  - New run: `python -m src.agents.complete_workflow_v2 [D|W|M|Q|Y]`
  - List sessions: `python -m src.agents.complete_workflow_v2 list`
  - Resume: `python -m src.agents.complete_workflow_v2 resume <session_id>`
- State file persists: session_id, current_phase (0, 1, 2, 2.5, 3, 4), completed_steps, file_paths, pending_briefs

## Key Components

- **Cache Strategy**: `src/utils/cache_strategy.py` implements caching for Anthropic models to optimize token usage
  - `AnthropicCacheStrategy` for Claude models uses prompt caching
  - `StandardCacheStrategy` for other models (no caching)
  - `CacheStrategyFactory` automatically selects appropriate strategy
- **Prompts**: All system prompts organized in `src/prompts/`
  - `system_prompts.py`: Lead researcher, clarifier, final report generation prompts
  - `persona_prompts.py`: CEO persona prompts (MrT, ZaloPay CEO, VNPay CEO, Mr Tường defensive)
- **Utils**: Helper functions in `src/utils/helpers.py` for formatting, logging, and tool management
  - Tavily search tool wrapper
  - Think tool for researcher reflection
  - Message formatting utilities
  - xAI model initialization with custom timeout
- **Reports Directory**: `./reports/` stores saved research reports (gitignored)
  - Auto-generated filenames: `{description}_{YYYYMMDD_HHMM}.md`
  - HTML insight pages: `./reports/htmls/insights_{description}_{YYYYMMDD_HHMM}.html`
- **Insight Generator**: `src/core/insight_generator.py` creates interactive HTML summaries
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
  - Boss Model (all CEO personas): `BOSS_MODEL = grok-4-fast-reasoning` (0.0 temp)
  - Clarifier: `grok-4-fast` (0.0 temp)
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
  - Supervisor: 6 iterations (`SUPERVISOR_MAX_RESEARCHER_ITERATIONS`)
  - Each Researcher: 4 iterations (`RESEARCHER_MAX_TOOL_CALL_ITERATIONS`)
  - Question Generator: 3 iterations (`QUESTION_GENERATOR_MAX_TOOL_CALL_ITERATIONS`)
  - Topics Generator: 5 iterations (hardcoded in MrW Explorer)
  - Opponent CEO Agent: 6 iterations (default in agent initialization)
- **Concurrent researchers**: Up to 5 can be launched in parallel (`SUPERVISOR_MAX_CONCURRENT_RESEARCHERS`)
- **Reports**: Automatically saved with descriptive filenames based on user input
  - Research reports: `./reports/{description}_{timestamp}.md`
  - Insight pages: `./reports/htmls/insights_{description}_{timestamp}.html`
  - MrT topics: `.output/mrT_topics_{timestamp}.md`
  - Opponent CEO briefs: `.output/opponent_{ceo_type}_briefs_{timestamp}.md`
- **Educational version**: `educational_no_logging/` has identical logic but cleaner presentation
- **Insight generation**: Uses `permission_mode='acceptAll'` to allow Claude full access to all tools
- **Performance tracking**: Automatically tracks time and token usage for each phase with summary table
- **Timeout configuration**: All LLM requests use 240 seconds to prevent timeouts during long operations
- **MrT Pipeline**: The `mrw_explorer` runs research **sequentially** (not parallel) to avoid overwhelming the system
- **Opponent CEO Agent**:
  - Uses MirMir tool (`query_momo_data`) to analyze MoMo's internal data for competitive intelligence
  - Requires MirMir API server running on `localhost:8001` (configurable via `MIRMIR_API_SERVER_BASE_URL`)
  - Configurable via `CEO_TYPE` constant in `src/opp_ceo_agent_topic_generator.py` (line 31)
  - Debug logging option available via `debug_log` parameter (saves to `.output/logs/`)