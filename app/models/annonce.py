# app/models/annonce.py
from pydantic import BaseModel
from typing import Optional

class Annonce(BaseModel):
    title: str
    price: int
    year: int
    mileage: int
    url: str
    motorization: Optional[str]
    finish: Optional[str] = None
    description: Optional[str] = None
    score: Optional[float] = None