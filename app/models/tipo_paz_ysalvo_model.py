from pydantic import BaseModel
from typing import Optional

class TipoPazYSalvo(BaseModel):
    id_tipo_paz_ysalvo: Optional[int] = None
    nombre: str