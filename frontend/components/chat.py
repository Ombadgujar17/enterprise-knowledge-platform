import streamlit as st


def render_chat() -> None:
    """Render the chat interface."""

    st.title("🤖 Enterprise Knowledge Assistant")

    st.info(
        "Upload a document to begin chatting with your knowledge base."
    )

    st.chat_input(
        "Ask a question...",
        disabled=True,
    )