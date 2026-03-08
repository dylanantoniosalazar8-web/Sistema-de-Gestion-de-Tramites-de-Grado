from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class PagoGrado(BaseModel):
    id: Optional[int] = None
    tramite_id: Optional[int]
    valor: Optional[Decimal]
    fecha_pago: Optional[datetime] = None
    estado: Optional[str] = None