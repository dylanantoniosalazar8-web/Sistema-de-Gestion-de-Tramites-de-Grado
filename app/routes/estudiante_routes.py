from fastapi import APIRouter
from controllers.estudiante_controller import *
from models.estudiante_model import Estudiante

router = APIRouter()

nuevo_estudiante = EstudianteController()


@router.post("/create_estudiante")
async def create_estudiante(estudiante: Estudiante):
    return nuevo_estudiante.create_estudiante(estudiante)


@router.get("/get_estudiante/{estudiante_id}", response_model=Estudiante)
async def get_estudiante(estudiante_id: int):
    return nuevo_estudiante.get_estudiante(estudiante_id)


@router.get("/get_estudiantes/")
async def get_estudiantes():
    return nuevo_estudiante.get_estudiantes()


@router.put("/update_estudiante/{estudiante_id}")
async def update_estudiante(estudiante_id: int, estudiante: Estudiante):
    return nuevo_estudiante.update_estudiante(estudiante_id, estudiante)


@router.delete("/delete_estudiante/{estudiante_id}")
async def delete_estudiante(estudiante_id: int):
    return nuevo_estudiante.delete_estudiante(estudiante_id)