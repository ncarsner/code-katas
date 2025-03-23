import random
import numpy as np
from timeit import timeit

MAX_RANGE = 100
NUM_RANDOMS = 1_000_000


def generate_with_random():
    return [random.randint(1, MAX_RANGE) for _ in range(NUM_RANDOMS)]


def generate_with_numpy():
    return np.random.randint(1, MAX_RANGE + 1, NUM_RANDOMS).tolist()


def measure_time_and_size(generator_func):
    execution_time = timeit(generator_func, number=1)
    generated_list = generator_func()
    size = len(generated_list)
    return execution_time, size


if __name__ == "__main__":
    random_time, random_size = measure_time_and_size(generate_with_random)
    numpy_time, numpy_size = measure_time_and_size(generate_with_numpy)

    print(f"Random library: Time = {random_time:.6f}s, Size = {random_size:,}")
    print(f"Numpy library: Time = {numpy_time:.6f}s, Size = {numpy_size:,}")
