from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str
    environment: str


class DocumentUploadResponse(BaseModel):
    filename: str
    pages: int
    characters: int
    chunks: int
    preview: str
    embedding_status: str