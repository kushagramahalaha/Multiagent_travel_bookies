from langchain_core.messages import HumanMessage, SystemMessage

from agents.shared import llm
from agents.state import TravelState


def itinerary_agent(state: TravelState):
    prompt = f"""
Create a travel itinerary.
User Query:
{state['user_query']}

Flight Results:
{state['flight_results']}
Hotel Results:
{state['hotel_results']}
"""
    response = llm.invoke(
        [
            SystemMessage(content="You are an expert travel planner."),
            HumanMessage(content=prompt),
        ]
    )
    return {
        "itinerary": response.content,
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }
