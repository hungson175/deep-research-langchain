# Deep Research System (LangChain)

A multi-agent AI research system that conducts comprehensive research on any topic using coordinated LLM agents.

## About This Project

This implementation is based on the excellent [Deep Research with LangGraph](https://academy.langchain.com/courses/take/deep-research-with-langgraph) course by LangChain Academy. The original course provides great insights into building LLM-powered research systems, but uses LangGraph which can be complex for beginners.

This version:
- **Simplified Architecture** - Uses pure LangChain without LangGraph for easier understanding
- **Token Optimization** - Added caching strategies for Anthropic models to reduce costs
- **Beginner-Friendly** - More straightforward code structure while maintaining the same powerful capabilities

## Quick Start

### 1. Set Up Python Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Set Up API Keys
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
- **ANTHROPIC_API_KEY** - Required for final report generation
- **XAI_API_KEY** - Required for research coordination
- **TAVILY_API_KEY** - Required for web search

### 3. Run Your First Research
```bash
python deep_research_system.py
```

Or use it in your code:
```python
import asyncio
from deep_research_system import DeepResearch

async def main():
    system = DeepResearch()

    # Ask any research question
    report = await system.run("Compare Deep Research products from OpenAI vs Google")

    print(report)

if __name__ == "__main__":
    asyncio.run(main())
```

## How It Works

The system operates in three phases:

1. **Clarification** - Understands your research intent and creates a research brief
2. **Research** - Multiple AI agents search and analyze information in parallel
3. **Report Generation** - Synthesizes findings into a comprehensive report with citations

## Features

- 🤖 **Multi-Agent Architecture** - Supervisor coordinates specialized research agents
- 🔍 **Web Search Integration** - Real-time information gathering via Tavily
- 📝 **Structured Reports** - Professional reports with proper citations
- 🚀 **Parallel Processing** - Multiple agents work simultaneously for faster results
- 💬 **Interactive Clarification** - Ensures research meets your exact needs

## Project Structure

```
├── deep_research_system.py  # Main entry point
├── clarifier.py             # User intent clarification
├── supervisor.py            # Research coordination
├── researcher.py            # Individual research agents
├── prompts.py              # System prompts
├── cache_strategy.py       # Token optimization
└── utils.py               # Helper functions
```

## Requirements

- Python 3.13+
- API Keys for Anthropic, XAI, and Tavily services

## Example Research Topics

- "Compare the latest AI models from major tech companies"
- "Analyze trends in renewable energy investments for 2024"
- "Research the impact of remote work on productivity"
- "Investigate quantum computing breakthroughs in the last year"

## Support

For issues or questions, please open an issue on GitHub.