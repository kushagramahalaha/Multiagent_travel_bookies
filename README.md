# Multi-Agent Travel Booking System

A LangGraph-based travel assistant that plans trips using multiple specialized agents working together. The system collects flight information, checks hotel options, creates an itinerary, and produces a final travel response for the user.

## System Overview

This project simulates a travel booking workflow with different agents:

- Flight Agent: fetches flight-related data
- Hotel Agent: looks up hotel suggestions and travel stay information
- Itinerary Agent: creates a structured trip plan
- Final Agent: combines all outputs into one polished final response

The whole process is orchestrated with LangGraph, which manages the flow between agents.

## Main Features

- Multi-agent workflow for travel planning
- Flight search integration
- Hotel research using Tavily search
- Itinerary generation with Groq LLM
- Final travel response generation
- Postgres-based LangGraph checkpointing
- Streamlit UI for interacting with the system

## Project Structure

```text
Multiagent travel booking system/
├── main.py                  # Graph setup and app execution
├── UI.py                   # Streamlit frontend
├── agents/
│   ├── __init__.py
│   ├── state.py            # Shared travel state
│   ├── shared.py           # Shared LLM config
│   ├── flight_agent.py
│   ├── hotel_agent.py
│   ├── itinerary_agent.py
│   ├── final_agent.py
├── tools/
│   ├── flight_tool.py
│   └── tavily_tool.py
├── langgraph_env3/         # Local Python environment
├── .env                    # Environment variables (not always committed)
├── requirements.txt        # Project dependencies
└── README.md
```

## Number of Agents

This system contains 4 agents:

1. Flight Agent
2. Hotel Agent
3. Itinerary Agent
4. Final Response Agent

## Requirements

Before running the project, make sure you have:

- Python 3.9+
- A virtual environment or project environment
- Access to the following APIs/keys:
  - Groq API key
  - Tavily API key
  - AviationStack API key
  - PostgreSQL connection string for DATABASE_URL

## Environment Variables

Create a `.env` file in the project root with values like:

```env
DATABASE_URL=your_postgres_connection_string
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
AVIATIONSTACK_API_KEY=your_aviationstack_key
```

> Note: The current project uses `ChatGroq` and reads environment variables using `python-dotenv`.

## Installation

From the project root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If a `requirements.txt` file is not present yet, install the dependencies manually:

```bash
pip install langgraph langchain-core langchain-groq python-dotenv psycopg requests tavily-python streamlit
```

## Running the Application

### Run the backend workflow

```bash
python main.py
```

### Run the UI

```bash
streamlit run UI.py
```

## How the System Works

1. The user enters a travel request.
2. The Flight Agent fetches flight data.
3. The Hotel Agent searches for hotel options.
4. The Itinerary Agent creates a complete travel plan.
5. The Final Agent combines the results into a final response.
6. The workflow is stored with Postgres-based checkpointing.

## Use Case

This system is useful for:

- Travel planning for vacations
- Multi-city trip planning
- Quick flight and hotel suggestions
- Personalized itinerary generation

## Notes

This is a prototype multi-agent travel planner intended for learning, experimentation, and extension. You can expand it by adding:

- car rental agent
- weather agent
- budget agent
- booking/checkout flow
- user authentication

## License

This project is for educational and demonstration purposes.
