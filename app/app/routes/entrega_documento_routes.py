from fastapi import APIRouter
from controllers.entrega_documento_controller import *
from models.entrega_documento_model import EntregaDocumento

router = APIRouter()

nueva_entrega_documento = EntregaDocumentoController()


@router.post("/create_entrega_documento")
async def create_entrega_documento(entrega_documento: EntregaDocumento):
    return nueva_entrega_documento.create_entrega_documento(entrega_documento)


@router.get("/get_entrega_documento/{entrega_documento_id}", response_model=EntregaDocumento)
async def get_entrega_documento(entrega_documento_id: int):
    return nueva_entrega_documento.get_entrega_documento(entrega_documento_id)


@router.get("/get_entregas_documento/")
async def get_entregas_documento():
    return nueva_entrega_documento.get_entregas_documento()


@router.put("/update_entrega_documento/{entrega_documento_id}")
async def update_entrega_documento(entrega_documento_id: int, entrega_documento: EntregaDocumento):
    return nueva_entrega_documento.update_entrega_documento(entrega_documento_id, entrega_documento)


@router.delete("/delete_entrega_documento/{entrega_documento_id}")
async def delete_entrega_documento(entrega_documento_id: int):
    return nueva_entrega_documento.delete_entrega_documento(entrega_documento_id)