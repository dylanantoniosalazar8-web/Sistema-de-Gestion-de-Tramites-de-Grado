from fastapi import APIRouter
from app.controllers.tipos_degrado_controller import TipoGradoController
from app.models.tipos_degrado_model import TipoGrado

router = APIRouter()

controller = TipoGradoController()


@router.post("/tipos_grado")
def crear_tipo_grado(tipo_grado: TipoGrado):
    return controller.create_tipo_grado(tipo_grado)


@router.get("/tipos_grado")
def listar_tipos_grado():
    return controller.get_tipos_grado()


@router.get("/tipos_grado/{id_tipo_grado}")
def obtener_tipo_grado(id_tipo_grado: int):
    return controller.get_tipo_grado(id_tipo_grado)


@router.put("/tipos_grado/{id_tipo_grado}")
def actualizar_tipo_grado(id_tipo_grado: int, tipo_grado: TipoGrado):
    return controller.update_tipo_grado(id_tipo_grado, tipo_grado)


@router.delete("/tipos_grado/{id_tipo_grado}")
def eliminar_tipo_grado(id_tipo_grado: int):
    return controller.delete_tipo_grado(id_tipo_grado)