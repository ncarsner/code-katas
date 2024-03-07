import numpy as np


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


def format_time(milliseconds):
    """Function to format time in suitable increments."""
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03f}"
    elif minutes > 0:
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:03f}"
    elif seconds > 0:
        return f"{seconds}.{milliseconds:03f} seconds"
    else:
        return f"{milliseconds:.3f} milliseconds"
