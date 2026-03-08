from pydantic import BaseModel
from typing import Optional

class Jurado(BaseModel):
    id: Optional[int] = None
    nombre: str
    correo: str
    especialidad: Optional[str] = None