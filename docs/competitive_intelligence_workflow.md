# Competitive Intelligence & Defensive Strategy Workflow

## Overview

This document describes the **Complete Strategic Intelligence Workflow** implemented in the deep research system. The workflow simulates real-world competitive dynamics with FOUR phases:

1. **MrT Topic Generation** - MoMo CEO generates strategic research briefs from market analysis (configurable: 1-5 briefs)
2. **Opponent CEO Attacks** - ZaloPay/VNPay CEOs analyze MoMo to generate exploitation strategies (3 strategies each)
3. **Mr Tường Defensive Response** - MoMo CEO reads attacks and generates defensive research briefs (flexible count)
4. **Deep Research Execution** - Comprehensive research on ALL briefs (MrT topics + defensive briefs)
5. **MrT Report Ranking** - MoMo CEO rates each final report 0-10 for strategic value

## Workflow Architecture

```mermaid
graph LR
    MRT0[Phase 0:<br/>MrT Topics] --> |1-5 briefs| FILTER[Phase 2.5:<br/>Brief Filtering]
    OPP[Phase 1:<br/>Opponent Attacks] --> |3 strategies| DEF[Phase 2:<br/>Defensive Briefs]
    DEF --> |flexible count| FILTER
    FILTER --> |unique briefs| DR[Phase 3:<br/>Deep Research]
    DR --> |reports| RANK[Phase 4:<br/>MrT Ranking]
    RANK --> |0-10 scores| END[Prioritized<br/>Action Items]

    style MRT0 fill:#9370db,stroke:#333,stroke-width:2px,color:#000
    style OPP fill:#ff6b6b,stroke:#333,stroke-width:2px,color:#000
    style DEF fill:#4ecdc4,stroke:#333,stroke-width:2px,color:#000
    style FILTER fill:#ffd700,stroke:#333,stroke-width:2px,color:#000
    style DR fill:#95e1d3,stroke:#333,stroke-width:2px,color:#000
    style RANK fill:#9370db,stroke:#333,stroke-width:2px,color:#000
    style END fill:#a8e6cf,stroke:#333,stroke-width:2px,color:#000
```

## Phase Overview

### Phase 0: MrT Topic Generation
- **Agent**: MrT (MoMo CEO)
- **Purpose**: Analyze market trends → Generate strategic research briefs
- **Output**: 1-5 research briefs (period-dependent: D/W/M/Q/Y)
- **File**: `.output/mrT_topics_*.md`

### Phase 1: Opponent CEO Attacks
- **Agents**: ZaloPay CEO / VNPay CEO
- **Purpose**: Analyze MoMo weaknesses → Generate exploitation strategies
- **Tools**: `query_momo_data`, `tavily_search`, `think_tool`
- **Output**: 3 executive exploitation plans
- **File**: `.output/opponent_{ceo_type}_attacks_*.md`

### Phase 2: Mr Tường Defensive Response
- **Agent**: Mr Tường (MoMo CEO)
- **Purpose**: Read opponent attacks → Generate defensive research briefs
- **Key Feature**: Flexible brief count (NOT 1-to-1 mapping)
- **Output**: Defensive research briefs (quality over quantity)
- **File**: `.output/mrt_defensive_vs_{opponent}_*.md`

### Phase 2.5: Brief Consolidation & Filtering (NEW)
- **Agent**: LLM-based deduplication agent
- **Purpose**: Read all gathered briefs → Filter duplicated/too similar briefs → Consolidate into unique research topics
- **Input**: MrT topics (1-5) + defensive briefs (flexible count)
- **Output**: Filtered list of unique research briefs
- **Process**: Read & think → Identify semantic duplicates → Merge similar briefs → Produce final research queue

### Phase 3: Deep Research Execution
- **System**: DeepResearch (Clarifier → Supervisor → 5 Researchers → Report Writer → Insight Generator)
- **Purpose**: Execute comprehensive research on FILTERED briefs (after deduplication)
- **Output**: Vietnamese research reports + HTML insights
- **Files**: `reports/*.md`, `reports/htmls/*.html`

### Phase 4: MrT Report Ranking
- **Agent**: MrT (MoMo CEO)
- **Purpose**: Evaluate all research reports for strategic value
- **Criteria**: 5 dimensions (0-10 each) → Overall score → Priority (HIGH/MEDIUM/LOW)
- **Output**: Ranked report list with justifications and recommendations
- **File**: `.output/mrt_rankings_*.md`

## Data Flow

