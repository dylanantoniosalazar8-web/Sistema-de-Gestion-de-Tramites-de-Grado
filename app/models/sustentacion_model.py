from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class Sustentacion(BaseModel):
    id: Optional[int] = None
    tramite_id: Optional[int]
    jurado_id: Optional[int]
    fecha: Optional[datetime] = None
    nota: Optional[Decimal] = None