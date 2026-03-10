from pydantic import BaseModel
from typing import Optional
from datetime import date

class PazYSalvo(BaseModel):
    id_paz_ysalvo: Optional[int] = None
    id_tipo_paz_ysalvo: int
    id_estudiante: int
    fecha_aprobacion: Optional[date] = None
    estado: Optional[str] = "Pendiente"