from fastapi import APIRouter, File, UploadFile

from app.models.document import DocumentUploadResponse
from app.services.document_service import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
) 


@router.post("/", response_model=DocumentUploadResponse)
def upload_document(
    file: UploadFile = File(...)
) -> DocumentUploadResponse:
    """Upload and process a PDF document."""

    service = DocumentService()

    return service.upload_document(file)