from fastapi import HTTPException
from app.models.document import DocumentUploadResponse
from app.rag.loaders.pdf_loader import PDFLoader
from app.rag.storage.local_storage import LocalStorage
from app.rag.chunking.text_splitter import TextSplitter


class DocumentService:
    """Coordinates document ingestion."""

    def __init__(self) -> None:
        self.storage = LocalStorage()
        self.loader = PDFLoader()
        self.splitter = TextSplitter()

    def upload_document(self, file):
        saved_file = self.storage.save(file)

        documents = self.loader.load(saved_file)

        chunks = self.splitter.split(documents)

        text = "\n".join(doc.page_content for doc in documents)

        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported."
                )

        return DocumentUploadResponse(
        filename=file.filename,
            pages=len(documents),
            characters=len(text),
            chunks=len(chunks),
            preview=chunks[0].page_content[:500],
        )
        
    