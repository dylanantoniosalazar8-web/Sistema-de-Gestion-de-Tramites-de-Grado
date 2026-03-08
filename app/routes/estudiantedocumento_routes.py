from fastapi import APIRouter
from controllers.estudiantedocumento_controller import *
from models.estudiantedocumento_model import EstudianteDocumento

router = APIRouter()

nuevo_estudiante_documento = EstudianteDocumentoController()


@router.post("/create_estudiante_documento")
async def create_estudiante_documento(data: EstudianteDocumento):
    return nuevo_estudiante_documento.create_estudiante_documento(data)

@router.get("/get_estudiante_documento/{id}", response_model=EstudianteDocumento)
async def get_estudiante_documento(id: int):
    return nuevo_estudiante_documento.get_estudiante_documento(id)


@router.get("/get_estudiantes_documentos", response_model=list[EstudianteDocumento])
async def get_estudiantes_documentos():
    return nuevo_estudiante_documento.get_estudiantes_documentos()


@router.put("/update_estudiante_documento/{id}")
async def update_estudiante_documento(id: int, data: EstudianteDocumento):
    return nuevo_estudiante_documento.update_estudiante_documento(id, data)


@router.delete("/delete_estudiante_documento/{id}")
async def delete_estudiante_documento(id: int):
    return nuevo_estudiante_documento.delete_estudiante_documento(id)