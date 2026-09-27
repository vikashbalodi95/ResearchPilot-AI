from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "ResearchPilot AI"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    GROQ_API_KEY: str = ""
    FRONTEND_ORIGINS: str = "http://localhost:5173,http://127.0.0.1:5173"

    class Config:
        env_file = ".env"

settings = Settings()