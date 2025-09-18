from sqlalchemy import Integer,String,Column
from app.database import Base

class Patient(Base):
    __tablename__="Patients"
    id =Column(Integer,primary_key=True,index=True)
    name=Column(String, index=True)
    age=Column(Integer)
    sex=Column(String)
    contact=Column(String)

