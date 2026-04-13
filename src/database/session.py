from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config.settings import settings

_engine = None


def get_engine():
    """
    Lazily creates database engine.
    Prevents CI/CD crashes when DATABASE_URL is missing.
    """
    global _engine

    if _engine is None:
        if not settings.DATABASE_URL:
            raise ValueError(
                "DATABASE_URL is not set. "
                "Set environment variable before using database."
            )

        _engine = create_engine(settings.DATABASE_URL)

    return _engine


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=get_engine()
)


def get_db():
    """
    Dependency for FastAPI routes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()