from sqlalchemy.orm import Session
from uuid import UUID

from app.models.TestsFonctionnels import TestsFonctionnels
from app.models.OutilsTestFonctionnel import OutilTestFonctionnel
from app.schemas.TestsFonctionnel import (
    TestsFonctionnelsCreate,
    TestsFonctionnelsPatch,
    TestsFonctionnelsUpdate,
)
from .base import CRUDBase


class CRUDTestsFonctionnels(CRUDBase):

    def create(self, db: Session, data: TestsFonctionnelsCreate):
        obj = TestsFonctionnels(
            anomaliesProduction=data.anomaliesProduction,
            testsFonctionnelsRealises=data.testsFonctionnelsRealises,
            typeTest=data.typeTest,
            informations_id=data.informations_id,
            outils=[
                OutilTestFonctionnel(nom=o.nom)
                for o in data.outils
            ],
        )

        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def get(self, db: Session, id: UUID):
        return db.query(TestsFonctionnels).filter(
            TestsFonctionnels.id == id
        ).first()

    def get_by_informations_id(self, db: Session, informations_id: UUID):
        return db.query(TestsFonctionnels).filter(
            TestsFonctionnels.informations_id == informations_id
        ).first()

    def update(self, db: Session, id: UUID, data: TestsFonctionnelsUpdate):
        obj = self.get(db, id)

        if not obj:
            raise ValueError("TestsFonctionnels not found")

        obj.anomaliesProduction = data.anomaliesProduction
        obj.testsFonctionnelsRealises = data.testsFonctionnelsRealises
        obj.typeTest = data.typeTest

        if data.outils is not None:
            obj.outils.clear()
            obj.outils = [
                OutilTestFonctionnel(nom=o.nom)
                for o in data.outils
            ]

        db.commit()
        db.refresh(obj)
        return obj

    def patch(self, db: Session, id: UUID, data: TestsFonctionnelsPatch):
        obj = self.get(db, id)

        if not obj:
            raise ValueError("TestsFonctionnels not found")

        update_data = data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            if key != "outils":
                setattr(obj, key, value)

        if data.outils is not None:
            obj.outils.clear()
            obj.outils = [
                OutilTestFonctionnel(nom=o.nom)
                for o in data.outils
            ]

        db.commit()
        db.refresh(obj)
        return obj


tests_fonctionnels_service = CRUDTestsFonctionnels(TestsFonctionnels)