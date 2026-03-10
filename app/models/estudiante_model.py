from pydantic import BaseModel
from typing import Optional
from datetime import date

class Estudiante(BaseModel):
    id_estudiante: Optional[int] = None
    nombre: str
    apellido: str
    documento: str
    id_tipo_documento: int
    correo: str
    id_programa: int
    id_tipo_grado: int
    fecha_nacimiento: Optional[date] = None