import calendar
from typing import List, Tuple
from datetime import datetime, timedelta
import random

RAND_YEAR = random.randint(1900, datetime.now().year)
RAND_MONTH = random.randint(1, 12)
RAND_DAY = random.randint(1, 28)  # To avoid issues with February
CURRENT_YEAR = datetime.now().year

def generate_month_calendar(year: int, month: int) -> str:
    """
    Generates a plain text calendar for a specific month and year.

    Args:
        year (int): The year of the calendar.
        month (int): The month of the calendar (1-12).

    Returns:
        str: A string representation of the month's calendar.
    """
    return calendar.month(year, month)


def is_leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return calendar.isleap(year)


def count_leap_years(start_year: int, end_year: int) -> int:
    """
    Counts the number of leap years in a given range of years.

    Args:
        start_year (int): The starting year (inclusive).
        end_year (int): The ending year (inclusive).

    Returns:
        int: The number of leap years in the range.
    """
    return calendar.leapdays(start_year, end_year + 1)


def get_weekday(year: int, month: int, day: int) -> str:
    """
    Returns the name of the weekday for a given date.

    Args:
        year (int): The year of the date.
        month (int): The month of the date (1-12).
        day (int): The day of the date (1-31).

    Returns:
        str: The name of the weekday (e.g., "Monday").
    """
    weekday_index = calendar.weekday(year, month, day)
    return calendar.day_name[weekday_index]


def get_month_days(year: int, month: int) -> List[Tuple[int, int]]:
    """
    Returns a list of weeks in a month, where each week is represented as tuples of days.
    Days outside the month are represented as 0.

    Args:
        year (int): The year of the month.
        month (int): The month (1-12).

    Returns:
        List[Tuple[int, int]]: A list of weeks with days as tuples.
    """
    return calendar.monthcalendar(year, month)


def print_year_calendar(year: int) -> None:
    """
    Prints a plain text calendar for the entire year.

    Args:
        year (int): The year to print the calendar for.
    """
    print(calendar.TextCalendar().formatyear(year))


if __name__ == "__main__":
    # Generate a random month calendar
    print(f"Calendar for {calendar.month_name[RAND_MONTH]} {RAND_YEAR}:")
    print(generate_month_calendar(RAND_YEAR, RAND_MONTH))

    # Check if a year is a leap year
    print(f"Is {RAND_YEAR} a leap year? {is_leap_year(RAND_YEAR)}")

    # Count leap years in a range
    print(f"Leap years between {RAND_YEAR} and {CURRENT_YEAR}: {count_leap_years(RAND_YEAR, CURRENT_YEAR)}")

    # Get the weekday of a specific date
    print(f"Weekday for {calendar.month_name[RAND_MONTH]} {RAND_DAY}, {RAND_YEAR} is: {get_weekday(RAND_YEAR, RAND_MONTH, RAND_DAY)}")

    # Get the days of a month as a list of weeks
    print(f"Weeks in {calendar.month_name[RAND_MONTH]} {RAND_YEAR}:")
    for week in get_month_days(RAND_YEAR, RAND_MONTH):
        print(week)

    # Print a full year calendar
    print(f"Full year calendar for {RAND_YEAR}:")
    print_year_calendar(RAND_YEAR)
