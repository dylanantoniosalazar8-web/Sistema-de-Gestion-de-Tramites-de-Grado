from pydantic import BaseModel
from typing import Optional
from datetime import date


class EntregaDocumento(BaseModel):
    id_entrega_documento: Optional[int] = None
    id_estudiante: int
    id_documento_requerido: int
    fecha_entrega: Optional[date] = None
    estado: Optional[str] = "Pendiente"
