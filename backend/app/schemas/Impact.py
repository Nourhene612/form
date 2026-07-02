from pydantic import BaseModel, ConfigDict
from uuid import UUID
from enum import Enum



class ProblemeRessourcesEnum(str, Enum):
    MANQUE          = "Oui, manque de ressources (surcharge, lenteur)"
    SURDIMENSIONNE  = "Oui, surdimensionnement (coûts inutiles)"
    LES_DEUX        = "Les deux"
    NON             = "Non"


# ─────────────────────────────────────────
# Impact
# ─────────────────────────────────────────
class ImpactCreate(BaseModel):
    nombreRessources: int | None = None
    coutIncident: float | None = None
    tempsResolution: str | None = None        # texte libre (ex: "2 heures")
    causesRework: str | None = None   # str si AUTRE
    problemeRessources: ProblemeRessourcesEnum | None = None
    informations_id: UUID


class ImpactUpdate(BaseModel):
    nombreRessources: int | None = None
    coutIncident: float | None = None
    tempsResolution: str | None = None
    causesRework: str | None = None
    problemeRessources: ProblemeRessourcesEnum | None = None


class ImpactResponse(BaseModel):
    id: UUID
    nombreRessources: int | None = None
    coutIncident: float | None = None
    tempsResolution: str | None = None
    causesRework: str | None = None
    problemeRessources: ProblemeRessourcesEnum | None = None
    informations_id: UUID

    model_config = ConfigDict(from_attributes=True)