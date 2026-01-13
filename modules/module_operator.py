import operator
from typing import List, Tuple, Any
from functools import reduce
import random

"""
The `operator` module provides a set of efficient functions corresponding to standard operators, which can be used for cleaner and faster code in data manipulation and analysis tasks.
"""


# Sorting a list of dictionaries by a specific key
def sort_by_key(data: List[dict], key: str) -> List[dict]:
    """
    Sorts a list of dictionaries by a specified key using `operator.itemgetter`.

    Args:
        data (List[dict]): The list of dictionaries to sort.
        key (str): The key to sort the dictionaries by.

    Returns:
        List[dict]: The sorted list of dictionaries.
    """
    sorted_data = sorted(data, key=operator.itemgetter(key))
    for item in sorted_data:
        print(item)
    return sorted_data


# Dynamic attribute access
class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary


def get_attribute(obj: Any, attr: str) -> Any:
    """
    Dynamically retrieves an attribute from an object using `operator.attrgetter`.

    Args:
        obj (Any): The object to retrieve the attribute from.
        attr (str): The name of the attribute to retrieve.

    Returns:
        Any: The value of the specified attribute.
    """
    return operator.attrgetter(attr)(obj)


# Reduce a list of numbers with a specific operation
def calculate_product(numbers: List[int]) -> int:
    """
    Calculates the product of a list of numbers using `operator.mul` and `functools.reduce`.

    Args:
        numbers (List[int]): The list of numbers to multiply.

    Returns:
        int: The product of the numbers.
    """
    return reduce(operator.mul, numbers, 1)


# Filter data with a specific condition
def filter_greater_than(data: List[int], threshold: int) -> List[int]:
    """
    Filters a list of numbers, returning only those greater than a given threshold.

    Args:
        data (List[int]): The list of numbers to filter.
        threshold (int): The threshold value.

    Returns:
        List[int]: The filtered list of numbers.
    """
    return list(filter(lambda x: operator.gt(x, threshold), data))


# Map operations to a list
def increment_all(data: List[int], increment: int) -> List[int]:
    """
    Increments all numbers in a list by a specified value using `operator.add`.

    Args:
        data (List[int]): The list of numbers to increment.
        increment (int): The value to add to each number.

    Returns:
        List[int]: The incremented list of numbers.
    """
    return list(map(operator.add, data, [increment] * len(data)))


if __name__ == "__main__":
    # Sorting
    employees = ["Alex", "Blake", "Chris", "Dylan", "Elliott"]
    salaries = [random.choice(range(50000, 125001, 5000)) for _ in range(len(employees))]
    random.shuffle(employees)
    employees = [
        {"name": employees[0], "age": random.randint(21, 65), "salary": salaries[0]},
        {"name": employees[1], "age": random.randint(21, 65), "salary": salaries[1]},
        {"name": employees[2], "age": random.randint(21, 65), "salary": salaries[2]},
        {"name": employees[3], "age": random.randint(21, 65), "salary": salaries[3]},
        {"name": employees[4], "age": random.randint(21, 65), "salary": salaries[4]},
    ]
    random_attribute = random.choice(list(employees[0].keys()))
    print(f"Sorted by {random_attribute}:", sort_by_key(employees, random_attribute))

    # Attribute access
    emp = Employee(
        random.choice(employees)["name"],
        random.randint(21, 65),
        random.choice(range(50000, 125001, 5000)),
    )
    print("\nEmployee's salary:", get_attribute(emp, "salary"))

    # Product calculation
    numbers = [random.randint(1, 10) for _ in range(3)]
    print(f"\n{numbers=} -> Product:", calculate_product(numbers))
    # print("Product of numbers:", calculate_product(numbers))

    # Filtering
    data = sorted([random.randint(1, 100) for _ in range(5)])
    threshold = random.randint(1, 100)
    print(f"\n{data=} -> {threshold=}:")
    print(f"Numbers > {threshold}:", filter_greater_than(data, threshold))

    # Mapping
    increment = random.randint(1, 10)
    print(f"\nIncrement all numbers by {increment}:")
    print("Incremented numbers:", increment_all(data, increment))
