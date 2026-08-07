from agno.agent import Agent

from agno.models.groq import Groq 

from dotenv import load_dotenv

from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv()
def build_agent():
    return Agent(
        model=Groq(id="qwen-7b-chat"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are a helpful and expert travel agent. You will answer questions about travel, including destinations, accommodations, transportation, and activities. You will provide detailed and accurate information to help users plan their trips.",
        add_datetime_to_context=True  #todays date

    )

groq_agent = build_agent()

response = groq_agent.run("Is it safe to travel to UAE today")

print(response.content)