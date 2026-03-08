from pydantic import BaseModel
from typing import Optional

class Documento(BaseModel):
    id: Optional[int] = None
    nombre: str
    obligatorio: Optional[bool] = True