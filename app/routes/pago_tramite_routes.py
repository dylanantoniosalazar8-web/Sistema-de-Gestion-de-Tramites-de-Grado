from fastapi import APIRouter
from app.controllers.pago_tramite_controller import PagoTramiteController
from app.models.pago_tramite_model import PagoTramite

router = APIRouter()

controller = PagoTramiteController()


@router.post("/pagos_tramite")
def crear_pago(pago: PagoTramite):
    return controller.create_pago(pago)


@router.get("/pagos_tramite")
def listar_pagos():
    return controller.get_pagos()


@router.get("/pagos_tramite/{id_pago}")
def obtener_pago(id_pago: int):
    return controller.get_pago(id_pago)


@router.put("/pagos_tramite/{id_pago}")
def actualizar_pago(id_pago: int, pago: PagoTramite):
    return controller.update_pago(id_pago, pago)


@router.delete("/pagos_tramite/{id_pago}")
def eliminar_pago(id_pago: int):
    return controller.delete_pago(id_pago)