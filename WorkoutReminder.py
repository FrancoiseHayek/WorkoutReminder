import smtplib
from datetime import datetime
import json
import os
from zoneinfo import ZoneInfo
from email.message import EmailMessage

KM_TO_MI = 0.621371

daysOfTheWeek = {
  0: "Monday",
  1: "Tuesday",
  2: "Wednesday",
  3: "Thursday",
  4: "Friday",
  5: "Saturday",
  6: "Sunday"
}

def send_reminder(event, context):

  subscriber_email = os.getenv("SUBSCRIBER_EMAIL")

  # Email credentials
  email = os.getenv("SENDER_EMAIL")
  password = os.getenv("PASSWORD")

  # Read JSON and convert string keys back to datetime
  with open("runData.json", "r") as f:
    loaded_runs_json = json.load(f)

  with open("workoutData.json", "r") as f:
    loaded_workout_json = json.load(f)

  with open("VO2MaxData.json", "r") as f:
    loaded_vo2_json = json.load(f)

  # Convert string keys back to datetime objects
  runs_dict = {datetime.strptime(k, "%Y-%m-%d %H:%M:%S"): v for k, v in loaded_runs_json.items()}
  workout_dict = loaded_workout_json
  vo2_dict = loaded_vo2_json

  # Set up SMTP server
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(email, password)

  now_est = datetime.now(ZoneInfo("America/New_York"))

  today = datetime(2025, month=now_est.month, day=now_est.day)
  weekday = daysOfTheWeek[datetime.today().weekday()]

  run = runs_dict[today]
  workout = workout_dict[weekday]
  vo2 = vo2_dict[weekday]

  subject = "Today's Workout Sessions:" if (subscriber_email != os.getenv("TEST_SUBSCRIBER_EMAIL")) else "Hey, it's Francoise, send me a screenshot of this email pls" 

  # Send SMS as an email
  if run == "Rest":
    body = "\nRun: Rest\n"
  else:
    miles = max(float(run), 1.0) * KM_TO_MI
    body = f"\nRun: {run} km ({miles:.2f} mi)\n"

  body += "Workout: " + workout
  body += "\nVO2: " + vo2

  # msg = f"Subject:{subject}\n\n{body}"
  # server.sendmail(email, sms_gateway, msg)


  msg = EmailMessage()
  msg["Subject"] = subject
  msg["From"]    = email
  msg["To"]      = subscriber_email
  msg.set_content(body)
  
  server.send_message(msg)

  server.quit()

  return {"status": "Message sent"}