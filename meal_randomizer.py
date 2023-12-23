"""
GOAL: Adding prep time limits and day exclusions to a previous script to randomize evening dinners.
"""

from random import shuffle
from datetime import datetime, timedelta
from meals import meals_and_prep_times

max_prep_time = 45
skip_days = ["Wed", "Sun"]

meals_filtered = [k for k, v in meals_and_prep_times.items() if v < max_prep_time]
shuffle(meals_filtered)

today = datetime.today()
tomorrow = today - timedelta(-1)

for i in range(7):
    d = today - timedelta(days=-i)  # starting today
    d = tomorrow - timedelta(days=-i)  # starting tomorrow
    d = d.strftime("%a")  # short form (i.e. Wed: %A for Wednesday)
    if d in skip_days:
        print(f"{d}: ----")
    else:
        print(f"{d}: {meals_filtered[i]}")
