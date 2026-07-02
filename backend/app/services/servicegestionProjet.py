from .base import CRUDBase
from app.models.GestionProjet import GestionProjet
from app.models.OutilGestionProjet import OutilGestionProjet
from app.models.IntegrationOutils import IntegrationOutils
from app.schemas.GestionProjet import GestionProjetCreate, GestionProjetUpdate
from sqlalchemy.orm import Session
from uuid import UUID

class CRUDGestionProjet(CRUDBase):
    def create(self, db: Session, data: GestionProjetCreate):
        obj = GestionProjet(
            typeMethode=data.typeMethode,
            outil_gestion=data.outil_gestion,
            aspects_couverts=data.aspects_couverts,
            informations_id=data.informations_id,
            outils=[OutilGestionProjet(nom=o.nom) for o in data.outils],
            integrations=[IntegrationOutils(typeIntegration=i.typeIntegration) for i in data.integrations]
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, id: UUID, data: GestionProjetUpdate):
        obj = db.get(GestionProjet, id)
        for key, value in data.model_dump(exclude_unset=True).items():
            if key not in ("outils", "integrations"):
                setattr(obj, key, value)
        if data.outils is not None:
            obj.outils.clear()
            obj.outils = [OutilGestionProjet(nom=o.nom) for o in data.outils]
        if data.integrations is not None:
            obj.integrations.clear()
            obj.integrations = [IntegrationOutils(typeIntegration=i.typeIntegration) for i in data.integrations]
        db.commit()
        db.refresh(obj)
        return obj

gestion_projet_service = CRUDGestionProjet(GestionProjet)

# Compatibilité avec les imports existants
gestion_projet = gestion_projet_service