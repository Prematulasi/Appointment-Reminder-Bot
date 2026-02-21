from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

scheduler = BackgroundScheduler()
scheduler.start()

def send_email(to_email, name, time):
    msg = MIMEText(f"Hello {name},\nReminder: You have an appointment at {time}")
    msg['Subject'] = "Appointment Reminder"
    msg['From'] = "your_email@gmail.com"
    msg['To'] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your_email@gmail.com", "your_app_password")
        server.send_message(msg)

def schedule_reminder(to_email, name, appointment_time):
    scheduler.add_job(
        send_email,
        'date',
        run_date=appointment_time,
        args=[to_email, name, appointment_time]
    )