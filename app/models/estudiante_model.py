from pydantic import BaseModel
from typing import Optional

class Estudiante(BaseModel):
    id_estudiante: Optional[int] = None
    nombre: str
    documento: str
    correo: str
    telefono: Optional[str] = None
    programa_id: Optional[int] = None