import streamlit as st

from api.client import APIClient


@st.cache_resource
def get_api_client() -> APIClient:
    """Return a cached API client."""
    return APIClient()