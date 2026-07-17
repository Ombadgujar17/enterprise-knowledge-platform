import streamlit as st

from api.client import APIClient

st.set_page_config(
    page_title="Enterprise Knowledge Assistant",
    page_icon="🤖",
)

st.title("Enterprise Knowledge Assistant")

client = APIClient()

try:
    health = client.health_check()
    st.success(f"Backend connected: {health}")
except Exception as exc:
    st.error(f"Cannot connect to backend.\n\n{exc}")
finally:
    client.close()