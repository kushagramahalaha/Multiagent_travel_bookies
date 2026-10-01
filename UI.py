import streamlit as st
import uuid

from langchain_core.messages import HumanMessage

# Import the compiled LangGraph application
from main import app


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="AI Travel Booking Agent",
    page_icon="✈️",
    layout="wide"
)

st.title("✈️ AI Travel Booking System")
st.caption("Multi-Agent Travel Planner powered by LangGraph")


# -----------------------------
# Create a unique session/thread
# -----------------------------
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())


# -----------------------------
# Store frontend chat history
# -----------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("Travel Assistant")

    st.write("Your request will be processed by:")

    st.write("✈️ Flight Agent")
    st.write("🏨 Hotel Agent")
    st.write("🗓️ Itinerary Agent")
    st.write("🤖 Final Response Agent")

    st.divider()

    if st.button("Clear Chat"):
        st.session_state.chat_history = []
        st.session_state.thread_id = str(uuid.uuid4())
        st.rerun()


# -----------------------------
# Display previous chat
# -----------------------------
for chat in st.session_state.chat_history:

    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])


# -----------------------------
# User input
# -----------------------------
user_input = st.chat_input(
    "Example: Plan a 5-day trip from Delhi to Goa..."
)


# -----------------------------
# Process request
# -----------------------------
if user_input:

    # Display user message immediately
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Configuration for LangGraph checkpointer
    config = {
        "configurable": {
            "thread_id": st.session_state.thread_id
        }
    }

    # Show processing status
    with st.chat_message("assistant"):

        with st.spinner("Planning your trip..."):

            try:

                result = app.invoke(
                    {
                        "messages": [
                            HumanMessage(content=user_input)
                        ],
                        "user_query": user_input,
                    },
                    config=config
                )

                # Get final message
                final_response = result["messages"][-1].content

                st.markdown(final_response)

                # Save assistant response
                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": final_response
                    }
                )

            except Exception as e:

                error_message = f"Error while processing request:\n\n`{str(e)}`"

                st.error(error_message)

                st.session_state.chat_history.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )