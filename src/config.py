"""Configuration file for LLM models used in the deep research system."""

# Boss Model - Used by all CEO persona agents (MrT, ZaloPay CEO, VNPay CEO)
# for strategic thinking and topic generation
BOSS_MODEL = "grok-4-fast-reasoning"
BOSS_TEMPERATURE = 0.0

CLARIFIER_MODEL = "grok-4-fast"
CLARIFIER_TEMPERATURE = 0.0

QUESTION_GENERATOR_MODEL = "grok-4-fast-reasoning"  # Legacy - use BOSS_MODEL instead
QUESTION_GENERATOR_TEMPERATURE = 0.0
QUESTION_GENERATOR_MAX_TOOL_CALL_ITERATIONS = 3

SUPERVISOR_MODEL = "grok-4-fast-reasoning"
SUPERVISOR_TEMPERATURE = 0.0
SUPERVISOR_MAX_RESEARCHER_ITERATIONS = 6
SUPERVISOR_MAX_CONCURRENT_RESEARCHERS = 5

RESEARCHER_MODEL = "grok-4-fast"
RESEARCHER_TEMPERATURE = 0.0
RESEARCHER_MAX_TOOL_CALL_ITERATIONS = 4

SUMMARIZATION_MODEL = "grok-4-fast"
SUMMARIZATION_TEMPERATURE = 0.0

WRITER_MODEL = "grok-4-fast-reasoning"
WRITER_TEMPERATURE = 0.0
WRITER_MAX_TOKENS = 32000
# WRITER_MODEL = "anthropic:claude-sonnet-4-20250514"

MIRMIR_API_SERVER_BASE_URL = "http://localhost:8001"
MIRMIR_TIMEOUT_SECONDS = 240  # 4 minutes

# LLM API timeouts (in seconds)
# Should be longer than MIRMIR_TIMEOUT to allow tool calls to complete
LLM_REQUEST_TIMEOUT = 240  # 4 minutes (longer than MirMir 3 min timeout)
LLM_HTTP_TIMEOUT = 240.0  # HTTP client timeout in seconds (must match or exceed REQUEST_TIMEOUT)

# xAI API configuration
XAI_BASE_URL = "https://api.x.ai/v1"