from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request model for chat messages."""

    message: str = Field(
        ...,
        description="User's natural language query",
    )


class ChatResponse(BaseModel):
    """Response model for chat messages."""

    response: str = Field(
        ...,
        description="Chatbot's response",
    )