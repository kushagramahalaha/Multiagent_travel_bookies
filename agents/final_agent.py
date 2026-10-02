from langchain_core.messages import HumanMessage

from agents.shared import llm
from agents.state import TravelState


def final_agent(state: TravelState):
    final_prompt = f"""
Generate final travel response.
Flights:
{state['flight_results']}
Hotels:
{state['hotel_results']}
Itinerary:
{state['itinerary']}
"""
    response = llm.invoke([HumanMessage(content=final_prompt)])
    return {
        "messages": [response],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }
