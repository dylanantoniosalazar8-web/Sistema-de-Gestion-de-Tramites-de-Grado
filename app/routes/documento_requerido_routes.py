from fastapi import APIRouter
from controllers.documento_requerido_controller import *
from models.documento_requerido_model import DocumentoRequerido

router = APIRouter()

nuevo_documento_requerido = DocumentoRequeridoController()


@router.post("/create_documento_requerido")
async def create_documento_requerido(documento_requerido: DocumentoRequerido):
    return nuevo_documento_requerido.create_documento_requerido(documento_requerido)


@router.get("/get_documento_requerido/{documento_requerido_id}", response_model=DocumentoRequerido)
async def get_documento_requerido(documento_requerido_id: int):
    return nuevo_documento_requerido.get_documento_requerido(documento_requerido_id)


@router.get("/get_documentos_requeridos/")
async def get_documentos_requeridos():
    return nuevo_documento_requerido.get_documentos_requeridos()


@router.put("/update_documento_requerido/{documento_requerido_id}")
async def update_documento_requerido(documento_requerido_id: int, documento_requerido: DocumentoRequerido):
    return nuevo_documento_requerido.update_documento_requerido(documento_requerido_id, documento_requerido)


@router.delete("/delete_documento_requerido/{documento_requerido_id}")
async def delete_documento_requerido(documento_requerido_id: int):
    return nuevo_documento_requerido.delete_documento_requerido(documento_requerido_id)