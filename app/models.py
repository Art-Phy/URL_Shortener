
from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

# -----------------------------------------------
#       Modelo principal de URLs acortadas
#    Representa un registro en la tabla "urls"
# -----------------------------------------------


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key= True, index=True)
    original_url = Column(String, nullable=False)
    short_url = Column(String, unique=True, index=True, nullable=False)
    clicks = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_accessed = Column(DateTime(timezone=True), nullable=True)
