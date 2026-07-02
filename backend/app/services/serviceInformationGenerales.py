from sqlalchemy.orm import Session
from uuid import UUID

from app.models.InformationsGenerales import InformationsGenerales
from app.schemas.InformationsGenerales import (
    InformationsGeneralesCreate,
    InformationsGeneralesUpdate
)
from .base import CRUDBase


class CRUDInformationsGenerales(CRUDBase):

    def create(self, db: Session, data: InformationsGeneralesCreate):
        obj = InformationsGenerales(
            dateEvaluation=data.dateEvaluation,
            nom=data.nom,
            prenom=data.prenom,
            email=data.email,
            mobile=data.mobile,
            entreprise=data.entreprise,
            secteurActivite=data.secteurActivite
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get(self, db: Session, id: UUID):
        return db.query(InformationsGenerales).filter(
            InformationsGenerales.idEvaluation == id
        ).first()

    def update(self, db: Session, id: UUID, data: InformationsGeneralesUpdate):
        obj = self.get(db, id)

        if not obj:
            raise ValueError("InformationsGenerales not found")

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)
        return obj


informations_generales_service = CRUDInformationsGenerales(InformationsGenerales)

# Compatibilité avec les imports existants
informations_generales = informations_generales_service