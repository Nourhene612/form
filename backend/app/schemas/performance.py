from pydantic import BaseModel, ConfigDict
from uuid import UUID
from typing import List, Optional
from enum import Enum  
from .OutilsTestPerformance import OutilTestPerformanceCreate, OutilTestPerformanceResponse

class TestChargeRealisesEnum(str, Enum):
    toujours = "Toujours"
    parfois = "Parfois"
    jamais = "Jamais"

class degradationPerformanceEnum(str, Enum):
    jamais = "Jamais"
    rarement = "Rarement" 
    oui = "Oui, et cela a impacté nos ventes"

class TypeTestChargeEnum(str, Enum):
    manuel = "Manuellement"
    auto = "Automatisés"
    les_deux = "Les deux" 


class PerformanceBase(BaseModel):
    degradationPerformance: degradationPerformanceEnum
    impactVentes: Optional[bool] = None
    testsChargeRealises: Optional[TestChargeRealisesEnum] = None
    typeTestCharge: Optional[TypeTestChargeEnum] = None


class PerformanceCreate(PerformanceBase):
    informations_id: UUID
    outils: List[OutilTestPerformanceCreate] = []



class PerformanceUpdate(BaseModel):
    degradationPerformance: Optional[degradationPerformanceEnum] = None
    testsChargeRealises: Optional[TestChargeRealisesEnum] = None
    typeTestCharge: Optional[TypeTestChargeEnum] = None
    outils: Optional[List[OutilTestPerformanceCreate]] = None

   


class PerformanceResponse(BaseModel):
    id: UUID
    degradationPerformance: degradationPerformanceEnum
    impactVentes: Optional[bool] = None
    testsChargeRealises: Optional[TestChargeRealisesEnum] = None
    typeTestCharge: Optional[TypeTestChargeEnum] = None
    informations_id: UUID
    outils: List[OutilTestPerformanceResponse] = []

    model_config = ConfigDict(from_attributes=True)