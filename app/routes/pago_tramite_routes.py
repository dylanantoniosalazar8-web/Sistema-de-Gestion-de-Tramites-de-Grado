from fastapi import APIRouter
from controllers.pago_tramite_controller import *
from models.pago_tramite_model import PagoTramite

router = APIRouter()

nuevo_pago_tramite = PagoTramiteController()


@router.post("/create_pago_tramite")
async def create_pago_tramite(pago_tramite: PagoTramite):
    return nuevo_pago_tramite.create_pago_tramite(pago_tramite)


@router.get("/get_pago_tramite/{pago_tramite_id}", response_model=PagoTramite)
async def get_pago_tramite(pago_tramite_id: int):
    return nuevo_pago_tramite.get_pago_tramite(pago_tramite_id)


@router.get("/get_pagos_tramite/")
async def get_pagos_tramite():
    return nuevo_pago_tramite.get_pagos_tramite()


@router.put("/update_pago_tramite/{pago_tramite_id}")
async def update_pago_tramite(pago_tramite_id: int, pago_tramite: PagoTramite):
    return nuevo_pago_tramite.update_pago_tramite(pago_tramite_id, pago_tramite)


@router.delete("/delete_pago_tramite/{pago_tramite_id}")
async def delete_pago_tramite(pago_tramite_id: int):
    return nuevo_pago_tramite.delete_pago_tramite(pago_tramite_id)