from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.config.settings import settings

Base = declarative_base()

_engine = None
_SessionLocal = None


def get_engine():
    global _engine

    if _engine is None:
        if not settings.DATABASE_URL:
            raise ValueError(
                "DATABASE_URL is not set. "
                "Set environment variable before using database."
            )

        _engine = create_engine(settings.DATABASE_URL)

    return _engine


def get_session_local():
    global _SessionLocal

    if _SessionLocal is None:
        _SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=get_engine()
        )

    return _SessionLocal


def get_db():
    SessionLocal = get_session_local()
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()