from fastapi import APIRouter
from controllers.tipo_documento_controller import *
from models.tipo_documento_model import TipoDocumento

router = APIRouter()

nuevo_tipo_documento = TipoDocumentoController()


@router.post("/create_tipo_documento")
async def create_tipo_documento(tipo_documento: TipoDocumento):
    return nuevo_tipo_documento.create_tipo_documento(tipo_documento)


@router.get("/get_tipo_documento/{tipo_documento_id}", response_model=TipoDocumento)
async def get_tipo_documento(tipo_documento_id: int):
    return nuevo_tipo_documento.get_tipo_documento(tipo_documento_id)


@router.get("/get_tipos_documento/")
async def get_tipos_documento():
    return nuevo_tipo_documento.get_tipos_documento()


@router.put("/update_tipo_documento/{tipo_documento_id}")
async def update_tipo_documento(tipo_documento_id: int, tipo_documento: TipoDocumento):
    return nuevo_tipo_documento.update_tipo_documento(tipo_documento_id, tipo_documento)


@router.delete("/delete_tipo_documento/{tipo_documento_id}")
async def delete_tipo_documento(tipo_documento_id: int):
    return nuevo_tipo_documento.delete_tipo_documento(tipo_documento_id)