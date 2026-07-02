from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid  

class OutilTestPerformance(Base):
    __tablename__ = "outil_test_performance"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = Column(String, nullable=False)

    performance_id = Column(UUID(as_uuid=True), ForeignKey("performance.id"), nullable=False)
    performance = relationship("Performance", back_populates="outils")