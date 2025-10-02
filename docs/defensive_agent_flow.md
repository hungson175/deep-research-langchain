# Defensive Agent Flow - Mr Tường vs Opponent CEOs

## Overview

Complete pipeline for competitive intelligence and defensive strategy generation:

```
Opponent CEO Agent → Attack Strategies → Mr Tường Defensive Agent → Research Briefs → Deep Research
```

## Components

### 1. Opponent CEO Agent
**File**: `src/agents/opp_ceo_agent_topic_generator.py`

**Personas**:
- ZaloPay CEO (Chi Le)
- VNPay CEO (Lê Tánh)

**Output**: Executive exploitation plans (3 by default, configurable via `NUM_STRATEGIES`)
- Identified MoMo weakness (data-backed)
- Exploitation approach
- Execution steps (3-5 actions)
- Expected impact (quantifiable)
- Success metrics

**Saved to**: `.output/opponent_{ceo_type}_attacks_{timestamp}.md`

**Run**: `python -m src.agents.opp_ceo_agent_topic_generator`

---

### 2. Mr Tường Defensive Agent (NEW)
**File**: `src/agents/mrt_defensive_agent.py`

**Persona**: Nguyễn Mạnh Tường (MoMo CEO)

**Input**: Opponent's attack strategies (list of strings)

**Process**:
1. Reads opponent attack strategies
2. Uses `tavily_search` to research market dynamics
3. Uses `think_tool` to identify strategic concerns
4. Generates defensive research briefs (Mr Tường decides quantity based on strategic importance)

**Output**: Defensive research briefs
- Research Objective
- Strategic Context (why it matters for MoMo's defense)
- Investigation Areas
- Expected Insights

**Key Feature**: NOT one-to-one mapping! Mr Tường decides which concerns matter most based on his strategic thinking.

**Saved to**: `.output/mrt_defensive_vs_{opponent}_{timestamp}.md`

**Run**: `python -m src.agents.mrt_defensive_agent`

---

### 3. Deep Research System
**File**: `src/core/deep_research_system.py`

**Input**: Research briefs (from Mr Tường or any source)

**Output**: Comprehensive research reports

**Run**: `python main.py` (or programmatically)

---

## Complete Flow Example

### Step 1: Generate Opponent Attack Strategies
```bash
# Configure opponent in src/agents/opp_ceo_agent_topic_generator.py
CEO_TYPE = "zalopay"  # or "vnpay"
NUM_STRATEGIES = 3

# Run opponent CEO
python -m src.agents.opp_ceo_agent_topic_generator
```

**Output**: `.output/opponent_zalopay_attacks_20251002_1800.md`

---

### Step 2: Generate Mr Tường's Defensive Briefs
```bash
# Mr Tường reads latest opponent file and generates defensive briefs
python -m src.agents.mrt_defensive_agent
```

**Output**: `.output/mrt_defensive_vs_zalopay_20251002_1805.md`

---

### Step 3: Deep Research on Defensive Briefs
```python
from src.core.deep_research_system import DeepResearch

# Read Mr Tường's defensive brief
with open('.output/mrt_defensive_vs_zalopay_20251002_1805.md', 'r') as f:
    content = f.read()
    # Extract first brief
    briefs = content.split("## Defensive Research Brief")
    first_brief = briefs[1] if len(briefs) > 1 else content

# Run deep research
research = DeepResearch()
await research.run(
    user_input="MrT Defensive Brief 1",
    skip_clarifier=True,
    research_brief=first_brief,
    save_to_file=True
)
```

**Output**: `./reports/mrt_defensive_brief_1_{timestamp}.md`

---

## Configuration

### Boss Models (All CEO Agents)
**File**: `src/utils/config.py`

```python
BOSS_MODEL = "grok-4-fast-reasoning"
BOSS_TEMPERATURE = 0.5  # Updated for more creative strategic thinking
```

Affects:
- MrT Topics Generator
- MrT Question Generator
- ZaloPay CEO (Opponent)
- VNPay CEO (Opponent)
- **Mr Tường Defensive Agent (NEW)**

---

## Key Design Principles

1. **NOT One-to-One Mapping**: Mr Tường doesn't generate one brief per attack strategy. He synthesizes threats and decides which concerns require research.

2. **Strategic Autonomy**: Mr Tường decides:
   - How many research briefs to create
   - Which threats are most important
   - What areas need deep investigation

3. **CEO-Level Thinking**: Both opponent CEOs and Mr Tường use BOSS model with strategic reasoning capabilities.

4. **Complete Research Briefs**: Output is ready for deep research system - no manual formatting needed.

---

## Directory Structure

```
.output/
├── opponent_zalopay_attacks_*.md      # ZaloPay CEO attack plans
├── opponent_vnpay_attacks_*.md        # VNPay CEO attack plans
├── mrt_defensive_vs_zalopay_*.md      # Mr Tường's defensive briefs
├── mrt_defensive_vs_vnpay_*.md        # Mr Tường's defensive briefs
└── logs/                               # Debug logs (if enabled)
    ├── opp_zalopay_briefs_*.md
    ├── opp_vnpay_briefs_*.md
    └── mrt_defensive_*.md

reports/
├── mrt_defensive_brief_1_*.md         # Deep research reports
└── htmls/
    └── insights_mrt_defensive_*.html  # Insight pages
```

---

## Debug Mode

Enable debug logging for detailed analysis:

```python
# Opponent CEO
agent = OpponentCEOTopicGenerator(
    ceo_type="zalopay",
    max_tool_call_iterations=6,
    debug_log=True  # Enables logging
)

# Mr Tường Defensive
agent = MrTuongDefensiveAgent(
    max_tool_call_iterations=6,
    debug_log=True  # Enables logging
)
```

Logs saved to `.output/logs/`
