from pydantic import BaseModel
class PatientBase(BaseModel):
    name:str
    age:int
    sex:str
    contact:str
class CreatePatient(PatientBase):
    pass
class Patient(PatientBase):
    id:int
class config:
    orm_mode=True