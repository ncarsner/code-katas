import random
import pandas as pd
from datetime import datetime, timedelta


first_three = slice(0, 3)
middle_section = slice(3, -3)
last_three = slice(-3, None)

example_list = [random.randint(0, 100) for _ in range(10)]
example_list.sort()

print(f"\n{example_list=}")
print("\nFirst:", example_list[first_three])
print("Middle:", example_list[middle_section])
print("Last:", example_list[last_three])


def get_slice(data, slice_obj):
    return data[slice_obj]


selection = random.choice([first_three, middle_section, last_three])
selection_name = next(
    name
    for slc, name in [
        (first_three, "first_three"),
        (middle_section, "middle_section"),
        (last_three, "last_three"),
    ]
    if slc == selection
)
print(f"\n{selection_name=}, {get_slice(example_list, selection)}")


"""Logging example with reusable slices."""
timestamp_slice = slice(0, 19)
log_level_slice = slice(20, 28)
user_id_slice = slice(29, 35)
message_slice = slice(36, None)

log_levels = ["INFO", "WARN", "ERROR", "DEBUG", "TRACE", "FATAL", "CRITICAL", "ALERT"]
messages = ["Login Successful", "Invalid Password", "Session Timeout", "Unknown Error"]


def user_ids(length=6):
    return "".join(str(random.randint(0, 9)) for _ in range(length))


max_len_log_level = max(len(level) for level in log_levels)


def parse_log_line(log_line):
    """Parses a structured log line using reusable slices."""
    return {
        "timestamp": log_line[timestamp_slice].strip(),
        "log_level": log_line[log_level_slice].strip(),
        "user_id": log_line[user_id_slice].strip(),
        "message": log_line[message_slice].strip(),
    }


# Random log lines with timestamps within the last day
log_lines = []
for _ in range(random.randint(5, 10)):
    timestamp = (
        datetime.now()
        - timedelta(
            hours=random.randint(0, 24),
            minutes=random.randint(0, 59),
            seconds=random.randint(0, 59),
        )
    ).strftime("%Y-%m-%d %H:%M:%S")
    log_level = random.choice(log_levels)
    user_id = user_ids()
    message = random.choice(messages)
    log_lines.append(
        f"{timestamp} {log_level:<{max_len_log_level}} {user_id:<6} {message}"
    )

parsed_logs = [parse_log_line(line) for line in log_lines]


df = pd.DataFrame(parsed_logs)
print("\nParsed Logs:")
print(df)
