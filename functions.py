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
        print(num, next_nearest(num, r=10))
