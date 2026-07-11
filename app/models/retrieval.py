from pydantic import BaseModel, Field


class RetrievalRequest(BaseModel):
    """Request model for document retrieval."""

    query: str = Field(
        ...,
        description="User query",
    )


class RetrievalResponse(BaseModel):
    """Response model for document retrieval."""

    chunks: list[str]