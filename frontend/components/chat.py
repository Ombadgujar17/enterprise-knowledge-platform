import streamlit as st


def render_chat():
    st.title("Enterprise Knowledge Platform")

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    return st.chat_input("Ask a question about your documents...")