from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb
from rich.pretty import pprint
load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()
def build_agent():
    return Agent(
        db=db,
        model=Groq(id="llama-3.3-70b-versatile"),
        markdown=True,
        add_history_to_context=True,
        enable_user_memories=True
        # instructions="You are a helpful and expert travel agent. You will answer questions about travel, including destinations, accommodations, transportation, and activities. You will provide detailed and accurate information to help users plan their trips.",
        # add_datetime_to_context=True  #todays date
    )

agent = build_agent()

user_id = "ram@gmail.com"
agent.print_response("I am hari and I am data Analyst.",user_id=user_id)
agent.print_response("who am i?",user_id=user_id)

memories = agent.get_user_memories(
    user_id=user_id
)
print("MEMORIES:")
pprint(memories)