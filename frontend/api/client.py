from __future__ import annotations

import httpx

from config import BACKEND_URL, REQUEST_TIMEOUT
from models.responses import ChatResponse, HealthResponse
from models.responses import DocumentUploadResponse


class APIClient:
    """Client responsible for communicating with the FastAPI backend."""

    def __init__(
        self,
        base_url: str = BACKEND_URL,
        timeout: int = REQUEST_TIMEOUT,
    ) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
        )

    def health_check(self) -> dict:
        response = self._client.get("/health")
        response.raise_for_status()
        return HealthResponse.model_validate(response.json())
    
    def upload_document(self, uploaded_file) -> DocumentUploadResponse:
        """Upload a PDF document to the backend."""

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type,
            )
        }

        response = self._client.post(
            "/documents/",
            files=files,
        )

        response.raise_for_status()

        return DocumentUploadResponse.model_validate(
            response.json()
        )
        
    def chat(self, message: str) -> ChatResponse:
        response = self._client.post(
            "/chat/",
            json={
                "message": message,
            },
        )

        response.raise_for_status()

        return ChatResponse.model_validate(response.json())
    