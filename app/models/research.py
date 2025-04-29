from pydantic import BaseModel
from typing import Optional

class Research(BaseModel):
    brand: str
    model: str
    finish: Optional[str] = None
    motorization: Optional[str] = None
    year_min: Optional[int] = None
    year_max: Optional[int] = None
    price_max: Optional[int] = None
    mileage_max: Optional[int] = None
    fuel: Optional[str] = None
    transmission: Optional[str] = None
    free_text: Optional[str] = None
