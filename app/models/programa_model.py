from pydantic import BaseModel
from typing import Optional

class Programa(BaseModel):
    id_programa: Optional[int] = None
    nombre: str
    id_facultad: int