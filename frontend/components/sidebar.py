import streamlit as st

from components.status import render_status


def render_sidebar():
    print(">>> render_sidebar() called")

    with st.sidebar:
        st.header("📄 Documents")

        uploaded_file = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
        )

        upload_clicked = st.button(
            "Upload",
            use_container_width=True,
            disabled=uploaded_file is None,
        )

        st.divider()

        render_status(st.session_state.backend_connected)

    print(">>> Returning:", uploaded_file, upload_clicked)
    return uploaded_file, upload_clicked