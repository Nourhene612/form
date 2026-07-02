from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid 

class InformationsGenerales(Base):
    __tablename__ = "informations_generales"

    idEvaluation = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    dateEvaluation = Column(Date, nullable=False)
    nom = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, nullable=False)
    mobile = Column(String, nullable=True)
    entreprise = Column(String, nullable=True)
    secteurActivite = Column(String, nullable=True)

    # Relations (1-to-1)
    performance = relationship("Performance", back_populates="informations", uselist=False)
    tests_fonctionnels = relationship("TestsFonctionnels", back_populates="informations", uselist=False)
    cicd = relationship("CICD", back_populates="informations", uselist=False)
    gestion_projet = relationship("GestionProjet", back_populates="informations", uselist=False)
    impact = relationship("Impact", back_populates="informations", uselist=False)