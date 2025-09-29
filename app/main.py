from typing import Union
import psycopg2
from app.models import Base
from app.database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import patients

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediTrack API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your React app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(patients.router)

@app.get("/")
def root():
   return {"Touch""VASU "}