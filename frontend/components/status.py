import streamlit as st


def render_status(connected: bool) -> None:
    """Render backend connection status."""

    st.subheader("Backend Status")

    if connected:
        st.success("🟢 Connected")
    else:
        st.error("🔴 Disconnected")