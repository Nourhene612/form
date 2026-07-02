from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.schemas.TestsFonctionnel import (
    TestsFonctionnelsCreate,
    TestsFonctionnelsUpdate,
    TestsFonctionnelsPatch,
    TestsFonctionnelsRead
)
from app.services.servicetestfonctionnel import tests_fonctionnels_service
from app.database import get_db

router = APIRouter(prefix="/tests-fonctionnels", tags=["Tests Fonctionnels"])


# ─────────────────────────────
# CREATE
# ─────────────────────────────
@router.post("/", response_model=TestsFonctionnelsRead)
def create_tests_fonctionnels(
    data: TestsFonctionnelsCreate,
    db: Session = Depends(get_db)
):
    return tests_fonctionnels_service.create(db, data)


# ─────────────────────────────
# GET by ID
# ─────────────────────────────
@router.get("/{id}", response_model=TestsFonctionnelsRead)
def get_tests_fonctionnels(id: UUID, db: Session = Depends(get_db)):
    obj = tests_fonctionnels_service.get(db, id)

    if not obj:
        raise HTTPException(status_code=404, detail="Not found")

    return obj


# ─────────────────────────────
# GET by formulaire (IMPORTANT)
# ─────────────────────────────
@router.get("/formulaire/{informations_id}", response_model=TestsFonctionnelsRead)
def get_by_formulaire(informations_id: UUID, db: Session = Depends(get_db)):
    obj = tests_fonctionnels_service.get_by_informations_id(db, informations_id)

    if not obj:
        raise HTTPException(status_code=404, detail="Not found")

    return obj


# ─────────────────────────────
# UPDATE (PUT)
# ─────────────────────────────
@router.put("/{id}", response_model=TestsFonctionnelsRead)
def update_tests_fonctionnels(
    id: UUID,
    data: TestsFonctionnelsUpdate,
    db: Session = Depends(get_db)
):
    try:
        return tests_fonctionnels_service.update(db, id, data)
    except ValueError:
        raise HTTPException(status_code=404, detail="Not found")


# ─────────────────────────────
# PATCH 
# ─────────────────────────────
@router.patch("/{id}", response_model=TestsFonctionnelsRead)
def patch_tests_fonctionnels(
    id: UUID,
    data: TestsFonctionnelsPatch,
    db: Session = Depends(get_db)
):
    try:
        return tests_fonctionnels_service.patch(db, id, data)
    except ValueError:
        raise HTTPException(status_code=404, detail="Not found")


# ─────────────────────────────
# DELETE 
# ─────────────────────────────
@router.delete("/{id}")
def delete_tests_fonctionnels(id: UUID, db: Session = Depends(get_db)):
    obj = tests_fonctionnels_service.get(db, id)

    if not obj:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(obj)
    db.commit()

    return {"message": "Deleted successfully"}