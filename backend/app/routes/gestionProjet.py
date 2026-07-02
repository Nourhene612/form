from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas.GestionProjet import (
    GestionProjetCreate,
    GestionProjetUpdate,
    GestionProjetResponse
)
from app.services.servicegestionProjet import gestion_projet

router = APIRouter(
    prefix="/gestion-projet",
    tags=["Gestion Projet"]
)


# ✅ CREATE
@router.post("/", response_model=GestionProjetResponse)
def create_gestion_projet(data: GestionProjetCreate, db: Session = Depends(get_db)):
    return gestion_projet.create(db, data)


# ✅ GET BY ID
@router.get("/{id}", response_model=GestionProjetResponse)
def get_gestion_projet(id: UUID, db: Session = Depends(get_db)):
    obj = gestion_projet.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="GestionProjet not found")
    return obj


# ✅ GET ALL
@router.get("/", response_model=list[GestionProjetResponse])
def get_all_gestion_projet(db: Session = Depends(get_db)):
    return gestion_projet.get_all(db)


# ✅ UPDATE
@router.put("/{id}", response_model=GestionProjetResponse)
def update_gestion_projet(id: UUID, data: GestionProjetUpdate, db: Session = Depends(get_db)):
    obj = gestion_projet.get_by_id(db, id)
    if not obj:
        raise HTTPException(status_code=404, detail="GestionProjet not found")

    return gestion_projet.update(db, id, data)


# ✅ DELETE
@router.delete("/{id}")
def delete_gestion_projet(id: UUID, db: Session = Depends(get_db)):
    obj = gestion_projet.get_by_id(db, id)

    if not obj:
        raise HTTPException(status_code=404, detail="GestionProjet not found")

    db.delete(obj)
    db.commit()
    return {"message": "Deleted successfully"}


# ✅ GET BY informations_id (TRÈS IMPORTANT pour ton projet)
@router.get("/by-informations/{informations_id}", response_model=GestionProjetResponse)
def get_by_informations(informations_id: UUID, db: Session = Depends(get_db)):
    obj = db.query(type(gestion_projet.model)).filter(
        gestion_projet.model.informations_id == informations_id
    ).first()

    if not obj:
        raise HTTPException(status_code=404, detail="GestionProjet not found")

    return obj