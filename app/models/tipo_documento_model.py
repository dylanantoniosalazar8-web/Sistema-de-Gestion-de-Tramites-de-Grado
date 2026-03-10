from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TramiteGrado(BaseModel):
    id: Optional[int] = None
    estudiante_id: Optional[int]
    fecha_solicitud: Optional[datetime] = None
    estado: Optional[str] = "pendiente"
    observaciones: Optional[str] = None