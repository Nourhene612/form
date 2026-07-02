from sqlalchemy import (
    Column, Integer, String, Boolean, Float, Date, ForeignKey
)
from sqlalchemy.orm import relationship 
from .base import Base  
from sqlalchemy.dialects.postgresql import UUID
import uuid  

class OutilTestFonctionnel(Base):
    __tablename__ = "outil_test_fonctionnel"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nom = Column(String, nullable=False)

    tests_fonctionnels_id = Column(UUID(as_uuid=True), ForeignKey("tests_fonctionnels.id"), nullable=False)
    tests_fonctionnels = relationship("TestsFonctionnels", back_populates="outils")