from fastapi import APIRouter
from controllers.tramite_grado_controller import *
from models.tramite_grado_model import TramiteGrado

router = APIRouter()

nuevo_tramite_grado = TramiteGradoController()


@router.post("/create_tramite_grado")
async def create_tramite_grado(tramite_grado: TramiteGrado):
    return nuevo_tramite_grado.create_tramite_grado(tramite_grado)


@router.get("/get_tramite_grado/{tramite_grado_id}", response_model=TramiteGrado)
async def get_tramite_grado(tramite_grado_id: int):
    return nuevo_tramite_grado.get_tramite_grado(tramite_grado_id)


@router.get("/get_tramites_grado/")
async def get_tramites_grado():
    return nuevo_tramite_grado.get_tramites_grado()


@router.put("/update_tramite_grado/{tramite_grado_id}")
async def update_tramite_grado(tramite_grado_id: int, tramite_grado: TramiteGrado):
    return nuevo_tramite_grado.update_tramite_grado(tramite_grado_id, tramite_grado)


@router.delete("/delete_tramite_grado/{tramite_grado_id}")
async def delete_tramite_grado(tramite_grado_id: int):
    return nuevo_tramite_grado.delete_tramite_grado(tramite_grado_id)