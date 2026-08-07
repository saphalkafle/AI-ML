from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

from agno.tools.yfinance import YFinanceTools
from agno.tools.duckduckgo import DuckDuckGoTools
load_dotenv()
def build_agent():
    return Agent(
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[DuckDuckGoTools(), YFinanceTools()],
        markdown=True,
        add_datetime_to_context=True,
        description="You are a comprehensive investment analyst with access to all financial data functions.",
        instructions=[
        "Use any financial function as needed for investment analysis",
        "Format your response using markdown and use tables to display data",
        "Provide detailed analysis and insights based on the data",
        "Include relevant financial metrics and recommendations",
    ],
        debug_mode=True
    )

agent = build_agent()
agent.print_response("What will be the best investment strategy for the next quarter based on current market trends and financial data?")