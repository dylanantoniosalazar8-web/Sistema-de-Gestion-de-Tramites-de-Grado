from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PagoTramite(BaseModel):
    id_pago: Optional[int] = None
    estudiante_id: int
    fecha_pago: Optional[datetime] = None
    monto: float
    metodo_pago: Optional[str] = None