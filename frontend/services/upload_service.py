import streamlit as st

from api.factory import get_api_client


def handle_document_upload(uploaded_file) -> None:
    client = get_api_client()

    try:
        with st.spinner("Uploading document..."):
            response = client.upload_document(uploaded_file)

        existing_files = {
            doc.filename
            for doc in st.session_state.uploaded_documents
        }

        if response.filename not in existing_files:
            st.session_state.uploaded_documents.append(response)


        st.success(
            f"""
Successfully processed **{response.filename}**

• Pages: {response.pages}
• Chunks: {response.chunks}
• Status: {response.embedding_status}
"""
        )

        st.rerun()

    except Exception as exc:
        st.error(f"Upload failed.\n\n{exc}")