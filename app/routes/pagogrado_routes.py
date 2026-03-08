from fastapi import APIRouter
from controllers.pagogrado_controller import *
from models.pagogrado_model import PagoGrado

router = APIRouter()

nuevo_pago = PagoGradoController()


@router.post("/create_pago")
async def create_pago(pago: PagoGrado):
    return nuevo_pago.create_pago(pago)

@router.get("/get_pago/{pago_id}", response_model=PagoGrado)
async def get_pago(pago_id: int):
    return nuevo_pago.get_pago(pago_id)


@router.get("/get_pagos", response_model=list[PagoGrado])
async def get_pagos():
    return nuevo_pago.get_pagos()


@router.put("/update_pago/{pago_id}")
async def update_pago(pago_id: int, pago: PagoGrado):
    return nuevo_pago.update_pago(pago_id, pago)


@router.delete("/delete_pago/{pago_id}")
async def delete_pago(pago_id: int):
    return nuevo_pago.delete_pago(pago_id)