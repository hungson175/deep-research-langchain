"""
Cache Strategy Module for Message Caching

Implements Strategy pattern for handling message caching across different LLM providers.
Following SOLID principles:
- Single Responsibility: Each strategy handles one caching approach
- Open/Closed: Can add new strategies without modifying existing code
- Liskov Substitution: All strategies implement the same interface
- Interface Segregation: Simple focused interface
- Dependency Inversion: Depend on abstractions, not concrete implementations
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union
from langchain_core.messages import BaseMessage, SystemMessage, HumanMessage, ToolMessage


class MessageCacheStrategy(ABC):
    """Abstract base class for message caching strategies."""

    @abstractmethod
    def prepare_system_message(self, content: str) -> SystemMessage:
        """Prepare a system message with appropriate caching."""
        pass

    @abstractmethod
    def prepare_human_message(self, content: str, add_cache: bool = False) -> HumanMessage:
        """Prepare a human message with optional caching."""
        pass

    @abstractmethod
    def prepare_tool_message(self, content: str, tool_call_id: str, add_cache: bool = False) -> ToolMessage:
        """Prepare a tool message with optional caching."""
        pass

    @abstractmethod
    def prepare_messages_for_invoke(self, messages: List[BaseMessage], cache_last: bool = False) -> List[BaseMessage]:
        """Prepare messages before invoking the model."""
        pass

    @abstractmethod
    def cleanup_messages_after_invoke(self, messages: List[BaseMessage]) -> List[BaseMessage]:
        """Clean up messages after invoking the model."""
        pass


class AnthropicCacheStrategy(MessageCacheStrategy):
    """Cache strategy for Anthropic models supporting ephemeral caching."""

    def prepare_system_message(self, content: str) -> SystemMessage:
        """Create system message with Anthropic cache control."""
        return SystemMessage(
            content=[
                {
                    "type": "text",
                    "text": content,
                    "cache_control": {"type": "ephemeral"}
                }
            ]
        )

    def prepare_human_message(self, content: str, add_cache: bool = False) -> HumanMessage:
        """Create human message with optional Anthropic cache control."""
        if add_cache:
            return HumanMessage(
                content=[
                    {
                        "type": "text",
                        "text": content,
                        "cache_control": {"type": "ephemeral"}
                    }
                ]
            )
        return HumanMessage(content=content)

    def prepare_tool_message(self, content: str, tool_call_id: str, add_cache: bool = False) -> ToolMessage:
        """Create tool message with optional Anthropic cache control."""
        if add_cache:
            return ToolMessage(
                content=[
                    {
                        "type": "text",
                        "text": content,
                        "cache_control": {"type": "ephemeral"}
                    }
                ],
                tool_call_id=tool_call_id
            )
        return ToolMessage(content=content, tool_call_id=tool_call_id)

    def prepare_messages_for_invoke(self, messages: List[BaseMessage], cache_last: bool = False) -> List[BaseMessage]:
        """Add cache control to the last message if needed."""
        if not cache_last or not messages:
            return messages

        # Work with a copy to avoid modifying original
        messages_copy = messages.copy()
        last_msg = messages_copy[-1]

        # Add cache control to last message
        if isinstance(last_msg, (HumanMessage, ToolMessage)):
            if isinstance(last_msg.content, str):
                last_msg.content = [
                    {
                        "type": "text",
                        "text": last_msg.content,
                        "cache_control": {"type": "ephemeral"}
                    }
                ]
            elif isinstance(last_msg.content, list) and last_msg.content:
                # Ensure cache control on last content item
                if isinstance(last_msg.content[-1], dict):
                    last_msg.content[-1]["cache_control"] = {"type": "ephemeral"}

        return messages_copy

    def cleanup_messages_after_invoke(self, messages: List[BaseMessage]) -> List[BaseMessage]:
        """Remove cache control from messages after invoke."""
        for msg in messages:
            if isinstance(msg, (SystemMessage, HumanMessage, ToolMessage)):
                if isinstance(msg.content, list):
                    for item in msg.content:
                        if isinstance(item, dict) and "cache_control" in item:
                            item.pop("cache_control", None)
        return messages


class NoCacheStrategy(MessageCacheStrategy):
    """Default strategy for models that don't support caching."""

    def prepare_system_message(self, content: str) -> SystemMessage:
        """Create standard system message without caching."""
        return SystemMessage(content=content)

    def prepare_human_message(self, content: str, add_cache: bool = False) -> HumanMessage:
        """Create standard human message without caching."""
        return HumanMessage(content=content)

    def prepare_tool_message(self, content: str, tool_call_id: str, add_cache: bool = False) -> ToolMessage:
        """Create standard tool message without caching."""
        return ToolMessage(content=content, tool_call_id=tool_call_id)

    def prepare_messages_for_invoke(self, messages: List[BaseMessage], cache_last: bool = False) -> List[BaseMessage]:
        """Return messages as-is for models without caching."""
        return messages

    def cleanup_messages_after_invoke(self, messages: List[BaseMessage]) -> List[BaseMessage]:
        """No cleanup needed for models without caching."""
        return messages


class CacheStrategyFactory:
    """Factory for creating appropriate cache strategies based on model type."""

    @staticmethod
    def create_strategy(model_name: str) -> MessageCacheStrategy:
        """
        Create appropriate cache strategy based on model name.

        Args:
            model_name: Name of the model (e.g., "anthropic:claude-sonnet-4-20250514")

        Returns:
            Appropriate cache strategy instance
        """
        if model_name.startswith("anthropic:") or "claude" in model_name.lower():
            return AnthropicCacheStrategy()
        else:
            return NoCacheStrategy()