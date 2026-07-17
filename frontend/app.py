import streamlit as st

from api.factory import get_api_client
from components.chat import render_chat
from components.sidebar import render_sidebar
from utils.session import initialize_session

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
    layout="wide",
)

initialize_session()

client = get_api_client()

try:
    client.health_check()
    st.session_state.backend_connected = True
except Exception:
    st.session_state.backend_connected = False

# 1️⃣ Get user actions from the sidebar
uploaded_file, upload_clicked = render_sidebar()

# 2️⃣ Handle the upload here 👇
if upload_clicked and uploaded_file:
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

# 3️⃣ Render the chat interface
render_chat()