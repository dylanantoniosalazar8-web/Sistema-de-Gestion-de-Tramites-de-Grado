from pydantic import BaseModel
from typing import Optional

class TipoGrado(BaseModel):
    id_tipo: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None