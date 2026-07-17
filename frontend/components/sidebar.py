import streamlit as st

from components.status import render_status
from components.document_list import render_document_list


def render_sidebar():
    print(">>> render_sidebar() called")

    with st.sidebar:
        st.header("🧠 Knowledge Base")

        uploaded_file = st.file_uploader(
            "Upload PDF",
            type=["pdf"],
        )

        upload_clicked = st.button(
            "Upload",
            use_container_width=True,
            disabled=uploaded_file is None,
        )

        render_document_list()

        st.divider()

        render_status(st.session_state.backend_connected)

    return uploaded_file, upload_clicked