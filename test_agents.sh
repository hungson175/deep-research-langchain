#!/bin/bash
# Test script for refactored CEO agents

echo "========================================"
echo "Testing Refactored CEO Agents"
echo "Started: $(date)"
echo "========================================"
echo ""

echo "TEST 1/3: MrT Topics Generator"
echo "========================================"
python3 -m src.agents.topics_generator
echo ""

echo "========================================"
echo "TEST 2/3: Opponent CEO Agent (ZaloPay)"
echo "========================================"
python3 -m src.agents.opp_ceo_agent_topic_generator
echo ""

echo "========================================"
echo "TEST 3/3: Mr Tường Defensive Agent"
echo "========================================"
python3 -m src.agents.mrt_defensive_agent
echo ""

echo "========================================"
echo "ALL TESTS COMPLETED"
echo "Finished: $(date)"
echo "========================================"
