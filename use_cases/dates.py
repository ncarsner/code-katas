from datetime import datetime as dt, date, timedelta
import platform
import random
    
CURRENT_YEAR = dt.today().year
OS = "Windows" if platform.system() == "Windows" else None

start_date = date(CURRENT_YEAR, 1, 1)
end_date = date(CURRENT_YEAR, 12, 31)
date_range = (end_date - start_date).days

# Generate random, sorted dates within the range
dates = sorted(
    [start_date + timedelta(days=random.randint(0, date_range)) for _ in range(10)]
)

# Format dates based on OS (single-digit format for non-Windows)
format_string = "%m/%d/%Y" if OS == "Windows" else "%-m/%-d/%Y"
formatted_dates = [d.strftime(format_string) for d in dates]

for item in formatted_dates:
    print(item)