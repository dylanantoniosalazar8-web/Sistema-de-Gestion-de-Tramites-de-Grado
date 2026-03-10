from fastapi import APIRouter
from app.controllers.entrega_documento_controller import EntregaDocumentosController
from app.models.entrega_documento_model import EntregaDocumento

router = APIRouter()

controller = EntregaDocumentosController()


@router.post("/entregas_documentos")
def crear_entrega(entrega: EntregaDocumento):
    return controller.create_entrega(entrega)


@router.get("/entregas_documentos")
def listar_entregas():
    return controller.get_entregas()


@router.get("/entregas_documentos/{id_entrega}")
def obtener_entrega(id_entrega: int):
    return controller.get_entrega(id_entrega)


@router.put("/entregas_documentos/{id_entrega}")
def actualizar_entrega(id_entrega: int, entrega: EntregaDocumento):
    return controller.update_entrega(id_entrega, entrega)


@router.delete("/entregas_documentos/{id_entrega}")
def eliminar_entrega(id_entrega: int):
    return controller.delete_entrega(id_entrega)