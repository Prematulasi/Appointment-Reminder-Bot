from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    appointment_time = Column(DateTime)