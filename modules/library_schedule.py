import schedule
import time
from datetime import datetime
import random


"""
To use this script:
1. Install the `schedule` library: `pip install schedule`
2. Run the script and observe the scheduled tasks being executed.

The script uses type hints and docstrings for clarity.
"""


def extract_data() -> None:
    """
    Simulates a data extraction task.
    This function could be replaced with actual code to extract data from a database or API.
    """
    print(f"[{datetime.now()}] Data extraction started...")
    # Simulate data extraction logic here
    time.sleep(2)  # Simulate processing time
    print(f"[{datetime.now()}] Data extraction completed.")


def transform_data() -> None:
    """
    Simulates a data transformation task.
    This function could be replaced with actual code to clean and transform data.
    """
    print(f"[{datetime.now()}] Data transformation started...")
    # Simulate data transformation logic here
    time.sleep(random.randint(2, 5))  # Simulate processing time
    print(f"[{datetime.now()}] Data transformation completed.")


def generate_report() -> None:
    """
    Simulates a report generation task.
    This function could be replaced with actual code to generate and send reports.
    """
    print(f"[{datetime.now()}] Report generation started...")
    # Simulate report generation logic here
    time.sleep(random.randint(2, 5))  # Simulate processing time
    print(f"[{datetime.now()}] Report generation completed.")


def schedule_tasks() -> None:
    """
    Schedules tasks using the `schedule` library.
    Tasks are scheduled at specific times or intervals.
    """
    # Schedule data extraction every day at 8:00 AM
    schedule.every().day.at("08:00").do(extract_data)

    # Schedule data transformation every day at 9:00 AM
    schedule.every().day.at("09:00").do(transform_data)

    # Schedule report generation every Monday at 10:00 AM
    schedule.every().monday.at("10:00").do(generate_report)

    print("Tasks have been scheduled. Waiting for execution...")


def run_scheduler() -> None:
    """
    Runs the scheduler in an infinite loop.
    This function continuously checks for scheduled tasks and executes them.
    """
    while True:
        schedule.run_pending()
        # Sleep for a short period to avoid busy waiting
        time.sleep(random.randint(2, 5))


if __name__ == "__main__":
    schedule_tasks()
    run_scheduler()
