from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProductSchema(BaseModel):
    id: int
    name: str
    price: float
    availability: str
    description: Optional[str] = None
    rating: Optional[int] = None
    scraped_at: datetime

    model_config = {
        "from_attributes": True  # <- Pydantic v2 replacement for orm_mode
    }