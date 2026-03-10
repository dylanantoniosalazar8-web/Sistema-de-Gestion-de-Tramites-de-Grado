from pydantic import BaseModel
from typing import Optional

class TipoGrado(BaseModel):
    id_tipo_grado: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None