import streamlit as st

from api.factory import get_api_client


def handle_chat_message(message: str) -> None:
    """Send a chat message and update conversation history."""

    client = get_api_client()

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": message,
        }
    )

    with st.spinner("Thinking..."):
        response = client.chat(message)

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": response.response,
        }
    )