from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import *
from app.models import *
from app.schemas import *
from app.database import get_db

router =APIRouter()

@router.get("/patients",response_model=list[Patient])
def get_patient(skip: int=10,limit: int=10, db: Session =Depends(get_db)): 
    return get_patients(db, skip=skip, limit=limit)

@router.post("/patients", response_model=Patient)
def create_patient(patient: CreatePatient, db: Session = Depends(get_db)):
    return create_patient(db=db, patient=patient)