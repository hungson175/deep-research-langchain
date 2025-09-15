# Deep Research System - Educational Version

This is a simplified, consolidated version of the Deep Research System for educational purposes. All logging and visual formatting have been removed to make the code easier to read and understand.

## File Structure

- `deep_research_system_complete.py` - Complete system in a single file containing all classes and modules

## Key Components

### 1. ResearchBriefCreator
- Interacts with users to clarify research intent
- Transforms user input into structured research briefs
- Uses structured output with Pydantic models

### 2. Supervisor
- Coordinates multiple parallel research agents
- Uses lead researcher prompt to plan and delegate tasks
- Can launch up to 3 concurrent researchers
- Has 6 iterations to complete research

### 3. Researcher
- Individual agents that conduct web searches
- Uses Tavily API for web search
- Has think_tool for strategic reflection
- Maximum 3 iterations per researcher
- Compresses findings at the end

### 4. DeepResearch (Main Orchestrator)
- Manages the three-phase research pipeline
- Phase 1: Clarification
- Phase 2: Supervised Research
- Phase 3: Report Generation
- Saves reports to markdown files

## Architecture Flow

```
User Input
    ↓
ResearchBriefCreator (Clarification)
    ↓
Supervisor (Coordination)
    ↓
Multiple Researchers (Parallel Search)
    ↓
Report Generation
    ↓
Markdown File Output
```

## Models Used

- **Clarifier**: `xai:grok-code-fast-1`
- **Supervisor**: `xai:grok-code-fast-1`
- **Researcher**: `xai:grok-code-fast-1`
- **Report Writer**: `anthropic:claude-sonnet-4-20250514`

## Cache Strategy

The system implements intelligent caching for Anthropic models using `cache_control` to optimize token usage. Other models use a standard message strategy without caching.

## Running the System

```python
import asyncio
from deep_research_system_complete import DeepResearch

async def main():
    system = DeepResearch()
    report = await system.run("Your research query here")
    print(report)

asyncio.run(main())
```

## Environment Variables Required

Create a `.env` file with:
```
ANTHROPIC_API_KEY=your_key_here
XAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

## Key Features

1. **Multi-agent Architecture**: Parallel research execution for comprehensive coverage
2. **Intelligent Caching**: Reduces API costs for Anthropic models
3. **Structured Output**: Uses Pydantic models for reliable response formatting
4. **Automatic Report Saving**: Saves reports with descriptive filenames
5. **Web Search Integration**: Uses Tavily API for current information
6. **Strategic Thinking**: Think tool for research planning and reflection

## Educational Notes

This version is optimized for learning and understanding the system architecture. For production use, refer to the main codebase which includes:
- Rich console formatting
- Progress indicators
- Detailed logging
- Error handling
- Visual feedback

The core logic remains identical between both versions.