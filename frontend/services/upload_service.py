import streamlit as st

from api.factory import get_api_client


def handle_document_upload(uploaded_file) -> None:
    """Upload a document and update application state."""

    client = get_api_client()

    try:
        with st.spinner("Uploading document..."):
            response = client.upload_document(uploaded_file)

        st.session_state.uploaded_documents.append(response)

        st.success(
            f"""
Successfully processed **{response.filename}**

• Pages: {response.pages}
• Chunks: {response.chunks}
• Status: {response.embedding_status}
"""
        )

    except Exception as exc:
        st.error(f"Upload failed.\n\n{exc}")