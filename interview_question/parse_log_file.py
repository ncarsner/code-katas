import re
import sys


def parse_log_file(file_path):
    error_pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}).*ERROR.*: (.*)")
    errors = []

    with open(file_path, "r") as file:
        for line in file:
            match = error_pattern.search(line)
            if match:
                timestamp, message = match.groups()
                errors.append((timestamp, message))

    return errors


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_log_file.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]
    errors = parse_log_file(log_file_path)

    for timestamp, message in errors:
        print(f"{timestamp} - {message}")
