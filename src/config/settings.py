import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")

    def validate(self) -> None:
        if not self.DATABASE_URL:
            raise ValueError("DATABASE_URL is not set")

settings = Settings()