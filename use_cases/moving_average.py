from collections import deque
from itertools import islice
import random


def moving_average(iterable, n):
    source = iter(iterable)
    scope = deque(islice(source, n), maxlen=n)
    if len(scope) < n:
        return
    s = sum(scope)
    yield s / n
    for elem in source:
        s += elem - scope[0]
        scope.append(elem)
        yield s / n


if __name__ == "__main__":
    data = [random.randint(1, 20) for _ in range(10)]
    round_to = 1
    print(data)
    print([round(num, round_to) for num in moving_average(data, 3)])
