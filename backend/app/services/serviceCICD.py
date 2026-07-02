from sqlalchemy.orm import Session
from uuid import UUID

from app.models.CICD import CICD
from app.schemas.CICD import CICDCreate, CICDUpdate
from .base import CRUDBase


class CRUDCICD(CRUDBase):

    def create(self, db: Session, data: CICDCreate):
        obj = CICD(
            utiliseCICD=data.utiliseCICD,
            outil=data.outil,
            testPerformanceIntegre=data.testPerformanceIntegre,
            momentTest=data.momentTest,
            distributionCharge=data.distributionCharge,
            informations_id=data.informations_id
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def update(self, db: Session, id: UUID, data: CICDUpdate):
        obj = db.get(CICD, id)

        if not obj:
            raise ValueError("CICD not found")

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(obj, key, value)

        db.commit()
        db.refresh(obj)
        return obj
    def get_by_informations_id(self, db: Session, informations_id: UUID):
     return db.query(CICD).filter(
        CICD.informations_id == informations_id
    ).first()

cicd_service = CRUDCICD(CICD)

# Compatibilité avec les imports existants
cicd = cicd_service