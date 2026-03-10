from fastapi import APIRouter
from controllers.tipo_grado_controller import *
from models.tipo_grado_model import TipoGrado

router = APIRouter()

nuevo_tipo_grado = TipoGradoController()


@router.post("/create_tipo_grado")
async def create_tipo_grado(tipo_grado: TipoGrado):
    return nuevo_tipo_grado.create_tipo_grado(tipo_grado)


@router.get("/get_tipo_grado/{tipo_grado_id}", response_model=TipoGrado)
async def get_tipo_grado(tipo_grado_id: int):
    return nuevo_tipo_grado.get_tipo_grado(tipo_grado_id)


@router.get("/get_tipos_grado/")
async def get_tipos_grado():
    return nuevo_tipo_grado.get_tipos_grado()


@router.put("/update_tipo_grado/{tipo_grado_id}")
async def update_tipo_grado(tipo_grado_id: int, tipo_grado: TipoGrado):
    return nuevo_tipo_grado.update_tipo_grado(tipo_grado_id, tipo_grado)


@router.delete("/delete_tipo_grado/{tipo_grado_id}")
async def delete_tipo_grado(tipo_grado_id: int):
    return nuevo_tipo_grado.delete_tipo_grado(tipo_grado_id)