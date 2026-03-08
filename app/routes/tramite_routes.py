from fastapi import APIRouter
from controllers.tramitegrado_controller import *
from models.tramitegrado_model import TramiteGrado

router = APIRouter()

nuevo_tramite = TramiteGradoController()


@router.post("/create_tramite")
async def create_tramite(tramite: TramiteGrado):
    return nuevo_tramite.create_tramite(tramite)


@router.get("/get_tramite/{tramite_id}", response_model=TramiteGrado)
async def get_tramite(tramite_id: int):
    return nuevo_tramite.get_tramite(tramite_id)


@router.get("/get_tramites/")
async def get_tramites():
    return nuevo_tramite.get_tramites()


@router.put("/update_tramite/{tramite_id}")
async def update_tramite(tramite_id: int, tramite: TramiteGrado):
    return nuevo_tramite.update_tramite(tramite_id, tramite)


@router.delete("/delete_tramite/{tramite_id}")
async def delete_tramite(tramite_id: int):
    return nuevo_tramite.delete_tramite(tramite_id)