from datetime import datetime, timedelta
import json

def weeklySchedule(day: datetime):

  weeklyWorkouts = {}
  weeklyWorkouts[day] = "Legs & Glutes"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Rest"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Chest & Triceps"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Back & Biceps"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Rest"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Rest"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Rest"

  return weeklyWorkouts

start_date = datetime(2025, 4, 28)
weeklyWorkouts = weeklySchedule(start_date)

for day in weeklyWorkouts.values():
  print(day)

json_dict = {dt.strftime("%A"): value for dt, value in weeklyWorkouts.items()}
with open("workoutData.json", "w") as f:
  json.dump(json_dict, f)