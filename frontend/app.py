import streamlit as st

from api.client import APIClient
from components.chat import render_chat
from components.sidebar import render_sidebar
from utils.session import initialize_session
from api.factory import get_api_client


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


render_sidebar()
render_chat()