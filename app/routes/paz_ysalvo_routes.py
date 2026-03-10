from fastapi import APIRouter
from controllers.paz_ysalvo_controller import *
from models.paz_ysalvo_model import PazYSalvo

router = APIRouter()

nuevo_paz_ysalvo = PazYSalvoController()


@router.post("/create_paz_ysalvo")
async def create_paz_ysalvo(paz_ysalvo: PazYSalvo):
    return nuevo_paz_ysalvo.create_paz_ysalvo(paz_ysalvo)


@router.get("/get_paz_ysalvo/{paz_ysalvo_id}", response_model=PazYSalvo)
async def get_paz_ysalvo(paz_ysalvo_id: int):
    return nuevo_paz_ysalvo.get_paz_ysalvo(paz_ysalvo_id)


@router.get("/get_pazes_ysalvo/")
async def get_pazes_ysalvo():
    return nuevo_paz_ysalvo.get_pazes_ysalvo()


@router.put("/update_paz_ysalvo/{paz_ysalvo_id}")
async def update_paz_ysalvo(paz_ysalvo_id: int, paz_ysalvo: PazYSalvo):
    return nuevo_paz_ysalvo.update_paz_ysalvo(paz_ysalvo_id, paz_ysalvo)


@router.delete("/delete_paz_ysalvo/{paz_ysalvo_id}")
async def delete_paz_ysalvo(paz_ysalvo_id: int):
    return nuevo_paz_ysalvo.delete_paz_ysalvo(paz_ysalvo_id)