from string import ascii_letters, digits
import random
import time


def timer(func):
    # TODO: Why can I not import this from use_cases/functions.py ?
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' executed in {end - start:.6f} seconds")
        return result

    return wrapper


with open("./data/raw/large_file.txt", "r") as file:
    data = file.read()


@timer
def contains_substring(data, substring):
    if substring in data:
        return True
    return False


@timer
def contains_substring_lower(data, substring):
    if substring.lower() in data.lower():
        return True
    return False


@timer
def substring_intersection(data, substring):
    return [line for line in data.splitlines() if substring in line]


if __name__ == "__main__":
    chars = ascii_letters + digits
    substring = "".join(random.choices(chars, k=random.randint(3, 5)))
    result = contains_substring(data, substring)
    print(f"Does the data contain '{substring}'? {result}")

    result_lower = contains_substring_lower(data, substring)
    print(f"Does the data contain '{substring}' (case-insensitive)? {result_lower}")

    results = substring_intersection(data, substring)
    print(f"Lines containing '{substring}': {len(results)} found")
