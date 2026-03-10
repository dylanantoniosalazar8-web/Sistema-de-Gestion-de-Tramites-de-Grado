from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentoRequerido(BaseModel):
    id_documento_requerido: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    id_tipo_grado: int