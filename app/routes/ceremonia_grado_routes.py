from fastapi import APIRouter
from controllers.ceremonia_grado_controller import *
from models.ceremonia_grado_model import CeremoniaGrado

router = APIRouter()

nueva_ceremonia_grado = CeremoniaGradoController()


@router.post("/create_ceremonia_grado")
async def create_ceremonia_grado(ceremonia_grado: CeremoniaGrado):
    return nueva_ceremonia_grado.create_ceremonia_grado(ceremonia_grado)


@router.get("/get_ceremonia_grado/{ceremonia_grado_id}", response_model=CeremoniaGrado)
async def get_ceremonia_grado(ceremonia_grado_id: int):
    return nueva_ceremonia_grado.get_ceremonia_grado(ceremonia_grado_id)


@router.get("/get_ceremonias_grado/")
async def get_ceremonias_grado():
    return nueva_ceremonia_grado.get_ceremonias_grado()


@router.put("/update_ceremonia_grado/{ceremonia_grado_id}")
async def update_ceremonia_grado(ceremonia_grado_id: int, ceremonia_grado: CeremoniaGrado):
    return nueva_ceremonia_grado.update_ceremonia_grado(ceremonia_grado_id, ceremonia_grado)


@router.delete("/delete_ceremonia_grado/{ceremonia_grado_id}")
async def delete_ceremonia_grado(ceremonia_grado_id: int):
    return nueva_ceremonia_grado.delete_ceremonia_grado(ceremonia_grado_id)