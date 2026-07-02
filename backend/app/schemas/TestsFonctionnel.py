from pydantic import BaseModel, ConfigDict
import uuid
import enum


class AnomaliesProductionEnum(str, enum.Enum):
    JAMAIS      = "Jamais"
    RAREMENT    = "Rarement"
    OUI_IMPACT  = "Oui, avec un impact sur les utilisateurs / le business"

class TestsFonctionnelsRealisesEnum(str, enum.Enum):
    TOUJOURS    = "Toujours"
    PARFOIS     = "Parfois"
    JAMAIS      = "Jamais"

class TypeTestEnum(str, enum.Enum):
    MANUELLEMENT    = "Manuellement"
    AUTOMATISES     = "Automatisés"
    LES_DEUX        = "Les deux"


# ─────────────────────────────────────────
# OutilTestFonctionnel
# ─────────────────────────────────────────
class OutilTestFonctionnelCreate(BaseModel):
    nom: str

class OutilTestFonctionnelUpdate(BaseModel):         # PUT — tous les champs
    nom: str

class OutilTestFonctionnelPatch(BaseModel):          # PATCH — champs optionnels
    nom: str| None = None

class OutilTestFonctionnelRead(BaseModel):
    id: uuid.UUID
    nom: str

    model_config = ConfigDict(from_attributes=True)

# Delete → pas de schéma, juste l'id dans l'URL : DELETE /outils/{id}


# ─────────────────────────────────────────
# TestsFonctionnels
# ─────────────────────────────────────────
class TestsFonctionnelsCreate(BaseModel):
    anomaliesProduction: AnomaliesProductionEnum | None = None
    testsFonctionnelsRealises: TestsFonctionnelsRealisesEnum | None = None
    typeTest: TypeTestEnum | None = None
    informations_id: uuid.UUID
    outils: list[OutilTestFonctionnelCreate] = []


class TestsFonctionnelsUpdate(BaseModel):
    anomaliesProduction: AnomaliesProductionEnum
    testsFonctionnelsRealises: TestsFonctionnelsRealisesEnum
    typeTest: TypeTestEnum
    outils: list[OutilTestFonctionnelCreate] = []



class TestsFonctionnelsPatch(BaseModel):
    anomaliesProduction: AnomaliesProductionEnum | None = None
    testsFonctionnelsRealises: TestsFonctionnelsRealisesEnum | None = None
    typeTest: TypeTestEnum | None = None
    outils: list[OutilTestFonctionnelCreate] | None = None


class TestsFonctionnelsRead(BaseModel):
    id: uuid.UUID
    anomaliesProduction: AnomaliesProductionEnum | None = None
    testsFonctionnelsRealises: TestsFonctionnelsRealisesEnum | None = None
    typeTest: TypeTestEnum | None = None
    informations_id: uuid.UUID
    outils: list[OutilTestFonctionnelRead] = []

    model_config = ConfigDict(from_attributes=True)

# Delete → pas de schéma, juste l'id dans l'URL : DELETE /tests-fonctionnels/{id}