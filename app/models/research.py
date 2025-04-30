from pydantic import BaseModel
from typing import Optional

class Research(BaseModel):
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
