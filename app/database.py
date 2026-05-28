import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# ----------------------------------------
#     Configuración PostgreSQL
# -----------------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL enviroment variable is not set")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    """
    Abre una sesión de base de datos y la cierra al terminar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
