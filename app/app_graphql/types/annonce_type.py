# app/graphql/types/annonce_type.py
import strawberry
from typing import Optional

@strawberry.type
class AnnonceType:
    title: str
    price: int
    year: int
    mileage: int
    url: str
    motorization: Optional[str] = None
    finish: Optional[str] = None
    description: Optional[str] = None
    score: Optional[float] = None

@strawberry.input
class AnnonceInput:
    title: str
    price: int
    year: int
    mileage: int
    url: str
    motorization: Optional[str] = None
    finish: Optional[str] = None
    description: Optional[str] = None