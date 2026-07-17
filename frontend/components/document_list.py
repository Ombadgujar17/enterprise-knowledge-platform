import streamlit as st


def render_document_list() -> None:
    """Render uploaded document cards."""

    documents = st.session_state.uploaded_documents

    st.subheader(f"📚 Knowledge Base ({len(documents)})")

    if not documents:
        st.info("Upload a PDF to build your knowledge base.")
        return

    total_pages = 0
    total_chunks = 0

    for document in documents:
        total_pages += document.pages
        total_chunks += document.chunks

        with st.container(border=True):
            st.markdown(f"**📄 {document.filename}**")

            col1, col2 = st.columns(2)

            with col1:
                st.caption(f"📑 Pages: {document.pages}")

            with col2:
                st.caption(f"🧩 Chunks: {document.chunks}")

            status = document.embedding_status.replace("_", " ").title()

            if document.embedding_status == "completed":
                st.caption("✅ Status: Indexed")
            else:
                st.caption(f"⏳ Status: {status}")

    st.divider()

    st.subheader("📊 Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Documents", len(documents))
    col2.metric("Pages", total_pages)
    col3.metric("Chunks", total_chunks)