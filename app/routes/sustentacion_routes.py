from fastapi import APIRouter
from controllers.sustentacion_controller import *
from models.sustentacion_model import Sustentacion

router = APIRouter()

nueva_sustentacion = SustentacionController()


@router.post("/create_sustentacion")
async def create_sustentacion(sustentacion: Sustentacion):
    return nueva_sustentacion.create_sustentacion(sustentacion)

@router.get("/get_sustentacion/{sustentacion_id}", response_model=Sustentacion)
async def get_sustentacion(sustentacion_id: int):
    return nueva_sustentacion.get_sustentacion(sustentacion_id)


@router.get("/get_sustentaciones", response_model=list[Sustentacion])
async def get_sustentaciones():
    return nueva_sustentacion.get_sustentaciones()


@router.put("/update_sustentacion/{sustentacion_id}")
async def update_sustentacion(sustentacion_id: int, sustentacion: Sustentacion):
    return nueva_sustentacion.update_sustentacion(sustentacion_id, sustentacion)


@router.delete("/delete_sustentacion/{sustentacion_id}")
async def delete_sustentacion(sustentacion_id: int):
    return nueva_sustentacion.delete_sustentacion(sustentacion_id)