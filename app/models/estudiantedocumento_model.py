from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EstudianteDocumento(BaseModel):
    id: Optional[int] = None
    estudiante_id: Optional[int]
    documento_id: Optional[int]
    entregado: Optional[bool] = False
    fecha_entrega: Optional[datetime] = None