from fastapi import FastAPI
from routes.estudiante_routes import router as estudiante_router
from routes.documento_requerido_routes import router as documento_requerido_router
from routes.facultad_routes import router as facultad_router
from routes.ceremonia_grado_routes import router as ceremonia_grado_router
from routes.asignacion_ceremonia_routes import router as asignacion_ceremonia_router
from routes.programa_routes import router as programa_router
from routes.pago_tramite_routes import router as pago_tramite_router
from routes.paz_ysalvo_routes import router as paz_ysalvo_router
from routes.tramite_grado_routes import router as tramite_grado_router
from routes.tipo_documento_routes import router as tipo_documento_router
from routes.tipo_paz_ysalvo_routes import router as tipo_paz_ysalvo_router
from routes.tipo_grado_routes import router as tipo_grado_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API de trámites funcionando correctamente"}

origins = ["*"]
    

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(estudiante_router)
app.include_router(documento_requerido_router)
app.include_router(facultad_router)
app.include_router(ceremonia_grado_router)
app.include_router(asignacion_ceremonia_router)
app.include_router(programa_router)
app.include_router(pago_tramite_router)
app.include_router(paz_ysalvo_router)
app.include_router(tramite_grado_router)
app.include_router(tipo_documento_router)
app.include_router(tipo_paz_ysalvo_router)
app.include_router(tipo_grado_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
