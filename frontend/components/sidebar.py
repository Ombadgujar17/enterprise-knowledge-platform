import streamlit as st

from components.status import render_status


def render_sidebar() -> None:
    """Render the application sidebar."""

    with st.sidebar:
        st.header("📄 Documents")

        st.file_uploader(
            "Upload a PDF",
            type=["pdf"],
            disabled=True,
        )

        st.button(
            "Upload",
            disabled=True,
            use_container_width=True,
        )

        st.divider()

        render_status(st.session_state.backend_connected)