from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid 

class OutilGestionProjet(Base):
    __tablename__ = "outil_gestion_projet"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = Column(String, nullable=False)

    gestion_projet_id = Column(UUID(as_uuid=True), ForeignKey("gestion_projet.id"), nullable=False)
    gestion_projet = relationship("GestionProjet", back_populates="outils")

