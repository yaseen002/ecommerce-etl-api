from sqlalchemy import create_engine
from src.config.settings import settings

engine = None

def get_engine():
    global engine
    if engine is None:
        if not settings.DATABASE_URL:
            raise ValueError("DATABASE_URL not configured")
        engine = create_engine(settings.DATABASE_URL)
    return engine