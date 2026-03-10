from fastapi import APIRouter
from controllers.facultad_controller import *
from models.facultad_model import Facultad

router = APIRouter()

nueva_facultad = FacultadController()


@router.post("/create_facultad")
async def create_facultad(facultad: Facultad):
    return nueva_facultad.create_facultad(facultad)


@router.get("/get_facultad/{facultad_id}", response_model=Facultad)
async def get_facultad(facultad_id: int):
    return nueva_facultad.get_facultad(facultad_id)


@router.get("/get_facultades/")
async def get_facultades():
    return nueva_facultad.get_facultades()


@router.put("/update_facultad/{facultad_id}")
async def update_facultad(facultad_id: int, facultad: Facultad):
    return nueva_facultad.update_facultad(facultad_id, facultad)


@router.delete("/delete_facultad/{facultad_id}")
async def delete_facultad(facultad_id: int):
    return nueva_facultad.delete_facultad(facultad_id)