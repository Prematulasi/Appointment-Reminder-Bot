# Appointment-Reminder-Bot
Build a scheduling assistant that compresses appointment data and patient preferences, sending smart reminders efficiently.
# Appointment Reminder Bot

An automated chatbot-based appointment reminder system that schedules appointments and sends smart reminders via email.

## Features
- Add, update, cancel appointments
- Automated reminders
- Chatbot interaction
- Background scheduler

## Tech Stack
- Python
- FastAPI
- SQLite
- APScheduler

## Run Instructions
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
