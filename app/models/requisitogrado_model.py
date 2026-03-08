from pydantic import BaseModel
from typing import Optional

class RequisitoGrado(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None