import time


def get_current_time():
    """Get current time in seconds since the Epoch.

    Returns:
        float: Current time in seconds since the Epoch.

    Example:
        >>> get_current_time()
        1633072800.0
    """
    return time.time()


def get_local_time(current_time):
    """Convert a time expressed in seconds since the Epoch to a struct_time.

    Args:
        current_time (float): Time in seconds since the Epoch.

    Returns:
        struct_time: Local time as a struct_time object.

    Example:
        >>> get_local_time(1633072800.0)
        time.struct_time(tm_year=2021, tm_mon=10, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=274, tm_isdst=0)
    """
    return time.localtime(current_time)


def local_time_to_string(local_time):
    """Convert a struct_time to a string representing local time.

    Args:
        local_time (struct_time): Local time as a struct_time object.

    Returns:
        str: Local time as a string.

    Example:
        >>> local_time_to_string(time.localtime(1633072800.0))
        'Fri Oct  1 00:00:00 2021'
    """
    return time.asctime(local_time)


def format_local_time(local_time):
    """Format a struct_time as a string according to a format specification.

    Args:
        local_time (struct_time): Local time as a struct_time object.

    Returns:
        str: Formatted local time.

    Example:
        >>> format_local_time(time.localtime(1633072800.0))
        '2021-10-01 00:00:00'
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", local_time)


def parse_time_string(time_string):
    """Parse a string representing a time according to a format specification to a struct_time.

    Args:
        time_string (str): Time string to parse.

    Returns:
        struct_time: Parsed time as a struct_time object.

    Example:
        >>> parse_time_string("2023-10-05 14:30:00")
        time.struct_time(tm_year=2023, tm_mon=10, tm_mday=5,
                        tm_hour=14, tm_min=30, tm_sec=0,
                        tm_wday=3, tm_yday=278, tm_isdst=-1)
    """
    return time.strptime(time_string, "%Y-%m-%d %H:%M:%S")


def get_monotonic_time():
    """Get current time in seconds since the Epoch as a float (monotonic clock).

    Returns:
        float: Monotonic time.

    Example:
        >>> get_monotonic_time()
        123456.789
    """
    return time.monotonic()


def get_performance_counter_time():
    """Get current time in seconds since the Epoch as a float (high resolution).

    Returns:
        float: Performance counter time.

    Example:
        >>> get_performance_counter_time()
        123456.789
    """
    return time.perf_counter()


def get_process_time():
    """Get current time in seconds since the Epoch as a float (high resolution, includes sleep time).

    Returns:
        float: Process time.

    Example:
        >>> get_process_time()
        123.456
    """
    return time.process_time()


def sleep_for_seconds(seconds):
    """
    Args:
        seconds (int): Number of seconds to sleep.

    Example:
        >>> sleep_for_seconds(2)
        Sleeping for 2 seconds...
        Awake!
    """
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    print("Awake!")


def get_thread_time():
    """
    Get the current thread time in seconds as a float (high resolution, does not include sleep time).

    This function is similar to get_process_time,
    but it measures the CPU time consumed by the current thread,
    rather than the entire process.

    Returns:
        float: Thread time.

    Example:
        >>> get_thread_time()
        123.456
    """
    return time.thread_time()


def get_thread_time_ns():
    """Get the current time in seconds since the Epoch as a float (high resolution, includes sleep time).

    Returns:
        int: Thread time in nanoseconds.

    Example:
        >>> get_thread_time_ns()
        1234567890123
    """
    return time.thread_time_ns()


def get_time_ns():
    """Get the current time in nanoseconds since the Epoch.

    Returns:
        int: Current time in nanoseconds since the Epoch.

    Example:
        >>> get_time_ns()
        1633072800000000000
    """
    return time.time_ns()


if __name__ == "__main__":
    current_time = get_current_time()
    print(f"Current time (seconds since Epoch): {current_time}")

    local_time = get_local_time(current_time)
    print(f"{local_time=}")

    local_time_as_string = local_time_to_string(local_time)
    print(f"{local_time_as_string=}")

    formatted_local_time = format_local_time(local_time)
    print(f"{formatted_local_time=}")

    parsed_time = parse_time_string("2023-10-05 14:30:00")
    print(f"{parsed_time=}")

    monotonic_time = get_monotonic_time()
    print(f"{monotonic_time=}")

    performance_counter_time = get_performance_counter_time()
    print(f"{performance_counter_time=}")

    process_time = get_process_time()
    print(f"{process_time=}")

    sleep_for_seconds(2)

    thread_time = get_thread_time()
    print(f"{thread_time=}")

    thread_time_ns = get_thread_time_ns()
    print(f"{thread_time_ns=}")

    time_ns = get_time_ns()
    print(f"Current time (ns since Epoch): {time_ns}")
