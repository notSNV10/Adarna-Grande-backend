"""
Configuration loader for environment-driven settings.
Use simple defaults for local development; override via environment variables.
"""
import os
from functools import lru_cache
from typing import Optional


class Settings:
    # Database
    db_host: str = os.getenv("DB_HOST", "148.222.53.75")
    db_user: str = os.getenv("DB_USER", "u446276639_adarna_user")
    db_password: str = os.getenv("DB_PASSWORD", "f!7WBjM4b")
    db_name: str = os.getenv("DB_NAME", "u446276639_adarna_db")
    db_port: int = int(os.getenv("DB_PORT", "3306"))

    # AI keys (placeholders; use env vars in local .env or host secrets)
    openrouter_api_key: Optional[str] = os.getenv("OPENROUTER_API_KEY")
    gemini_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")
    mistral_api_key: Optional[str] = os.getenv("MISTRAL_API_KEY")

    # Operational
    ai_timeout_seconds: int = int(os.getenv("AI_TIMEOUT_SECONDS", "20"))
    ai_log_prompts: bool = os.getenv("AI_LOG_PROMPTS", "true").lower() == "true"


@lru_cache()
def get_settings() -> Settings:
    return Settings()

