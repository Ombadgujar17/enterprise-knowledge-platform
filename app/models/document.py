from pydantic import BaseModel, Field


class DocumentUploadResponse(BaseModel):
    """Response returned after successfully uploading a document."""

    filename: str = Field(..., description="Uploaded document name")
    pages: int = Field(..., description="Number of pages in the document")
    characters: int = Field(..., description="Total extracted characters")
    preview: str = Field(..., description="Preview of extracted text")
    chunks: int = Field(
    ...,
    description="Number of generated text chunks",
)