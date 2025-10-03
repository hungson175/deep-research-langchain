"""
Validate Complete Workflow V2 agent signatures without running LLM calls.
This script checks that all agent instantiations and method calls use correct parameters.
"""

import inspect
from src.agents.topics_generator import TopicsGenerator
from src.agents.opp_ceo_agent_topic_generator import OpponentCEOTopicGenerator
from src.agents.mrt_defensive_agent import MrTuongDefensiveAgent
from src.agents.brief_filter_agent import BriefFilterAgent
from src.agents.mrt_ranking_agent import MrTRankingAgent

def check_signature(class_name, method_name, expected_params):
    """Check if method signature matches expected parameters."""
    try:
        cls = globals()[class_name]
        method = getattr(cls, method_name)
        sig = inspect.signature(method)
        actual_params = list(sig.parameters.keys())

        # Remove 'self' from instance methods
        if 'self' in actual_params:
            actual_params.remove('self')

        print(f"\n{class_name}.{method_name}:")
        print(f"  Expected: {expected_params}")
        print(f"  Actual:   {actual_params}")

        # Check if expected params are in actual
        for param in expected_params:
            if param not in actual_params:
                print(f"  ❌ MISSING: {param}")
                return False

        print(f"  ✅ VALID")
        return True

    except Exception as e:
        print(f"  ❌ ERROR: {e}")
        return False

def main():
    print("=" * 80)
    print("Validating Complete Workflow V2 Agent Signatures")
    print("=" * 80)

    all_valid = True

    # Phase 0: TopicsGenerator
    print("\n[Phase 0: MrT Topics]")
    all_valid &= check_signature("TopicsGenerator", "__init__", ["max_tool_call_iterations"])
    all_valid &= check_signature("TopicsGenerator", "generate", ["period"])

    # Phase 1: OpponentCEOTopicGenerator
    print("\n[Phase 1: Opponent Attacks]")
    all_valid &= check_signature("OpponentCEOTopicGenerator", "__init__", ["ceo_type", "max_tool_call_iterations", "debug_log"])
    all_valid &= check_signature("OpponentCEOTopicGenerator", "generate", ["num_strategies"])

    # Phase 2: MrTuongDefensiveAgent
    print("\n[Phase 2: Defensive Response]")
    all_valid &= check_signature("MrTuongDefensiveAgent", "__init__", ["max_tool_call_iterations", "debug_log"])
    all_valid &= check_signature("MrTuongDefensiveAgent", "generate", ["opponent_name", "attack_strategies", "num_briefs"])

    # Phase 2.5: BriefFilterAgent
    print("\n[Phase 2.5: Brief Filtering]")
    all_valid &= check_signature("BriefFilterAgent", "__init__", [])
    all_valid &= check_signature("BriefFilterAgent", "filter_duplicates", ["briefs"])

    # Phase 4: MrTRankingAgent
    print("\n[Phase 4: Report Ranking]")
    all_valid &= check_signature("MrTRankingAgent", "__init__", ["debug_log"])
    all_valid &= check_signature("MrTRankingAgent", "rank_reports", ["report_paths"])

    print("\n" + "=" * 80)
    if all_valid:
        print("✅ ALL SIGNATURES VALID")
    else:
        print("❌ SOME SIGNATURES INVALID - CHECK ABOVE")
    print("=" * 80)

    return 0 if all_valid else 1

if __name__ == "__main__":
    exit(main())
