from datetime import datetime, timedelta
import json

MARATHON_KM = 42
EASY_RUN_MAX = 5
MED_RUN_MAX = 10
KM_TO_MI = 0.621371
NUM_TRAINING_WEEKS = 49

start_date = datetime(2024, 12, 9)
race_date = datetime(2025, 12, 14)

print("Start date: " + start_date.strftime("%c"))
print("Race date: " + race_date.strftime("%c"))

def weeklySchedule(factor: float, day: datetime):

  global taperCount
  if factor > NUM_TRAINING_WEEKS:
    taperCount += 13
    factor = NUM_TRAINING_WEEKS - taperCount
  
  factor /= NUM_TRAINING_WEEKS

  weeklyRuns = {}
  weeklyRuns[day] = "Rest"
  day += timedelta(days = 1)
  weeklyRuns[day] = "{km:2.1f}".format(km = max(float(round(factor * EASY_RUN_MAX)), 1.0))
  day += timedelta(days = 1)
  weeklyRuns[day] = "Rest"
  day += timedelta(days = 1)
  weeklyRuns[day] = "{km:2.1f}".format(km = max(float(round(factor * MED_RUN_MAX)), 1.0))
  day += timedelta(days = 1)
  weeklyRuns[day] = "Rest"
  day += timedelta(days = 1)
  weeklyRuns[day] = "{km:2.1f}".format(km = max(float(round(factor * MARATHON_KM)), 1.0))
  day += timedelta(days = 1)
  weeklyRuns[day] = "Rest"
  
  return weeklyRuns

taperCount = 0
runs = {}

week = start_date
for i in range(1, NUM_TRAINING_WEEKS + 5):
  weeklyRuns = weeklySchedule(i, week)
  print("Week of", week.strftime("%m-%d") + " (km): ", end="| ")
  for day in weeklyRuns.values():
    print(day.center(6), end=" | ")
  print()
  runs = runs | weeklyRuns
  week += timedelta(weeks = 1)


json_dict = {dt.strftime("%Y-%m-%d %H:%M:%S"): value for dt, value in runs.items()}
with open("runData.json", "w") as f:
  json.dump(json_dict, f)
