from api.factory import get_api_client
import streamlit as st


def check_backend_health() -> None:
    """Update backend connection status."""

    client = get_api_client()

    try:
        client.health_check()
        st.session_state.backend_connected = True
    except Exception:
        st.session_state.backend_connected = False