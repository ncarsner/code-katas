from collections import deque
import random
from pprint import pprint

STREAM_CONTENT = [random.randint(1, 100) for _ in range(10)]
N_COUNT = random.randint(1, 10)


def moving_average(stream, N):
    window = deque(maxlen=N)
    current_sum = 0
    moving_averages = []

    for number in stream:
        window.append(number)
        current_sum = sum(window)
        moving_averages.append(current_sum / len(window))

    return moving_averages


if __name__ == "__main__":
    stream = STREAM_CONTENT
    N = N_COUNT
    result = moving_average(stream, N)
    print(f"{stream=}, {N=}")
    pprint(result)
