# app/models.py
from pydantic import BaseModel, Field

class BMIInput(BaseModel):
    weight: float = Field(..., gt=0, description="Weight in kilograms (must be positive)")
    height: float = Field(..., gt=0, description="Height in meters (must be positive)")
