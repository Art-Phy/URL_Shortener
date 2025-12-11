
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime
from typing import List

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



# ----------------------------
#    Endpoint: Estadísticas
# ----------------------------
@app.get("/stats/code/{short_code}", response_model=schemas.URLInfo)
def get_url_stats(short_code: str, db: Session = Depends(get_db)):
    """
    Devuelve las estadísticas de una URL acortada.
    Incluye la URL original, el código corto y el número de clicks.
    """
    db_url = db.query(models.URL).filter(models.URL.short_url == short_code).first()

    if not db_url:
        raise HTTPException(status_code=404, detail="URL no encontrada 🥲")
    
    return db_url



# --------------------------------
#    Endpoint: Estadísticas-Top
# --------------------------------
@app.get("/stats/top", response_model=list[schemas.URLInfo])
def get_top_urls(limit: int = 10, db: Session = Depends(get_db)):
    """
    Devuelve las URLs más populares ordenadas por número de clics.
    El parámetro 'limit' permite controlar cuántos resultados se devuelven.
    """
    if limit <= 0:
        raise HTTPException(status_code=400, detail="El parámetro 'limit' debe ser mayor que 0")
    
    urls = (
        db.query(models.URL)
        .order_by(models.URL.clicks.desc())
        .limit(limit)
        .all()
    )

    return urls



# ------------------------------------
#    Endpoint: Estadísticas-Sumario
# ------------------------------------
@app.get("/stats/summary", response_model=schemas.SummaryInfo)
def get_summary(db: Session = Depends(get_db)):
    """
    Devuelve estadísticas globales del servicio:
    total de URLs, total de clics, media y URL más popular.
    """

    total_urls = db.query(models.URL).count()
    total_clicks = db.query(models.URL).with_entities(
        func.sum(models.URL.clicks)
    ).scalar() or 0

    average_clicks = total_clicks / total_urls if total_urls > 0 else 0

    most_clicked = (
        db.query(models.URL)
        .order_by(models.URL.clicks.desc())
        .first()
    )

    return {
        "total_urls": total_urls,
        "total_clicks": total_clicks,
        "average_clicks": average_clicks,
        "most_clicked": most_clicked
    }



# -------------------------------------------
#    Endpoint: Redirigir a la URL original
# -------------------------------------------
@app.get("/{short_code}")
def redirect_to_original(short_code: str, db: Session = Depends(get_db)):
    """
    Redirige a la URL original asociada al código corto.
    Aumenta el contador de clics antes de enviar la redirección.
    """
    db_url = db.query(models.URL).filter(models.URL.short_url == short_code).first()

    if not db_url:
        raise HTTPException(status_code=404, detail="URL no encontrada 🥲")
    
    # Aumentamos clicks
    db_url.clicks += 1
    db_url.last_accessed = datetime.utcnow()
    
    db.commit()
    db.refresh(db_url) # Fuerza a SQLAlchemy a cargar el valor actualizado

    return RedirectResponse(db_url.original_url)
