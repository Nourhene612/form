from app.models.performance import Performance
from app.models.OutilTestPerformance import OutilTestPerformance
from app.schemas.performance import PerformanceCreate, PerformanceUpdate
from sqlalchemy.orm import Session
from uuid import UUID

def create(db: Session, data: PerformanceCreate):
    obj = Performance(
        degradationPerformance=data.degradationPerformance,
        impactVentes=data.impactVentes,
        testsChargeRealises=data.testsChargeRealises,
        typeTestCharge=data.typeTestCharge,
        informations_id=data.informations_id,
        outils=[OutilTestPerformance(nom=o.nom) for o in data.outils]
    )
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_by_id(db: Session, id: UUID):
    return db.get(Performance, id)

def get_all(db: Session):
    return db.query(Performance).all()

def update(db: Session, id: UUID, data: PerformanceUpdate):
    obj = db.get(Performance, id)
    if not obj:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        if key != "outils":
            setattr(obj, key, value)
    if data.outils is not None:
        obj.outils.clear()
        obj.outils = [OutilTestPerformance(nom=o.nom) for o in data.outils]
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, id: UUID):
    obj = db.get(Performance, id)
    if not obj:
        return None
    db.delete(obj)
    db.commit()