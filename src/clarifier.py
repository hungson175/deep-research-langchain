from dotenv import load_dotenv
load_dotenv()

from .utils import show_prompt, get_today_str, console, init_xai_model
from rich.panel import Panel
from rich.text import Text
from .prompts import human_clarify_with_user_instructions, human_transform_messages_into_research_topic_prompt
from pydantic import BaseModel, Field
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, get_buffer_string
from typing import Union
from .cache_strategy import CacheStrategyFactory, MessageCacheStrategy
from .config import CLARIFIER_MODEL, CLARIFIER_TEMPERATURE


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

    SYSTEM_PROMPT = """
    You are a research assistant that is helping the user to clarify their request for a research report then write a research brief.
    Today's date is {date}.
    """
    def __init__(self):
        console.print(Panel("[bold cyan]🎯 Initializing Research Brief Creator[/bold cyan]", border_style="cyan"))

        self.llm = init_xai_model(model=CLARIFIER_MODEL, temperature=CLARIFIER_TEMPERATURE)
        # Single structured output model that can handle both response types
        self.structured_output_model = self.llm.with_structured_output(FlexibleResponse)

        # Initialize cache strategy based on model
        self.cache_strategy = CacheStrategyFactory.create_strategy(f"xai:{CLARIFIER_MODEL}")
        console.print(f"[dim]Using model: {CLARIFIER_MODEL}[/dim]")
        console.print(f"[dim]Cache strategy: {self.cache_strategy.__class__.__name__}[/dim]")

        self.total_tokens = 0

        # Create initial system message with caching if supported
        system_msg = self.cache_strategy.prepare_system_message(
            self.SYSTEM_PROMPT.format(date=get_today_str())
        )
        self.messages = [system_msg]
        
    def clarify_with_user(self, user_input: str):
        console.print(Panel(f"[bold blue]📝 Starting Clarification Process[/bold blue]\n\nUser input: {user_input}", border_style="blue"))

        # Create and append human message with cache strategy
        clarify_msg = self.cache_strategy.prepare_human_message(
            human_clarify_with_user_instructions.format(user_input=user_input),
            add_cache=True  # Cache the initial clarification request
        )
        self.messages.append(clarify_msg)

        while True:
            console.print("[dim]Invoking LLM for clarification...[/dim]")
            # Invoke directly - messages already have cache from prepare_human_message
            flexible_response = self.structured_output_model.invoke(self.messages)
            if hasattr(flexible_response, 'usage_metadata') and flexible_response.usage_metadata:
                self.total_tokens += flexible_response.usage_metadata.get('total_tokens', 0)

            # DEBUG: Log the exact response
            console.print(f"[yellow]DEBUG - flexible_response type: {type(flexible_response)}[/yellow]")
            console.print(f"[yellow]DEBUG - flexible_response: {flexible_response}[/yellow]")
            console.print(f"[yellow]DEBUG - flexible_response.response type: {type(flexible_response.response)}[/yellow]")
            console.print(f"[yellow]DEBUG - flexible_response.response: {flexible_response.response}[/yellow]")

            # Cleanup messages after invoke
            self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

            response = flexible_response.response

            # Check if it's a ClarifyWithUser response
            if isinstance(response, ClarifyWithUser):
                # Convert structured output to proper AIMessage
                self.messages.append(AIMessage(content=f"Need clarification: {response.need_clarification}\nQuestion: {response.question}\nVerification: {response.verification}"))

                if not response.need_clarification:
                    console.print(Panel("[bold green]✅ No further clarification needed[/bold green]", border_style="green"))
                    console.print(f"[dim]Verification: {response.verification}[/dim]")
                    return response

                # Get user input (for interactive use)
                console.print(Panel(f"[bold yellow]❓ Clarification Required[/bold yellow]\n\n{response.question}", border_style="yellow"))
                user_answer = input("Your answer: ")
                console.print(f"[dim]User answered: {user_answer}[/dim]")

                # Create user answer message with cache strategy
                answer_msg = self.cache_strategy.prepare_human_message(
                    user_answer,
                    add_cache=True  # Cache user answers for better context
                )
                self.messages.append(answer_msg)
            else:
                # This shouldn't happen in clarify phase, but handle gracefully
                console.print("[red]Unexpected response type in clarification phase[/red]")
                return response
    
    def write_research_brief(self) -> ResearchQuestion:
        console.print(Panel("[bold magenta]📋 Creating Research Brief[/bold magenta]", border_style="magenta"))

        # Create transform message with cache strategy
        transform_msg = self.cache_strategy.prepare_human_message(
            human_transform_messages_into_research_topic_prompt,
            add_cache=True  # Cache the transformation request
        )
        self.messages.append(transform_msg)

        console.print("[dim]Transforming conversation into research brief...[/dim]")
        # Invoke directly - messages already have cache from prepare_human_message
        flexible_response = self.structured_output_model.invoke(self.messages)
        if hasattr(flexible_response, 'usage_metadata') and flexible_response.usage_metadata:
            self.total_tokens += flexible_response.usage_metadata.get('total_tokens', 0)

        # Cleanup messages after invoke
        self.messages = self.cache_strategy.cleanup_messages_after_invoke(self.messages)

        response = flexible_response.response

        # Check if it's a ResearchQuestion response
        if isinstance(response, ResearchQuestion):
            # Convert structured output to proper AIMessage
            self.messages.append(AIMessage(content=f"Research brief: {response.research_brief}"))
            console.print(Panel(f"[bold green]✅ Research Brief Created[/bold green]\n\n{response.research_brief}", border_style="green"))
            return response
        else:
            # This shouldn't happen in research brief phase, but handle gracefully
            console.print(f"[red]Error: Expected ResearchQuestion, got {type(response)}[/red]")
            raise ValueError(f"Expected ResearchQuestion, got {type(response)}")
    
    def run(self, user_input: str):
        console.print(Panel("[bold cyan]🚀 Starting Research Brief Creation Process[/bold cyan]", border_style="cyan"))
        self.clarify_with_user(user_input)
        research_brief = self.write_research_brief()
        console.print(Panel("[bold cyan]✨ Research Brief Creation Complete[/bold cyan]", border_style="cyan"))
        return research_brief


if __name__ == "__main__":
    console.print("[bold]═" * 80 + "[/bold]")
    console.print(Panel("[bold cyan]Research Brief Creator - Demo Mode[/bold cyan]", border_style="cyan"))
    console.print("[bold]═" * 80 + "[/bold]")

    brief_creator = ResearchBriefCreator()
    result = brief_creator.run("I want to research the best specialty coffee shops in VN main cities")

    console.print("\n[bold]═" * 80 + "[/bold]")
    console.print(Panel(f"[bold green]📄 Final Research Brief[/bold green]\n\n{result.research_brief}", border_style="green"))
    console.print("[bold]═" * 80 + "[/bold]")