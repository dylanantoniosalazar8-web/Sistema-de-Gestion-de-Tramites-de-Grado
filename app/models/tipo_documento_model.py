from pydantic import BaseModel
from typing import Optional
<<<<<<< HEAD
from datetime import date

class TramiteGrado(BaseModel):
    id_tramite_grado: Optional[int] = None
    id_estudiante: int
    id_tipo_grado: int
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    estado: Optional[str] = "En Proceso"
=======
from datetime import datetime
from decimal import Decimal

class TipoDocumento(BaseModel):
    id_tipo_documento: Optional[int] = None
    nombre: str
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
