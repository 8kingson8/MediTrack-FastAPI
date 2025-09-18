from app import crud, schemas
from app.database import SessionLocal

# Get DB session
db = SessionLocal()

# 1️⃣ Create patient
new_patient = schemas.PatientCreate(
    name="Alice",
    age=28,
    gender="Female",
    contact="111222333"
)
created = crud.create_patient(db, new_patient)
print("Created:", created.id, created.name)

# 2️⃣ Get all patients
patients = crud.get_patients(db)
print("Patients:", patients)

# 3️⃣ Get one patient
patient = crud.get_patient(db, created.id)
print("Single Patient:", patient)

# 4️⃣ Delete patient
deleted = crud.delete_patient(db, created.id)
print("Deleted:", deleted)

db.close()