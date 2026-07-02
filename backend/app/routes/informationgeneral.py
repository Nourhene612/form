from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas.InformationsGenerales import (
    InformationsGeneralesCreate,
    InformationsGeneralesUpdate,
    InformationsGeneralesResponse
)
from app.services.serviceInformationGenerales import informations_generales

router = APIRouter(
    prefix="/informations-generales",
    tags=["Informations Generales"]
)


#  CREATE
@router.post("/", response_model=InformationsGeneralesResponse)
def create_informations(data: InformationsGeneralesCreate, db: Session = Depends(get_db)):
    return informations_generales.create(db, data)


#  GET BY ID
@router.get("/{id}", response_model=InformationsGeneralesResponse)
def get_informations(id: UUID, db: Session = Depends(get_db)):
    obj = informations_generales.get(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    return obj


#  GET ALL
@router.get("/", response_model=list[InformationsGeneralesResponse])
def get_all_informations(db: Session = Depends(get_db)):
    return informations_generales.get_all(db)


#  UPDATE
@router.put("/{id}", response_model=InformationsGeneralesResponse)
def update_informations(id: UUID, data: InformationsGeneralesUpdate, db: Session = Depends(get_db)):
    try:
        return informations_generales.update(db, id, data)
    except ValueError:
        raise HTTPException(status_code=404, detail="Not found")


#  DELETE
@router.delete("/{id}")
def delete_informations(id: UUID, db: Session = Depends(get_db)):
    obj = informations_generales.get(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(obj)
    db.commit()
    return {"message": "Deleted successfully"}