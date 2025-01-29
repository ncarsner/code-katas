import datetime
import pytz

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Get the current date
today = datetime.date.today()
print("Today's date:", today)

# Create a specific date
specific_date = datetime.date(2023, 10, 1)
print("Specific date:", specific_date)

# Create a specific time
specific_time = datetime.time(14, 30, 45)
print("Specific time:", specific_time)

# Create a datetime object
specific_datetime = datetime.datetime(2023, 10, 1, 14, 30, 45)
print("Specific datetime:", specific_datetime)

# Calculate the difference between two dates
date1 = datetime.date(2023, 10, 1)
date2 = datetime.date(2023, 10, 15)
difference = date2 - date1
print("Difference between dates:", difference.days, "days")

# Add a time delta to a date
delta = datetime.timedelta(days=10)
new_date = today + delta
print("New date after adding 10 days:", new_date)

# Format a datetime object as a string
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted datetime:", formatted_datetime)

# Parse a string into a datetime object
date_string = "2023-10-01 14:30:45"
parsed_datetime = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_datetime)

# Get the current time in UTC
now_utc = datetime.datetime.utcnow()
print("Current UTC time:", now_utc)

# Get the current time with timezone info
now_with_tz = datetime.datetime.now(datetime.timezone.utc)
print("Current time with timezone:", now_with_tz)

# Convert a datetime object to a different timezone
utc_time = datetime.datetime.now(datetime.timezone.utc)
eastern = pytz.timezone("US/Eastern")
eastern_time = utc_time.astimezone(eastern)
print("Eastern time:", eastern_time)
