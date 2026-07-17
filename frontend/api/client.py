from __future__ import annotations

import httpx

from config import BACKEND_URL, REQUEST_TIMEOUT


class APIClient:
    """Client responsible for communicating with the FastAPI backend."""

    def __init__(
        self,
        base_url: str = BACKEND_URL,
        timeout: int = REQUEST_TIMEOUT,
    ) -> None:
        self.client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
        )

    def health_check(self) -> dict:
        response = self.client.get("/health")
        response.raise_for_status()
        return response.json()

    def close(self) -> None:
        self.client.close()