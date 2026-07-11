from pathlib import Path

from fastapi import UploadFile


class LocalStorage:
    """Handles saving uploaded files locally."""

    def __init__(self) -> None:
        self.storage_path = Path("data/raw")
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def save(self, file: UploadFile) -> Path:
        """Save an uploaded file and return its local path."""

        destination = self.storage_path / file.filename

        with destination.open("wb") as buffer:
            buffer.write(file.file.read())

        return destination