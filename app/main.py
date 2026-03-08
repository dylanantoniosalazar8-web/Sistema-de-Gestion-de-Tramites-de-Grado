from fastapi import FastAPI
from routes.estudiante_routes import router as estudiante_router
from routes.documento_routes import router as documento_router
from routes.estudiantedocumento_routes import router as estudiantedocumento_router
from routes.facultad_routes import router as facultad_router
from routes.jurado_routes import router as jurado_router
from routes.pagogrado_routes import router as pagogrado_router
from routes.programa_routes import router as programa_router
from routes.requisitogrado_routes import router as requisitogrado_router
from routes.sustentacion_routes import router as sustentancion_router
from routes.tramite_routes import router as tramite_router
from routes.tramiterequisito_routes import router as tramiterequisito_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API de trámites funcionando correctamente"}

origins = [
    #"http://localhost.tiangolo.com",
    "https://ep-square-flower-aiq3n3y4-pooler.c-4.us-east-1.aws.neon.tech",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documento_router)
app.include_router(estudiante_router)
app.include_router(estudiantedocumento_router)
app.include_router(facultad_router)
app.include_router(jurado_router)
app.include_router(pagogrado_router)
app.include_router(programa_router)
app.include_router(requisitogrado_router)
app.include_router(sustentancion_router)
app.include_router(tramite_router)
app.include_router(tramiterequisito_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
