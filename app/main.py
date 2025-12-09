
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from . import models, schemas
from .utils import generate_short_code

# Crear tablas automáticamente (sólo en desarrollo)
Base.metadata.create_all(bind=engine)


# -------------------------------------------------
#    Punto de entradad de nuestra app FastApi
# -------------------------------------------------

app = FastAPI(
    title="URL Shortener API",
    description="Servicio para cortar URLs y obtener estadísticas.",
    version="0.1.0"
)


# -------------------
#    Endpoint raíz
# -------------------
@app.get("/")
def root():
    """
    Endpoint básico para comprobar que el servidor está funcionando.
    Cuando accedamos a la ruta raíz ("/") nos devolverá un mensahe simple.
    """
    return {"message": "UR Shortener API listo para trabajar 🚀"}


# -------------------------------
#    Endpoint: Crear URL corta
# -------------------------------
@app.post("/shorten", response_model=schemas.URLInfo)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    """
    Crea una versión acortada de la URL enviada por el usuario.
    Genera un código aleatorio, lo guarda en la base de datos
    y devuelve la información completa del registro.
    """
    short = generate_short_code()

    db_url = models.URL(
        original_url=str(url.original_url), # convierte a string
        short_url=short,
        clicks=0
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    return db_url
