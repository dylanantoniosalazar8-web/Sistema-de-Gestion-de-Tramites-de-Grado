from fastapi import APIRouter
from controllers.tramiterequisito_controller import *
from models.tramiterequisito_model import TramiteRequisito

router = APIRouter()

nuevo_tramite_requisito = TramiteRequisitoController()


@router.post("/create_tramite_requisito")
async def create_tramite_requisito(data: TramiteRequisito):
    return nuevo_tramite_requisito.create_tramite_requisito(data)


@router.get("/get_tramite_requisito/{id}", response_model=TramiteRequisito)
async def get_tramite_requisito(id: int):
    return nuevo_tramite_requisito.get_tramite_requisito(id)

@router.get("/get_tramites_requisitos", response_model=list[TramiteRequisito])
async def get_tramites_requisitos():
    return nuevo_tramite_requisito.get_tramites_requisitos()


@router.put("/update_tramite_requisito/{id}")
async def update_tramite_requisito(id: int, data: TramiteRequisito):
    return nuevo_tramite_requisito.update_tramite_requisito(id, data)


@router.delete("/delete_tramite_requisito/{id}")
async def delete_tramite_requisito(id: int):
    return nuevo_tramite_requisito.delete_tramite_requisito(id)