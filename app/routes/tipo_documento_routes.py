<<<<<<< HEAD
from fastapi import APIRouter
from controllers.tramite_grado_controller import *
from models.tramite_grado_model import TramiteGrado

router = APIRouter()

nuevo_tramite_grado = TramiteGradoController()


@router.post("/create_tramite_grado")
async def create_tramite_grado(tramite_grado: TramiteGrado):
    return nuevo_tramite_grado.create_tramite_grado(tramite_grado)


@router.get("/get_tramite_grado/{tramite_grado_id}", response_model=TramiteGrado)
async def get_tramite_grado(tramite_grado_id: int):
    return nuevo_tramite_grado.get_tramite_grado(tramite_grado_id)


@router.get("/get_tramites_grado/")
async def get_tramites_grado():
    return nuevo_tramite_grado.get_tramites_grado()


@router.put("/update_tramite_grado/{tramite_grado_id}")
async def update_tramite_grado(tramite_grado_id: int, tramite_grado: TramiteGrado):
    return nuevo_tramite_grado.update_tramite_grado(tramite_grado_id, tramite_grado)


@router.delete("/delete_tramite_grado/{tramite_grado_id}")
async def delete_tramite_grado(tramite_grado_id: int):
    return nuevo_tramite_grado.delete_tramite_grado(tramite_grado_id)
=======
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
>>>>>>> 2f020c94eabd9dc0d1eec678067809b240c8663f
