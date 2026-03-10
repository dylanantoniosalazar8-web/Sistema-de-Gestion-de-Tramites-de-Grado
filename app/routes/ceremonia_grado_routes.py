from fastapi import APIRouter
from app.controllers.ceremonia_grado_controller import CeremoniaGradoController
from app.models.ceremonia_grado_model import CeremoniaGrado

router = APIRouter()

controller = CeremoniaGradoController()


@router.post("/ceremonias")
def crear_ceremonia(ceremonia: CeremoniaGrado):
    return controller.create_ceremonia(ceremonia)


@router.get("/ceremonias")
def listar_ceremonias():
    return controller.get_ceremonias()


@router.get("/ceremonias/{id_ceremonia}")
def obtener_ceremonia(id_ceremonia: int):
    return controller.get_ceremonia(id_ceremonia)


@router.put("/ceremonias/{id_ceremonia}")
def actualizar_ceremonia(id_ceremonia: int, ceremonia: CeremoniaGrado):
    return controller.update_ceremonia(id_ceremonia, ceremonia)


@router.delete("/ceremonias/{id_ceremonia}")
def eliminar_ceremonia(id_ceremonia: int):
    return controller.delete_ceremonia(id_ceremonia)