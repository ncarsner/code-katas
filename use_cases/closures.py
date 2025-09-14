import math
import random
import json


# Creating a custom multiplier function
def multiplier(factor):
    def multiply_by(value):
        return value * factor

    return multiply_by


# Caching expensive computations
def cache_function(func):
    cache = {}

    def cached_func(arg):
        if arg not in cache:
            cache[arg] = func(arg)
        return cache[arg]

    return cached_func


@cache_function
def expensive_computation(x):
    print(f"Computing for {x}...")
    return math.sqrt(x)


# Closure for filtering data based on a condition
def data_filter(condition):
    def filter_data(data):
        return [item for item in data if condition(item)]

    return filter_data


# Closure for generating unique IDs
def id_generator(start=0):
    current_id = start

    def generate_id():
        nonlocal current_id
        current_id += 1
        return current_id

    return generate_id


# Closure for logging function calls
def logger(func):
    def log_and_call(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        return func(*args, **kwargs)

    return log_and_call


@logger
def calculate_total(price, quantity):
    return price * quantity


def _parse_numbers(data: str) -> int:
    total = 0

    def process(item) -> None:
        nonlocal total
        if isinstance(item, dict):
            for v in item.values():
                process(v)
        elif isinstance(item, list):
            for v in item:
                process(v)
        elif isinstance(item, (int, float)):
            total += item
        else:
            return None

    process(json.loads(data))

    return total


if __name__ == "__main__":
    # Custom multiplier usage
    a, b = random.randint(1, 10), random.randint(1, 10)
    double = multiplier(2)
    triple = multiplier(3)

    print(f"double({a}) = {double(a)}")
    print(f"triple({b}) = {triple(b)}")

    # Caching expensive computation usage
    c, d = random.randint(5, 20), random.randint(5, 20)
    print(f"expensive_computation({c}) = {expensive_computation(c):.5f}")
    print(f"expensive_computation({d}) = {expensive_computation(d):.5f}")

    # Closure for filtering data based on a condition
    is_positive = data_filter(lambda x: x > 0)
    data = [random.randint(-10, 10) for _ in range(10)]
    print(f"Original data: {sorted(data)}")
    print(f"Positive data: {is_positive(data)}")

    # Closure for generating unique IDs
    generate_employee_id = id_generator(1000)

    print(generate_employee_id())
    print(generate_employee_id())

    # Closure for logging function calls
    e, f = random.randint(1, 20), random.randint(1, 20)
    print(calculate_total(e, f))  # Logs the call without keyword arguments
    print(calculate_total(price=e, quantity=f))  # Logs the call with keyword arguments

    # Parsing numbers from JSON-like string
    data = '{"a": 10, "b": [1, 2, {"c": 3.5}], "d": "text"}'
    result = _parse_numbers(data)
    print(result)
