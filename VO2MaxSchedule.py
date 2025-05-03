from datetime import datetime, timedelta
import json

def weeklySchedule(day: datetime):

  weeklyWorkouts = {}
  weeklyWorkouts[day] = "Rest"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "8 x 30s All-Out Sprints"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Rest"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "Rest"
  day += timedelta(days = 1)
  weeklyWorkouts[day] = "6 x 400m 5k Pace (4:01-4:22 /km)"
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
with open("VO2MaxData.json", "w") as f:
  json.dump(json_dict, f)