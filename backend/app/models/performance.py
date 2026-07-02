from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid 

class Performance(Base):
    __tablename__ = "performance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    degradationPerformance = Column(String, nullable=True)
    impactVentes = Column(Boolean, nullable=True)
    testsChargeRealises = Column(String, nullable=True)
    typeTestCharge = Column(String, nullable=True)

    informations_id = Column(UUID(as_uuid=True), ForeignKey("informations_generales.idEvaluation"), nullable=False)
    informations = relationship("InformationsGenerales", back_populates="performance")

    # 1-to-many → OutilTestPerformance
    outils = relationship("OutilTestPerformance",  cascade="all, delete-orphan", back_populates="performance")