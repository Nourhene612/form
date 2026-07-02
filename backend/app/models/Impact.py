from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid  


class Impact(Base):
    __tablename__ = "impact"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombreRessources = Column(Integer, nullable=True)
    coutIncident = Column(Float, nullable=True)
    tempsResolution = Column(String, nullable=True)
    causesRework = Column(String, nullable=True)
    problemeRessources = Column(String, nullable=True)

    informations_id = Column(UUID(as_uuid=True), ForeignKey("informations_generales.idEvaluation"), nullable=False)
    informations = relationship("InformationsGenerales", back_populates="impact")