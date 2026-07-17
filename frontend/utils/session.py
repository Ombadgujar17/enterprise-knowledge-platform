import streamlit as st


def initialize_session() -> None:
    """Initialize Streamlit session state."""

    defaults = {
        "chat_history": [],
        "backend_connected": False,
        "uploaded_documents": [],
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []