from fastapi import APIRouter
from controllers.requisitogrado_controller import *
from models.requisitogrado_model import RequisitoGrado

router = APIRouter()

nuevo_requisito = RequisitoGradoController()


@router.post("/create_requisito")
async def create_requisito(requisito: RequisitoGrado):
    return nuevo_requisito.create_requisito(requisito)


@router.get("/get_requisito/{requisito_id}", response_model=RequisitoGrado)
async def get_requisito(requisito_id: int):
    return nuevo_requisito.get_requisito(requisito_id)


@router.get("/get_requisitos/")
async def get_requisitos():
    return nuevo_requisito.get_requisitos()


@router.put("/update_requisito/{requisito_id}")
async def update_requisito(requisito_id: int, requisito: RequisitoGrado):
    return nuevo_requisito.update_requisito(requisito_id, requisito)


@router.delete("/delete_requisito/{requisito_id}")
async def delete_requisito(requisito_id: int):
    return nuevo_requisito.delete_requisito(requisito_id)