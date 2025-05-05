import sched
import time
from datetime import datetime
from typing import Callable

"""Lightweight task scheduler used for time-based automation."""


# Initialize the scheduler
scheduler = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)


def log_event(event_name: str) -> None:
    """
    Logs the execution of a scheduled event.

    Args:
        event_name (str): The name of the event being logged.
    """
    print(f"[{datetime.now()}] Event executed: {event_name}")


def schedule_task(
    delay: int,
    priority: int,
    action: Callable,
    argument: tuple = (),
    kwargs: dict = None,
) -> None:
    """
    Schedules a task using the sched module.

    Args:
        delay (int): The delay in seconds before the task is executed.
        priority (int): The priority of the task (lower numbers indicate higher priority).
        action (Callable): The function to execute.
        argument (tuple): Positional arguments to pass to the function.
        kwargs (dict): Keyword arguments to pass to the function.
    """
    if kwargs is None:
        kwargs = {}
    scheduler.enter(delay, priority, action, argument, kwargs)


# Automating a daily data extraction task
def extract_data(source: str) -> None:
    """
    Simulates a data extraction task.

    Args:
        source (str): The data source to extract from.
    """
    print(f"[{datetime.now()}] Extracting data from {source}...")
    log_event("Data Extraction")


# Automating a data transformation task
def transform_data(dataset: str) -> None:
    """
    Simulates a data transformation task.

    Args:
        dataset (str): The dataset to transform.
    """
    print(f"[{datetime.now()}] Transforming dataset: {dataset}...")
    log_event("Data Transformation")


# Automating a report generation task
def generate_report(report_name: str) -> None:
    """
    Simulates a report generation task.

    Args:
        report_name (str): The name of the report to generate.
    """
    print(f"[{datetime.now()}] Generating report: {report_name}...")
    log_event("Report Generation")


if __name__ == "__main__":
    # Schedule tasks
    schedule_task(delay=5, priority=1, action=extract_data, argument=("DataWarehouse",))
    schedule_task(10, 2, transform_data, argument=("SalesData",))
    schedule_task(15, 3, generate_report, argument=("MonthlySalesReport",))

    # Start the scheduler
    print(f"[{datetime.now()}] Starting the scheduler...")
    scheduler.run()
    print(f"[{datetime.now()}] All scheduled tasks have been executed.")
