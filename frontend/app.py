import streamlit as st

from services.chat_service import handle_chat_message
from api.factory import get_api_client
from components.chat import render_chat
from components.sidebar import render_sidebar
from utils.session import initialize_session
from services.upload_service import handle_document_upload

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
    layout="wide",
)

initialize_session()

client = get_api_client()

uploaded_file, upload_clicked = render_sidebar()

if upload_clicked and uploaded_file:
    handle_document_upload(uploaded_file)


# 3️⃣ Render the chat interface
message = render_chat()

if message:
    handle_chat_message(message)

    st.rerun()