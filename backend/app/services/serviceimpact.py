from sqlalchemy.orm import Session
from uuid import UUID

from app.models.Impact import Impact
from app.schemas.Impact import ImpactCreate, ImpactUpdate
from .base import CRUDBase


class CRUDImpact(CRUDBase):

    def create(self, db: Session, data: ImpactCreate):
        obj = Impact(**data.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get_by_informations_id(self, db: Session, informations_id: UUID):
        return db.query(Impact).filter(
            Impact.informations_id == informations_id
        ).first()

    def update(self, db: Session, informations_id: UUID, data: ImpactUpdate):
        obj = self.get_by_informations_id(db, informations_id)

        if not obj:
            raise ValueError("Impact not found")

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)
        return obj


impact_service = CRUDImpact(Impact)

# Instance exportée pour usage standard
impact = impact_service