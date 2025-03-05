from datetime import datetime

dates = ['2024-04-12', '2024-03-03', '2024-01-03', '2024-01-04', '2024-01-05',
         '2024-11-16', '2024-1-7', '2024-07-04', '2024-12-25', '2024-01-10']

# Convert date strings to date objects
dates = [datetime.strptime(date_str, "%Y-%m-%d").date() for date_str in dates]

# Format the date objects in "m/d/yyyy" format with single-digit months and days
formatted_dates = [date.strftime("%#m/%#d/%Y") for date in dates]

for date in formatted_dates:
    print(date)