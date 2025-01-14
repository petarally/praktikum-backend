from pydantic import BaseModel
from typing import Optional

class Bill(BaseModel):
    house: str
    amount: float
    due_date: str
    category: str
    description: Optional[str] = None
