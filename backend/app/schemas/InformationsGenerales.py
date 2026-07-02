from pydantic import BaseModel, ConfigDict, EmailStr
from uuid import UUID
from datetime import date
from typing import Optional 
class InformationsGeneralesBase(BaseModel):
    dateEvaluation: date
    nom: str
    prenom: str
    email: EmailStr

    mobile: Optional[str] = None
    entreprise: Optional[str] = None
    secteurActivite: Optional[str] = None 
class InformationsGeneralesCreate(InformationsGeneralesBase):
    pass
class InformationsGeneralesUpdate(BaseModel):
    dateEvaluation: Optional[date] = None
    nom: Optional[str] = None
    prenom: Optional[str] = None
    email: Optional[EmailStr] = None

    mobile: Optional[str] = None
    entreprise: Optional[str] = None
    secteurActivite: Optional[str] = None 
class InformationsGeneralesResponse(InformationsGeneralesBase):
    idEvaluation: UUID

    model_config = ConfigDict(from_attributes=True)