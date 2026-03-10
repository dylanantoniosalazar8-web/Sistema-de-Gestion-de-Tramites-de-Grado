from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CeremoniaGrado(BaseModel):
    id_ceremonia: Optional[int] = None
    fecha: datetime
    lugar: str
    descripcion: Optional[str] = None