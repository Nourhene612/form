from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey, JSON
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid  

class GestionProjet(Base):
    __tablename__ = "gestion_projet"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    typeMethode = Column(String, nullable=True)
    outil_gestion = Column(String, nullable=True)
    aspects_couverts = Column(JSON, nullable=True)

    informations_id = Column(UUID(as_uuid=True), ForeignKey("informations_generales.idEvaluation"), nullable=False)
    informations = relationship("InformationsGenerales", back_populates="gestion_projet")

    # 1-to-many → OutilGestionProjet
    outils = relationship("OutilGestionProjet", cascade="all, delete-orphan", back_populates="gestion_projet")

    # 1-to-many → IntegrationOutils
    integrations = relationship("IntegrationOutils", cascade="all, delete-orphan", back_populates="gestion_projet")