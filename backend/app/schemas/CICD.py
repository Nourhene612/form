from pydantic import BaseModel, ConfigDict
from uuid import UUID
from enum import Enum



class MomentTestEnum(str, Enum):
    SHIFT_LEFT          = "Dès la phase de développement (Shift-left)"
    AVANT_PRODUCTION    = "Avant mise en production"
    APRES_INCIDENT      = "Après incident en production"

class DistributionChargeEnum(str, Enum):
    OUI             = "Oui"
    PARTIELLEMENT   = "Partiellement"
    NON             = "Non"


# ─────────────────────────────────────────
# CICD
# ─────────────────────────────────────────
class CICDCreate(BaseModel):
    utiliseCICD: bool | None = None
    outil: str | None = None  # str si AUTRE
    testPerformanceIntegre: bool | None = None
    momentTest: MomentTestEnum | None = None
    distributionCharge: DistributionChargeEnum | None = None
    informations_id: UUID


class CICDUpdate(BaseModel):
    utiliseCICD: bool | None = None
    outil: str | None = None
    testPerformanceIntegre: bool | None = None
    momentTest: MomentTestEnum | None = None
    distributionCharge: DistributionChargeEnum | None = None


class CICDResponse(BaseModel):
    id: UUID
    utiliseCICD: bool | None = None
    outil: str | None = None
    testPerformanceIntegre: bool | None = None
    momentTest: MomentTestEnum | None = None
    distributionCharge: DistributionChargeEnum | None = None
    informations_id: UUID

    model_config = ConfigDict(from_attributes=True)


CICDOut = CICDResponse