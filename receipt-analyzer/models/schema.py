from pydantic import BaseModel
from typing import Optional
from datetime import date

class Receipt(BaseModel):
    vendor: str
    amount: float
    date: date
    category: Optional[str]
