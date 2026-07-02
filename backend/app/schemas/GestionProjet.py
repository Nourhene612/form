from pydantic import BaseModel, ConfigDict
from uuid import UUID
from enum import Enum


class TypeMethodeEnum(str, Enum):
    AGILE       = "Agile (Scrum / Kanban)"
    CYCLE_V     = "Cycle en V (Waterfall)"
    HYBRIDE     = "Hybride"
    PAS_METHODE = "Pas de méthode définie"


# ─────────────────────────────────────────
# OutilGestionProjet
# ─────────────────────────────────────────
class OutilGestionProjetCreate(BaseModel):
    nom: str

class OutilGestionProjetUpdate(BaseModel):
    nom: str | None = None

class OutilGestionProjetRead(BaseModel):
    id: UUID
    nom: str
    gestion_projet_id: UUID

    model_config = ConfigDict(from_attributes=True)


# ─────────────────────────────────────────
# IntegrationOutils
# ─────────────────────────────────────────
class IntegrationOutilsCreate(BaseModel):
    typeIntegration: str

class IntegrationOutilsUpdate(BaseModel):
    typeIntegration: str | None = None

class IntegrationOutilsRead(BaseModel):
    id: UUID
    typeIntegration: str
    gestion_projet_id: UUID

    model_config = ConfigDict(from_attributes=True)


# ─────────────────────────────────────────
# GestionProjet
# ─────────────────────────────────────────
class GestionProjetCreate(BaseModel):
    typeMethode: TypeMethodeEnum | None = None
    outil_gestion: str | None = None
    aspects_couverts: list[str] | None = None
    informations_id: UUID
    outils: list[OutilGestionProjetCreate] = []
    integrations: list[IntegrationOutilsCreate] = []

class GestionProjetUpdate(BaseModel):
    typeMethode: TypeMethodeEnum | None = None
    outil_gestion: str | None = None
    aspects_couverts: list[str] | None = None
    outils: list[OutilGestionProjetCreate] | None = None
    integrations: list[IntegrationOutilsCreate] | None = None

class GestionProjetResponse(BaseModel):
    id: UUID
    typeMethode: TypeMethodeEnum | None = None
    outil_gestion: str | None = None
    aspects_couverts: list[str] | None = None
    informations_id: UUID
    outils: list[OutilGestionProjetRead] = []
    integrations: list[IntegrationOutilsRead] = []

    model_config = ConfigDict(from_attributes=True)


GestionProjetOut = GestionProjetResponse