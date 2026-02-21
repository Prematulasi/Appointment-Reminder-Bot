from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from database import engine, SessionLocal
from models import Base, Appointment
from scheduler import schedule_reminder
    
app = FastAPI()
templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add")
def add_appointment(
    name: str = Form(...),
    email: str = Form(...),
    appointment_time: str = Form(...)
):
    db = SessionLocal()
    appointment_dt = datetime.strptime(appointment_time, "%Y-%m-%dT%H:%M")

    new_appointment = Appointment(
        name=name,
        email=email,
        appointment_time=appointment_dt
    )

    db.add(new_appointment)
    db.commit()

    schedule_reminder(email, name, appointment_dt)

    return {"message": "Appointment added & reminder scheduled!"}