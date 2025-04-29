# app/app_graphql/types/research_type.py
import strawberry
from typing import Optional

@strawberry.type
class ResearchType:
    brand: str
    model: str
    finish: Optional[str] = None
    motorization: Optional[str] = None
    yearMin: Optional[int] = None
    yearMax: Optional[int] = None
    priceMax: Optional[int] = None
    mileageMax: Optional[int] = None
    fuel: Optional[str] = None
    transmission: Optional[str] = None
    freeText: Optional[str] = None

@strawberry.input
class ResearchInput:
    brand: str
    model: str
    finish: Optional[str] = None
    motorization: Optional[str] = None
    yearMin: Optional[int] = None
    yearMax: Optional[int] = None
    priceMax: Optional[int] = None
    mileageMax: Optional[int] = None
    fuel: Optional[str] = None
    transmission: Optional[str] = None
    freeText: Optional[str] = None