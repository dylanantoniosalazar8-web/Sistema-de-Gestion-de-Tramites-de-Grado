from fastapi import APIRouter
from controllers.tipo_paz_ysalvo_controller import *
from models.tipo_paz_ysalvo_model import TipoPazYSalvo

router = APIRouter()

nuevo_tipo_paz_ysalvo = TipoPazYSalvoController()


@router.post("/create_tipo_paz_ysalvo")
async def create_tipo_paz_ysalvo(tipo_paz_ysalvo: TipoPazYSalvo):
    return nuevo_tipo_paz_ysalvo.create_tipo_paz_ysalvo(tipo_paz_ysalvo)


@router.get("/get_tipo_paz_ysalvo/{tipo_paz_ysalvo_id}", response_model=TipoPazYSalvo)
async def get_tipo_paz_ysalvo(tipo_paz_ysalvo_id: int):
    return nuevo_tipo_paz_ysalvo.get_tipo_paz_ysalvo(tipo_paz_ysalvo_id)


@router.get("/get_tipos_paz_ysalvo/")
async def get_tipos_paz_ysalvo():
    return nuevo_tipo_paz_ysalvo.get_tipos_paz_ysalvo()


@router.put("/update_tipo_paz_ysalvo/{tipo_paz_ysalvo_id}")
async def update_tipo_paz_ysalvo(tipo_paz_ysalvo_id: int, tipo_paz_ysalvo: TipoPazYSalvo):
    return nuevo_tipo_paz_ysalvo.update_tipo_paz_ysalvo(tipo_paz_ysalvo_id, tipo_paz_ysalvo)


@router.delete("/delete_tipo_paz_ysalvo/{tipo_paz_ysalvo_id}")
async def delete_tipo_paz_ysalvo(tipo_paz_ysalvo_id: int):
    return nuevo_tipo_paz_ysalvo.delete_tipo_paz_ysalvo(tipo_paz_ysalvo_id)