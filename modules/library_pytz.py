from datetime import datetime, timedelta
from typing import List
import pytz

"""
The `pytz` library is useful for timezone-aware datetime operations when working with global data.

Requires: pytz, datetime
"""


def list_all_timezones() -> List[str]:
    """
    Returns a list of all available timezones in pytz.
    Useful for validating user input or populating dropdowns.
    """
    return pytz.all_timezones


def convert_to_timezone(dt: datetime, tz_name: str) -> datetime:
    """
    Converts a naive or aware datetime to the specified timezone.

    Args:
        dt: The datetime object (naive or aware).
        tz_name: The target timezone name (e.g., 'America/New_York').

    Returns:
        A timezone-aware datetime in the target timezone.

    Raises:
        pytz.UnknownTimeZoneError: If tz_name is invalid.
    """
    tz = pytz.timezone(tz_name)
    if dt.tzinfo is None:
        # Assume input is UTC if naive
        dt = pytz.utc.localize(dt)
    return dt.astimezone(tz)


def get_current_time_in_timezone(tz_name: str) -> datetime:
    """
    Gets the current time in the specified timezone.

    Args:
        tz_name: The target timezone name.

    Returns:
        A timezone-aware datetime object.
    """
    tz = pytz.timezone(tz_name)
    return datetime.now(tz)


def localize_naive_datetime(dt: datetime, tz_name: str) -> datetime:
    """
    Localizes a naive datetime to the specified timezone.

    Args:
        dt: Naive datetime object.
        tz_name: Timezone name.

    Returns:
        Timezone-aware datetime.

    Raises:
        ValueError: If dt is already timezone-aware.
    """
    if dt.tzinfo is not None:
        raise ValueError("Datetime is already timezone-aware.")
    tz = pytz.timezone(tz_name)
    return tz.localize(dt)


def convert_between_timezones(dt: datetime, from_tz: str, to_tz: str) -> datetime:
    """
    Converts a naive datetime from one timezone to another.

    Args:
        dt: Naive datetime object.
        from_tz: Source timezone name.
        to_tz: Target timezone name.

    Returns:
        Timezone-aware datetime in the target timezone.
    """
    src_tz = pytz.timezone(from_tz)
    tgt_tz = pytz.timezone(to_tz)
    localized_dt = src_tz.localize(dt)
    return localized_dt.astimezone(tgt_tz)


def get_time_difference(dt1: datetime, tz1: str, dt2: datetime, tz2: str) -> timedelta:
    """
    Calculates the time difference between two datetimes in different timezones.

    Args:
        dt1: First naive datetime.
        tz1: Timezone of dt1.
        dt2: Second naive datetime.
        tz2: Timezone of dt2.

    Returns:
        timedelta representing the difference (dt1 - dt2).
    """
    dt1_tz = pytz.timezone(tz1).localize(dt1)
    dt2_tz = pytz.timezone(tz2).localize(dt2)
    return dt1_tz - dt2_tz


if __name__ == "__main__":
    # List all timezones
    print("Available timezones:", list_all_timezones()[:5], "...")

    # Convert naive datetime to New York time
    naive_dt = datetime(2024, 6, 1, 12, 0, 0)
    ny_dt = localize_naive_datetime(naive_dt, "America/New_York")
    print("NY localized:", ny_dt)

    # Convert NY time to Tokyo time
    tokyo_dt = convert_between_timezones(naive_dt, "America/New_York", "Asia/Tokyo")
    print("NY to Tokyo:", tokyo_dt)

    # Get current time in London
    print("Current London time:", get_current_time_in_timezone("Europe/London"))

    # Calculate time difference
    dt1 = datetime(2024, 6, 1, 9, 0, 0)
    dt2 = datetime(2024, 6, 1, 17, 0, 0)
    diff = get_time_difference(dt1, "America/Los_Angeles", dt2, "Europe/Berlin")
    print("Time difference:", diff)
