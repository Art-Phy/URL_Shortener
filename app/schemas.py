
from pydantic import BaseModel, HttpUrl
from datetime import datetime

# ---------------------------------------------------------------------
#    Esquemas Pydantic para validar datos que entran/salen de la API
# ---------------------------------------------------------------------

class URLCreate(BaseModel):
    original_url: HttpUrl # valida que sea URL real



class URLInfo(BaseModel):
    id: int
    original_url: str
    short_url: str
    clicks: int
    created_at: datetime | None = None
    last_accessed: datetime | None = None

    class Config:
        from_attributes = True # permite devolver objetos SQLAlchemy convertidos a JSON
