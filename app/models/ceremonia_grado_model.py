from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class CeremoniaGrado(BaseModel):
    id_ceremonia_grado: Optional[int] = None
    nombre: Optional[str] = None
    fecha: date
    lugar: Optional[str] = None
    horario: Optional[time] = None
    capacidad: Optional[int] = None