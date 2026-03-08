from fastapi import APIRouter
from controllers.jurado_controller import *
from models.jurado_model import Jurado

router = APIRouter()

nuevo_jurado = JuradoController()


@router.post("/create_jurado")
async def create_jurado(jurado: Jurado):
    return nuevo_jurado.create_jurado(jurado)

@router.get("/get_jurado/{jurado_id}", response_model=Jurado)
async def get_jurado(jurado_id: int):
    return nuevo_jurado.get_jurado(jurado_id)


@router.get("/get_jurados", response_model=list[Jurado])
async def get_jurados():
    return nuevo_jurado.get_jurados()


@router.put("/update_jurado/{jurado_id}")
async def update_jurado(jurado_id: int, jurado: Jurado):
    return nuevo_jurado.update_jurado(jurado_id, jurado)


@router.delete("/delete_jurado/{jurado_id}")
async def delete_jurado(jurado_id: int):
    return nuevo_jurado.delete_jurado(jurado_id)