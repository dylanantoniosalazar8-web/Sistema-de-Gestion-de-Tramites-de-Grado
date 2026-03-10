from pydantic import BaseModel
from typing import Optional
from datetime import date


class TramiteGrado(BaseModel):
    id_tramite_grado: Optional[int] = None
    id_estudiante: int
    id_tipo_grado: int
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    estado: Optional[str] = "En Proceso"