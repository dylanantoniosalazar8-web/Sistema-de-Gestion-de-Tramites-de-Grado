from pydantic import BaseModel
from typing import Optional

class PazYSalvo(BaseModel):
    id_pazsalvo: Optional[int] = None
    id_estudiante: int
    biblioteca: bool
    financiero: bool
    laboratorio: bool