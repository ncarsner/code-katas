import numpy as np
import time
from datetime import datetime


def next_nearest(n, r):
    if n == n + (r - n) % r:
        return n + (r - n) % r + r
    return n + (r - n) % r


nums = np.arange(12, 85)

for num in nums:
    if num % 7 != 0:
        continue
    else:
        # print(num, next_nearest(num, r=10))
        pass


# def format_time(milliseconds):
#     """Function to format time in suitable increments."""
#     seconds, milliseconds = divmod(milliseconds, 1000)
#     minutes, seconds = divmod(seconds, 60)
#     hours, minutes = divmod(minutes, 60)

#     if hours > 0:
#         return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03f}"
#     elif minutes > 0:
#         return f"{minutes:02d}:{seconds:02d}.{milliseconds:03f}"
#     elif seconds > 0:
#         return f"{seconds}.{milliseconds:03f} seconds"
#     else:
#         return f"{milliseconds:.3f} milliseconds"



def fibonacci(n):
    """Recursive function to calculate Fibonacci numbers."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def exponential_time_calculation(n):
    """Function that increases exponentially in time needed to calculate."""
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def format_time(milliseconds):
    """Function to format time in suitable increments."""
    if milliseconds >= 60000:
        minutes, seconds = divmod(milliseconds / 1000, 60)
        return f"{int(minutes)} minutes {seconds:.2f} seconds"
    elif milliseconds >= 1000:
        return f"{milliseconds / 1000:.2f} seconds"
    else:
        return f"{milliseconds:.4f} milliseconds"


for i in range(15,45,5):
    # result, execution_time = exponential_time_calculation(i)
    # print(f"Fibonacci({i}) = {result:,} | Execution Time: {format_time(execution_time * 1000)}")
    ...


n = 45  # Fibonacci sequence number to calculate
# result, execution_time = exponential_time_calculation(n)
# print(f"Fibonacci({n}) = {result}")
# print("Execution Time:", format_time(execution_time * 1000))  # Convert to milliseconds


def get_current_time() -> str:
    """A function that returns the user's current time as a string object.
    >>> get_current_time()
    "2024-11-13 09:05:53 AM"

    %F YYYY-MM-DD
    %H Hour
    %M Minute
    %S Second
    %p AM/PM
    %A Day of week"""
    now: datetime = datetime.now()
    return f"{now:%F %T %p}"

print(get_current_time())

print(f"{type(get_current_time())=}")

print(get_current_time.__doc__)