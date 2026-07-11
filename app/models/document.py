from pydantic import BaseModel, Field


class DocumentUploadResponse(BaseModel):
    filename: str

    pages: int

    characters: int

    chunks: int

    preview: str

    embedding_status: str = Field(
        ...,
        description="Embedding status",
    )