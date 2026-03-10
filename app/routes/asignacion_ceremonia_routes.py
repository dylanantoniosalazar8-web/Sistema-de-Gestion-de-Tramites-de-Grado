from fastapi import APIRouter
from app.controllers.asignacion_ceremonia_controller import AsignacionCeremoniaController
from app.models.asignacion_ceremonia_model import AsignacionCeremonia

router = APIRouter()

controller = AsignacionCeremoniaController()


@router.post("/asignaciones")
def crear_asignacion(asignacion: AsignacionCeremonia):
    return controller.create_asignacion(asignacion)


@router.get("/asignaciones")
def listar_asignaciones():
    return controller.get_asignaciones()


@router.get("/asignaciones/{id_asignacion}")
def obtener_asignacion(id_asignacion: int):
    return controller.get_asignacion(id_asignacion)


@router.put("/asignaciones/{id_asignacion}")
def actualizar_asignacion(id_asignacion: int, asignacion: AsignacionCeremonia):
    return controller.update_asignacion(id_asignacion, asignacion)


@router.delete("/asignaciones/{id_asignacion}")
def eliminar_asignacion(id_asignacion: int):
    return controller.delete_asignacion(id_asignacion)