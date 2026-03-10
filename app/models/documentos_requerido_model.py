from pydantic import BaseModel
from typing import Optional

class DocumentoRequerido(BaseModel):
    id_documento: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = True