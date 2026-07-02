from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas.Impact import ImpactCreate, ImpactUpdate, ImpactResponse
from app.services.serviceimpact import impact

router = APIRouter(
    prefix="/impact",
    tags=["Impact"]
)


#  CREATE
@router.post("/", response_model=ImpactResponse)
def create_impact(data: ImpactCreate, db: Session = Depends(get_db)):
    return impact.create(db, data)


#  GET BY informations_id 
@router.get("/by-informations/{informations_id}", response_model=ImpactResponse)
def get_impact_by_informations(informations_id: UUID, db: Session = Depends(get_db)):
    obj = impact.get_by_informations_id(db, informations_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Impact not found")
    return obj


#  UPDATE (par informations_id)
@router.put("/by-informations/{informations_id}", response_model=ImpactResponse)
def update_impact(informations_id: UUID, data: ImpactUpdate, db: Session = Depends(get_db)):
    try:
        return impact.update(db, informations_id, data)
    except ValueError:
        raise HTTPException(status_code=404, detail="Impact not found")


#  DELETE 
@router.delete("/by-informations/{informations_id}")
def delete_impact(informations_id: UUID, db: Session = Depends(get_db)):
    obj = impact.get_by_informations_id(db, informations_id)

    if not obj:
        raise HTTPException(status_code=404, detail="Impact not found")

    db.delete(obj)
    db.commit()
    return {"message": "Deleted successfully"}