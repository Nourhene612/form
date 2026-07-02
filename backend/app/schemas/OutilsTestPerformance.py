from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

class OutilTestPerformanceCreate(BaseModel):
    nom: str

class OutilTestPerformanceUpdate(BaseModel):
    nom: str | None = None

class OutilTestPerformanceResponse(BaseModel):
    id: UUID
    nom: str
    performance_id: UUID

    model_config = ConfigDict(from_attributes=True)