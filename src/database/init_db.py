"""
Database initialization script.

Creates database tables from ORM models.
"""

from src.database.session import engine
from src.database.models import Base


def init_db():
    """
    Initialize database schema.
    """
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()