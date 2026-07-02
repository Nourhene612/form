# services/base.py
from sqlalchemy.orm import Session
from uuid import UUID

class CRUDBase:
    def __init__(self, model):
        self.model = model

    def get_by_id(self, db: Session, id: UUID):
        return db.get(self.model, id)

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def delete(self, db: Session, id: UUID):
        obj = db.get(self.model, id)
        db.delete(obj)
        db.commit()