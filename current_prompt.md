# First prompt
look at '/Users/sonph36/dev/deep_research_mrW/deep_research_langchain/sample_codes/auto-explore': it's MirMir Agent - read '/Users/sonph36/dev/deep_research_mrW/deep_research_langchain/sample_codes/auto-explore/CLAUDE.md' to 
understand the project

That agent can retrieve data from MoMo data store using nature language.


The main code is in: /Users/sonph36/dev/deep_research_mrW/deep_research_langchain/sample_codes/auto-explore/mirmir_agent - READ THIS DIRECTORY VERY CAREFUL to know how to implement it
Use the System Prompt & Tool description EXACTLY how it is , because those prompts cost millions of USD to make.


I want to implement a tool that supervior can use to retrieve MoMo data using that agent(in /Users/sonph36/dev/deep_research_mrW/deep_research_langchain/supervisor.py) 

What solution do you suggest - write it out here , so I can review it ?


---
# Second prompt

The description of tool query_momo_data() must be MUCH more details, and input must 

 "If referenced files are not found in expected locations, search for them using Glob or Grep tools." -> add LS tool