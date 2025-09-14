from dotenv import load_dotenv
load_dotenv()

from utils import show_prompt, get_today_str
from prompts import human_clarify_with_user_instructions, human_transform_messages_into_research_topic_prompt
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, get_buffer_string
from typing import Union
from cache_strategy import CacheStrategyFactory, MessageCacheStrategy


class ClarifyWithUser(BaseModel):
    """Response for user clarification."""
    need_clarification: bool = Field(
        description="Whether the user needs to be asked a clarifying question.",
    )
    question: str = Field(
        description="A question to ask the user to clarify the report scope",
    )
    verification: str = Field(
        description="Verify message that we will start research after the user has provided the necessary information.",
    )

class ResearchQuestion(BaseModel):
    """Schema for structured research brief generation."""

    research_brief: str = Field(
        description="A research question that will be used to guide the research.",
    )

class FlexibleResponse(BaseModel):
    """Flexible response that can be either clarification or research brief."""
    response: Union[ClarifyWithUser, ResearchQuestion]
    
class ResearchBriefCreator:
    
    CLARIFIER_MODEL="xai:grok-code-fast-1"
    SYSTEM_PROMPT = """
    You are a research assistant that is helping the user to clarify their request for a research report then write a research brief.
    Today's date is {date}.
    """
    def __init__(self):
        self.llm = init_chat_model(model=self.CLARIFIER_MODEL, temperature=0.0)
        # Single structured output model that can handle both response types
        self.structured_output_model = self.llm.with_structured_output(FlexibleResponse)

        # Initialize cache strategy based on model
        self.cache_strategy = CacheStrategyFactory.create_strategy(self.CLARIFIER_MODEL)

        # Create initial system message with caching if supported
        system_msg = self.cache_strategy.prepare_system_message(
            self.SYSTEM_PROMPT.format(date=get_today_str())
        )
        self.messages = [system_msg]
        
    def clarify_with_user(self, user_input: str):
        # Create and append human message with cache strategy
        clarify_msg = self.cache_strategy.prepare_human_message(
            human_clarify_with_user_instructions.format(user_input=user_input),
            add_cache=True  # Cache the initial clarification request
        )
        self.messages.append(clarify_msg)

        while True:
            # Invoke directly - messages already have cache from prepare_human_message
            flexible_response = self.structured_output_model.invoke(self.messages)

            # Cleanup messages after invoke
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

            response = flexible_response.response

            # Check if it's a ClarifyWithUser response
            if isinstance(response, ClarifyWithUser):
                # Convert structured output to proper AIMessage
                self.messages.append(AIMessage(content=f"Need clarification: {response.need_clarification}\nQuestion: {response.question}\nVerification: {response.verification}"))

                if not response.need_clarification:
                    return response

                # Get user input (for interactive use)
                print(f"Clarification needed: {response.question}")
                user_answer = input("Your answer: ")

                # Create user answer message with cache strategy
                answer_msg = self.cache_strategy.prepare_human_message(
                    user_answer,
                    add_cache=True  # Cache user answers for better context
                )
                self.messages.append(answer_msg)
            else:
                # This shouldn't happen in clarify phase, but handle gracefully
                return response
    
    def write_research_brief(self) -> ResearchQuestion:
        # Create transform message with cache strategy
        transform_msg = self.cache_strategy.prepare_human_message(
            human_transform_messages_into_research_topic_prompt,
            add_cache=True  # Cache the transformation request
        )
        self.messages.append(transform_msg)

        # Invoke directly - messages already have cache from prepare_human_message
        flexible_response = self.structured_output_model.invoke(self.messages)

        # Cleanup messages after invoke
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        response = flexible_response.response

        # Check if it's a ResearchQuestion response
        if isinstance(response, ResearchQuestion):
            # Convert structured output to proper AIMessage
            self.messages.append(AIMessage(content=f"Research brief: {response.research_brief}"))
            return response
        else:
            # This shouldn't happen in research brief phase, but handle gracefully
            raise ValueError(f"Expected ResearchQuestion, got {type(response)}")
    
    def run(self, user_input: str):
        self.clarify_with_user(user_input)
        research_brief = self.write_research_brief()
        return research_brief


if __name__ == "__main__":
    brief_creator = ResearchBriefCreator()
    result = brief_creator.run("I want to research the best specialty coffee shops in VN main cities")
    print(f"Final research brief: {result.research_brief}")