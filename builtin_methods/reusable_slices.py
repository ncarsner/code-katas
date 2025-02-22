import random
import string
import pandas as pd
from datetime import datetime, timedelta


first_three = slice(0, 3)
middle_section = slice(3, -3)
last_three = slice(-3, None)

example_list = [random.randint(0, 100) for _ in range(10)]
example_list.sort()


def get_slice(data, slice_obj):
    return data[slice_obj]


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


"""Testing for expected values using reusable slices."""
today = datetime.now()
weekday_name = today.strftime("%A")
month_name = today.strftime("%B")
day_of_month = today.strftime("%d")
year = today.strftime("%Y")
month_number = today.strftime("%#m")
day_number = today.strftime("%#d")
hour = today.strftime("%#H")

"""Generate a 32-character random string made entirely of characters from the current date and time."""
chars = (
    weekday_name + month_name + day_of_month + year + month_number + day_number + hour
)
chars += string.punctuation
all_chars = string.ascii_letters + string.digits + string.punctuation


def generate_valid_string(chars=chars, length=32):
    return "".join(random.choices(chars, k=length))


def generate_invalid_string(chars=all_chars, length=32):
    return "".join(random.choices(chars, k=length))


def is_valid_string(s, valid_chars=chars):
    return all(c in valid_chars for c in s)


def main(parse_list_example=True, parse_log_example=True, valid_string_example=True):
    if parse_list_example:
        print(f"\n{example_list=}")
        print("\nFirst:", example_list[first_three])
        print("Middle:", example_list[middle_section])
        print("Last:", example_list[last_three])

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

    if parse_log_example:
        df = pd.DataFrame(parsed_logs)
        print("\nParsed Logs:")
        print(df)

    if valid_string_example:
        for i in range(10):
            length = 32
            valid_string = generate_valid_string(length=length)
            invalid_string = generate_invalid_string(length=length)
            print(
                valid_string,
                is_valid_string(valid_string, valid_chars=chars),
                invalid_string,
                is_valid_string(invalid_string, valid_chars=chars),
            )


if __name__ == "__main__":
    main(
        parse_list_example=False,
        parse_log_example=False,
        valid_string_example=True,
    )
