from pydantic import BaseModel
from typing import Optional

class PagoTramite(BaseModel):
    id: Optional[int] = None
    tramite_id: Optional[int]
    requisito_id: Optional[int]
    cumplido: Optional[bool] = False