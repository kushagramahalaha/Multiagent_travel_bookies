from langchain_core.messages import AIMessage

from agents.state import TravelState
from tools.flight_tool import search_flight


def flight_agent(state: TravelState):
    query = state["user_query"]
    flight_data = search_flight(query)
    return {
        "flight_results": flight_data,
        "messages": [AIMessage(content="Flight result fetched")],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }