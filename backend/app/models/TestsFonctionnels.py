from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid  

class TestsFonctionnels(Base):
    __tablename__ = "tests_fonctionnels"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    anomaliesProduction = Column(String, nullable=True)
    testsFonctionnelsRealises = Column(String, nullable=True)
    typeTest = Column(String, nullable=True)

    informations_id = Column(UUID(as_uuid=True), ForeignKey("informations_generales.idEvaluation"), nullable=False)
    informations = relationship("InformationsGenerales", back_populates="tests_fonctionnels")

    # 1-to-many → OutilTestFonctionnel
    outils = relationship("OutilTestFonctionnel", cascade="all, delete-orphan", back_populates="tests_fonctionnels")