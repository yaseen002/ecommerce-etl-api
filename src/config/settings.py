"""
Application configuration module.

Loads environment variables and provides database connection settings.
"""

from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """Central configuration class."""

    DATABASE_URL: str = os.getenv("DATABASE_URL", "")


settings = Settings()