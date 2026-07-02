from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas.CICD import CICDCreate, CICDUpdate, CICDResponse
from app.services.serviceCICD import cicd  

router = APIRouter(prefix="/cicd", tags=["CICD"])


#  CREATE
@router.post("/", response_model=CICDResponse)
def create_cicd(data: CICDCreate, db: Session = Depends(get_db)):
    return cicd.create(db, data)


#  GET BY ID
@router.get("/{id}", response_model=CICDResponse)
def get_cicd(id: UUID, db: Session = Depends(get_db)):
    obj = cicd.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="CICD not found")
    return obj


#  GET ALL
@router.get("/", response_model=list[CICDResponse])
def get_all_cicd(db: Session = Depends(get_db)):
    return cicd.get_all(db)


#  UPDATE
@router.put("/{id}", response_model=CICDResponse)
def update_cicd(id: UUID, data: CICDUpdate, db: Session = Depends(get_db)):
    try:
        return cicd.update(db, id, data)
    except ValueError:
        raise HTTPException(status_code=404, detail="CICD not found")


#  DELETE
@router.delete("/{id}")
def delete_cicd(id: UUID, db: Session = Depends(get_db)):
    cicd.delete(db, id)
    return {"message": "Deleted successfully"}


#  GET BY informations_id (IMPORTANT POUR TON PROJET)
@router.get("/by-informations/{informations_id}", response_model=CICDResponse)
def get_by_informations(informations_id: UUID, db: Session = Depends(get_db)):
    obj = cicd.get_by_informations_id(db, informations_id)
    if not obj:
        raise HTTPException(status_code=404, detail="CICD not found")
    return obj