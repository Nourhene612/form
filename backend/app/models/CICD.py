from sqlalchemy import (
    Column, String, Boolean, ForeignKey
)
from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class CICD(Base):
    __tablename__ = "cicd"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    utiliseCICD = Column(Boolean, nullable=True)
    outil = Column(String, nullable=True)
    testPerformanceIntegre = Column(Boolean, nullable=True)
    momentTest = Column(String, nullable=True)
    distributionCharge = Column("distributionCharge", String, nullable=True)
    informations_id = Column(UUID(as_uuid=True), ForeignKey("informations_generales.idEvaluation"), nullable=False)
    informations = relationship("InformationsGenerales", back_populates="cicd")
