"""
Database models for product storage.

Defines ORM schema for scraped product data.
"""

from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from src.database.session import Base


class Product(Base):
    """
    Product ORM model.

    Represents scraped e-commerce product data.
    """

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False, index=True)

    price = Column(Float, nullable=False, index=True)

    availability = Column(String, nullable=False)

    description = Column(String, nullable=True)

    rating = Column(Integer, nullable=True)

    scraped_at = Column(DateTime, default=datetime.utcnow)