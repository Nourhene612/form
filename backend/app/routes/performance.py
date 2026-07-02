from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas.performance import PerformanceCreate, PerformanceUpdate, PerformanceResponse
from app.services import serviceperformance

router = APIRouter(
    prefix="/performance",
    tags=["Performance"]
)


# ✅ CREATE
@router.post("/", response_model=PerformanceResponse)
def create_performance(data: PerformanceCreate, db: Session = Depends(get_db)):
    return serviceperformance.create(db, data)


# ✅ GET BY ID
@router.get("/{id}", response_model=PerformanceResponse)
def get_performance(id: UUID, db: Session = Depends(get_db)):
    obj = serviceperformance.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="Performance not found")
    return obj


# ✅ GET ALL
@router.get("/", response_model=list[PerformanceResponse])
def get_all_performance(db: Session = Depends(get_db)):
    return serviceperformance.get_all(db)


# ✅ UPDATE
@router.put("/{id}", response_model=PerformanceResponse)
def update_performance(id: UUID, data: PerformanceUpdate, db: Session = Depends(get_db)):
    obj = serviceperformance.update(db, id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Performance not found")
    return obj


#  DELETE
@router.delete("/{id}")
def delete_performance(id: UUID, db: Session = Depends(get_db)):
    obj = serviceperformance.delete(db, id)
    if obj is None:
        raise HTTPException(status_code=404, detail="Performance not found")
    return {"message": "Deleted successfully"}