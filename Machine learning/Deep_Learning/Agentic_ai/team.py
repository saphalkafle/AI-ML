from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
# from agno.tools.duckduckgo import DuckDuckGoTools
from agno.team import Team
load_dotenv()


eng_agent = Agent(name="English Agent",role="You answer questions in English.")
chinese_agent = Agent(name="Chinese Agent",role="You answer questions in Chinese.")
nepali_agent = Agent(name="Nepali Agent",role="You answer questions in Nepali.")


team_leader = Team(
    name="Answer and Translate Team",
    members=[eng_agent, chinese_agent, nepali_agent],
    model = Groq("llama-3.3-70b-versatile"),
    markdown=True,
    show_members_responses=True,
    instructions="""All member agents must responf to answer the query in their specific language.
                         Do not route just one agent
                         Output the response of all agents"""
)

team_leader.print_response("why do people switch their gender?")