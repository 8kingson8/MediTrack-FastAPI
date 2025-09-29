from app.models import * 
from app.schemas import *
from sqlalchemy.orm import Session
def get_patients(db:Session,skip: int=10,limit: int=10 ):
    return db.query(Patient).skip(skip).limit(limit).all()
def create_patient(db:Session,patinet:CreatePatient):
    db_patient=Patient(**patinet.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
