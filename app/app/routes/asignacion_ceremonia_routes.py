from fastapi import APIRouter
from controllers.asignacion_ceremonia_controller import *
from models.asignacion_ceremonia_model import AsignacionCeremonia

router = APIRouter()

nueva_asignacion_ceremonia = AsignacionCeremoniaController()


@router.post("/create_asignacion_ceremonia")
async def create_asignacion_ceremonia(asignacion_ceremonia: AsignacionCeremonia):
    return nueva_asignacion_ceremonia.create_asignacion_ceremonia(asignacion_ceremonia)


@router.get("/get_asignacion_ceremonia/{asignacion_ceremonia_id}", response_model=AsignacionCeremonia)
async def get_asignacion_ceremonia(asignacion_ceremonia_id: int):
    return nueva_asignacion_ceremonia.get_asignacion_ceremonia(asignacion_ceremonia_id)


@router.get("/get_asignaciones_ceremonia/")
async def get_asignaciones_ceremonia():
    return nueva_asignacion_ceremonia.get_asignaciones_ceremonia()


@router.put("/update_asignacion_ceremonia/{asignacion_ceremonia_id}")
async def update_asignacion_ceremonia(asignacion_ceremonia_id: int, asignacion_ceremonia: AsignacionCeremonia):
    return nueva_asignacion_ceremonia.update_asignacion_ceremonia(asignacion_ceremonia_id, asignacion_ceremonia)


@router.delete("/delete_asignacion_ceremonia/{asignacion_ceremonia_id}")
async def delete_asignacion_ceremonia(asignacion_ceremonia_id: int):
    return nueva_asignacion_ceremonia.delete_asignacion_ceremonia(asignacion_ceremonia_id)