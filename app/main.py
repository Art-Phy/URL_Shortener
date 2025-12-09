
from fastapi import FastAPI
from .database import Base, engine

# Crear tablas automáticamente (sólo en desarrollo)
Base.metadata.create_all(bind=engine)


# -------------------------------------------------
#    Punto de entradad de nuestra app FastApi
#    Endpoint simple para verificar que funciona
# -------------------------------------------------

app = FastAPI(
    title="URL Shortener API",
    description="Servicio para cortar URLs y obtener estadísticas.",
    version="0.1.0"
)

@app.get("/")
def root():
    """
    Endpoint básico para comprobar que el servidor está funcionando.
    Cuando accedamos a la ruta raíz ("/") nos devolverá un mensahe simple.
    """
    return {"message": "UR Shortener API listo para trabajar 🚀"}