```mermaid
sequenceDiagram
    participant MRT as MrT Topics
    participant OPP as Opponent CEOs
    participant DEF as Defensive
    participant DR as Deep Research
    participant RANK as Ranking

    Note over MRT: Phase 0
    MRT->>DR: 1-5 research briefs

    Note over OPP,DEF: Phase 1-2
    OPP->>DEF: 3 attack strategies
    DEF->>DR: Flexible defensive briefs

    Note over DR: Phase 3
    DR->>DR: 5 researchers × 4 iterations
    DR->>RANK: Vietnamese reports + HTML

    Note over RANK: Phase 4
    RANK->>RANK: Evaluate 5 criteria (0-10)
    RANK->>RANK: Priority: HIGH/MEDIUM/LOW
```

## Running the Complete Pipeline

```bash
# Full 5-phase workflow
python -m src.agents.topics_generator              # Phase 0: Generate MrT topics
python -m src.agents.opp_ceo_agent_topic_generator # Phase 1: Opponent attacks
python -m src.agents.mrt_defensive_agent           # Phase 2: Defensive briefs
python main.py                                      # Phase 3: Deep research
python -m src.agents.mrt_ranking_agent             # Phase 4: Rank reports

# Or use automated pipeline for Phase 0+3
python -m src.agents.mrw_explorer Y                # MrT topics → Deep research (5 briefs)
python -m src.agents.mrt_ranking_agent             # Then rank the reports
```

## Key Design Principles

1. **Realistic Competitive Dynamics**: Opponents exploit weaknesses, Mr Tường prioritizes strategically (not 1-to-1)
2. **Data-Driven Intelligence**: Real MoMo data + market research + strategic synthesis
3. **CEO Persona Authenticity**: Distinct backgrounds, strategies, and competitive advantages
4. **Flexible Output**: Adaptive brief counts based on strategic importance
5. **Quality over Quantity**: Focus on actionable insights, not volume

## File Organization

```
.output/                          # Agent outputs
├── mrT_topics_*.md              # MrT research briefs
├── opponent_{ceo}_attacks_*.md  # Opponent exploitation plans
├── mrt_defensive_vs_*.md        # Defensive briefs
├── mrt_rankings_*.md            # Report rankings
└── logs/                        # Debug logs (optional)

reports/                          # Final research outputs
├── *.md                         # Vietnamese reports
└── htmls/*.html                 # Interactive insights
```

## Pseudo-Code Overview

### Version 1: Simple (No Resume)

```python
def run_complete_workflow(period="Y"):
    # Phase 0: MrT generates 1-5 research briefs
    mrt_topics = TopicsGenerator().generate(period)

    # Phase 1: Opponent CEOs generate attack strategies
    zalopay_attacks = OpponentCEO("zalopay").generate()
    vnpay_attacks = OpponentCEO("vnpay").generate()

    # Phase 2: Mr Tường generates defensive briefs
    defensive_vs_zalopay = MrTDefensive().generate(zalopay_attacks)
    defensive_vs_vnpay = MrTDefensive().generate(vnpay_attacks)

    # Phase 2.5: Filter duplicates
    all_briefs = mrt_topics + defensive_vs_zalopay + defensive_vs_vnpay
    filtered_briefs = BriefFilter().filter(all_briefs)

    # Phase 3: Deep research each brief
    reports = [DeepResearch().run(brief) for brief in filtered_briefs]

    # Phase 4: MrT ranks reports 0-10
    rankings = MrTRanking().rank(reports)

    return {briefs, reports, rankings}
```

### Version 2: With Resume Capability

Pseudo-code (not python !):
```python
class WorkflowState:
    session_id: str
    current_phase: float  # 0, 1, 2, 2.5, 3, 4
    completed_steps: List[str]
    file_paths: Dict  # All output file paths
    pending_briefs: List[dict]  # For Phase 3 tracking

def run_resumable_workflow(period="Y", session_id=None):
    # Load or create state
    state = load_state(session_id) if session_id else WorkflowState()

    # Each phase checks: if state.current_phase <= X
    # Execute phase → Save outputs → Update state → save_state()

    # Phase 3 special: Track individual brief completion
    while state.pending_briefs:
        brief = state.pending_briefs[0]
        report = DeepResearch().run(brief)
        state.completed_reports.append(report)
        state.pending_briefs.pop(0)
        save_state(state)  # Save after each brief

    return state
```

**Key Design:**
- **State file**: `.output/workflow_states/{session_id}.json`
- **Idempotent**: Each phase checks if already done before executing
- **Granular Phase 3**: Saves after each brief (longest phase)
- **Auto-resume**: `run_resumable_workflow(session_id="xxx")`

**When to use:**
- Version 1: Quick runs, 1-3 briefs
- Version 2: Production, 5+ briefs, long-running

## Related Documentation

- [Refactoring Summary](./refactoring_summary.md) - Base class architecture
- [CLAUDE.md](../CLAUDE.md) - Complete system overview
- [MrT Generator](./MrT_generator.md) - MrT persona documentation
- [CEO Persona Prompts](../src/prompts/persona_prompts.py) - All CEO prompt templates
