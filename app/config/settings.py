from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Enterprise Knowledge Platform"
    app_version: str = "0.1.0"
    app_env: str = "development"

    log_level: str = "INFO"

    openai_api_key: str = ""

    google_api_key: str = ""

    langsmith_api_key: str = ""

    class Config:
        env_file = ".env"

settings = Settings()