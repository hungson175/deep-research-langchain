"""Configuration file for LLM models used in the deep research system."""

CLARIFIER_MODEL = "xai:grok-4-fast"

SUPERVISOR_MODEL = "xai:grok-4-fast-reasoning"
SUPERVISOR_MAX_RESEARCHER_ITERATIONS = 6
SUPERVISOR_MAX_CONCURRENT_RESEARCHERS = 5

RESEARCHER_MODEL = "xai:grok-4-fast-reasoning"
RESEARCHER_MAX_TOOL_CALL_ITERATIONS = 5

SUMMARIZATION_MODEL = "xai:grok-4-fast"

WRITER_MODEL = "xai:grok-4-fast-reasoning"
# WRITER_MODEL = "anthropic:claude-sonnet-4-20250514"

MIRMIR_API_SERVER_BASE_URL = "http://localhost:8001"
MIRMIR_TIMEOUT_SECONDS = 300