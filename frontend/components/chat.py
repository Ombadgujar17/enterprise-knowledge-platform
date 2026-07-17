import streamlit as st

WELCOME_QUESTIONS = [
    {
        "icon": "📄",
        "prompt": "Summarize this document",
    },
    {
        "icon": "📋",
        "prompt": "What is the leave policy?",
    },
    {
        "icon": "👨‍💼",
        "prompt": "Explain the onboarding process.",
    },
    {
        "icon": "🔒",
        "prompt": "What security policies exist?",
    },
]


def render_chat():
    """Render the chat interface."""

    st.title("🧠 Enterprise Knowledge Platform")

    st.caption(
        "Your AI assistant for enterprise knowledge and documentation."
    )

    selected_prompt = None

    if not st.session_state.chat_history:

        st.info(
            "Upload one or more PDF documents from the sidebar, then ask questions about them."
        )

        st.markdown("### 💡 Try asking")

        for suggestion in WELCOME_QUESTIONS:

            if st.button(
                f'{suggestion["icon"]} {suggestion["prompt"]}',
                use_container_width=True,
            ):
                selected_prompt = suggestion["prompt"]

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    chat_input = st.chat_input(
        "Ask a question about your documents..."
    )

    return chat_input, selected_prompt