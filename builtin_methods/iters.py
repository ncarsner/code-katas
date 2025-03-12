from typing import List
from itertools import cycle
import random
import string


def manual_iteration(data: List[int]) -> List[int]:
    """
    Manually iterate over a list using an iterator object.

    Args:
        data (List[int]): A list of integers.

    Returns:
        List[int]: A new list with each element incremented by 1.
    """
    result = []
    iterator = iter(data)

    while True:
        try:
            item = next(iterator)
            result.append(item + 1)
        except StopIteration:
            break

    return result


def iterate_with_sentinel(file_path: str) -> List[str]:
    """
    Read lines from a file until an empty string is encountered using iter with a sentinel.

    Args:
        file_path (str): Path to the file.

    Returns:
        List[str]: A list of lines read from the file.
    """
    lines = []
    with open(file_path, "r") as file:
        for line in iter(file.readline, ""):
            lines.append(line.strip())

    return lines


def cycle_through_elements(data: List[str], n: int) -> List[str]:
    """
    Cycle through elements of a list n times using an iterator.

    Args:
        data (List[str]): A list of strings.
        n (int): Number of times to cycle through the list.

    Returns:
        List[str]: A new list with elements cycled n times.
    """
    result = []
    iterator = cycle(data)

    for _ in range(n * len(data)):
        result.append(next(iterator))

    return result


# Example usage
if __name__ == "__main__":
    # Manual iteration
    data = [random.randint(1, 10) for _ in range(5)]
    print(manual_iteration(data))

    # Iteration with sentinel
    file_path = "example_lorem.txt"
    print(iterate_with_sentinel(file_path))

    # Cycle through elements
    data = [random.choices(string.ascii_lowercase, k=random.randint(3, 6))]
    print(cycle_through_elements(data, random.choice([2, 3])))
