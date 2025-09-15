"""
Utility Functions and Tools for Deep Research System
=====================================================
Helper functions, cache strategies, and search tools.
"""

from datetime import datetime
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from tavily import TavilyClient


def get_today_str() -> str:
    """Get current date in human-readable format."""
    return datetime.now().strftime("%a %b %-d, %Y")


# ===========================
# CACHE STRATEGIES
# ===========================

class MessageCacheStrategy:
    """Base cache strategy - no caching."""

    def prepare_system_message(self, content: str) -> SystemMessage:
        return SystemMessage(content=content)

    def prepare_human_message(self, content: str, add_cache: bool = False) -> HumanMessage:
        return HumanMessage(content=content)

    def prepare_tool_message(self, content: str, tool_call_id: str, add_cache: bool = False) -> ToolMessage:
        return ToolMessage(content=content, tool_call_id=tool_call_id)

    def cleanup_messages_after_invoke(self, messages: list) -> list:
        return messages


class AnthropicCacheStrategy(MessageCacheStrategy):
    """Cache strategy for Anthropic models using cache_control."""

    def prepare_system_message(self, content: str) -> SystemMessage:
        return SystemMessage(
            content=[{"type": "text", "text": content, "cache_control": {"type": "ephemeral"}}]
        )

    def prepare_human_message(self, content: str, add_cache: bool = False) -> HumanMessage:
        if add_cache:
            return HumanMessage(
                content=[{"type": "text", "text": content, "cache_control": {"type": "ephemeral"}}]
            )
        return HumanMessage(content=content)

    def prepare_tool_message(self, content: str, tool_call_id: str, add_cache: bool = False) -> ToolMessage:
        if add_cache:
            return ToolMessage(
                content=[{"type": "text", "text": content, "cache_control": {"type": "ephemeral"}}],
                tool_call_id=tool_call_id
            )
        return ToolMessage(content=content, tool_call_id=tool_call_id)

    def cleanup_messages_after_invoke(self, messages: list) -> list:
        """Remove cache_control from messages after invoke."""
        cleaned = []
        for msg in messages:
            if isinstance(msg, (SystemMessage, HumanMessage, ToolMessage)):
                if isinstance(msg.content, list):
                    clean_content = []
                    for item in msg.content:
                        if isinstance(item, dict) and "cache_control" in item:
                            clean_item = item.copy()
                            del clean_item["cache_control"]
                            clean_content.append(clean_item)
                        else:
                            clean_content.append(item)

                    if isinstance(msg, SystemMessage):
                        cleaned.append(SystemMessage(content=clean_content))
                    elif isinstance(msg, HumanMessage):
                        cleaned.append(HumanMessage(content=clean_content))
                    elif isinstance(msg, ToolMessage):
                        cleaned.append(ToolMessage(content=clean_content, tool_call_id=msg.tool_call_id))
                else:
                    cleaned.append(msg)
            else:
                cleaned.append(msg)
        return cleaned


class CacheStrategyFactory:
    """Factory for creating appropriate cache strategies."""

    @staticmethod
    def create_strategy(model_name: str) -> MessageCacheStrategy:
        if "anthropic" in model_name.lower() or "claude" in model_name.lower():
            return AnthropicCacheStrategy()
        return MessageCacheStrategy()


# ===========================
# SEARCH TOOLS
# ===========================

tavily_client = TavilyClient()
summarization_model = init_chat_model(model="xai:grok-code-fast-1")


class Summary(BaseModel):
    summary: str = Field(description="Concise summary of the webpage content")
    key_excerpts: str = Field(description="Important quotes and excerpts")


def summarize_webpage(content: str) -> str:
    """Summarize webpage content."""
    try:
        structured_model = summarization_model.with_structured_output(Summary)
        summary = structured_model.invoke([
            HumanMessage(content=f"Summarize this webpage content:\n{content}\nDate: {get_today_str()}")
        ])
        return f"<summary>\n{summary.summary}\n</summary>\n\n<key_excerpts>\n{summary.key_excerpts}\n</key_excerpts>"
    except:
        return content[:1000] + "..." if len(content) > 1000 else content


@tool(parse_docstring=True)
def tavily_search(query: str, max_results: int = 3) -> str:
    """Search the web using Tavily API.

    Args:
        query: Search query
        max_results: Max number of results

    Returns:
        Formatted search results
    """
    result = tavily_client.search(query, max_results=max_results, include_raw_content=True)

    output = "Search results:\n\n"
    for i, res in enumerate(result['results'], 1):
        content = summarize_webpage(res['raw_content']) if res.get('raw_content') else res['content']
        output += f"--- SOURCE {i}: {res['title']} ---\n"
        output += f"URL: {res['url']}\n\n"
        output += f"SUMMARY:\n{content}\n\n"
        output += "-" * 80 + "\n"

    return output


@tool(parse_docstring=True)
def think_tool(reflection: str) -> str:
    """Reflect on research progress and plan next steps.

    Args:
        reflection: Your analysis of findings and next steps

    Returns:
        Confirmation
    """
    return f"Reflection recorded: {reflection}"