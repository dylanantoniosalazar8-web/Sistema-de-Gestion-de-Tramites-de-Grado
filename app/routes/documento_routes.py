from fastapi import APIRouter
from controllers.documento_controller import *
from models.documento_model import Documento

router = APIRouter()

nuevo_documento = DocumentoController()


@router.post("/create_documento")
async def create_documento(documento: Documento):
    return nuevo_documento.create_documento(documento)


@router.get("/get_documento/{documento_id}", response_model=Documento)
async def get_documento(documento_id: int):
    return nuevo_documento.get_documento(documento_id)


@router.get("/get_documentos/")
async def get_documentos():
    return nuevo_documento.get_documentos()


@router.put("/update_documento/{documento_id}")
async def update_documento(documento_id: int, documento: Documento):
    return nuevo_documento.update_documento(documento_id, documento)


@router.delete("/delete_documento/{documento_id}")
async def delete_documento(documento_id: int):
    return nuevo_documento.delete_documento(documento_id)