from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class TipoDocumento(BaseModel):
    id_tipo_documento: Optional[int] = None
    nombre: str