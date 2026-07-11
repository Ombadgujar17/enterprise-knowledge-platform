from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = "Enterprise Knowledge Platform"
    app_version: str = "0.1.0"
    app_env: str = "development"

    log_level: str = "INFO"

    openai_api_key: str = ""
    google_api_key: str = ""
    gemini_model: str = ""
    langsmith_api_key: str = ""

    llm_provider: str = ""
    llm_model: str = ""

    groq_api_key: str = ""

    chunk_size: int = 1000
    chunk_overlap: int = 200

    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2"
    chroma_db_path: str = "data/chroma"
    chroma_collection_name: str = "enterprise_documents"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()


settings = get_settings()