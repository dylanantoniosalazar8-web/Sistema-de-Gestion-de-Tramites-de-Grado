from pydantic import BaseModel
from typing import Optional

class Facultad(BaseModel):
    id: Optional[int] = None
    nombre: str