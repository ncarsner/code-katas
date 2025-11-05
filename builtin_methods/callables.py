from typing import Any, Callable, List
import random
import string


names = ["Alex", "Blake", "Chris", "Dillon", "Elliott"]
nums = [random.randint(1, 20) for _ in range(random.randint(5, 10))]


# Using a function as a callable
def greet(name: str) -> str:
    """Function that greets a person by name."""
    return f"Hello, {name}!"


# Using a class with a __call__ method as a callable
class Multiplier:
    """Class that multiplies a number by a given factor."""

    def __init__(self, factor: int) -> None:
        self.factor = factor

    def __call__(self, number: int) -> int:
        return number * self.factor


# Using a lambda function as a callable
square: Callable[[int], int] = lambda x: x * x


# Use a callable to filter a list
def is_even(number: int) -> bool:
    """Function that checks if a number is even."""
    return number % 2 == 0


def filter_list(numbers: List[int], condition: Callable[[int], bool]) -> List[int]:
    """Filters a list of numbers based on a condition."""
    return [number for number in numbers if condition(number)]


# Attempting to call a non-callable object raises a TypeError
try:
    non_callable = 42
    print(non_callable()) # type: ignore
except TypeError as e:
    print(f"Error: {e}")

# Misinterpreting a list as a callable raises a TypeError
try:
    my_list = [1, 2, 3]
    print(my_list(1))  # type: ignore
except TypeError as e:
    print(f"Error: {e}")

# Using a string as a callable raises a TypeError
try:
    my_string = "hello"
    print(my_string())  # type: ignore
except TypeError as e:
    print(f"Error: {e}")


# OOPS! No __call__ method in a class object
class Adder:
    def __init__(self, addend: int) -> None:
        self.addend = addend

    # Missing __call__ method


# Correcting Example 8 by adding the __call__ method
class AdderCorrected:
    def __init__(self, addend: int) -> None:
        self.addend = addend

    def __call__(self, number: int) -> int:
        return number + self.addend



if __name__ == "__main__":
    print(greet(random.choice(names)))

    # Using the Multiplier class
    two, three, four = 2, 3, 4
    factor = random.choice([two, three, four])
    multiple = Multiplier(factor)
    print(f"{factor=}, multiplier={multiple(factor)}")

    # Using the lambda function
    sq_num = random.randint(2, 10)
    print(f"{sq_num=}, square={square(sq_num)}")

    # Using the filter_list function with is_even as the condition
    even_numbers = filter_list(nums, is_even)
    print(f"{even_numbers=}")

    try:
        add_num = random.randint(2, 10)
        adder = Adder(add_num)
        print(adder(add_num))  # type: ignore - raises a TypeError (no __call__ method)
    except TypeError as e:
        print(f"Error: {e}")

    try:
        add_num = random.randint(2, 10)
        adder_corrected = AdderCorrected(add_num)
        print(f"{add_num=}, adder_corrected={adder_corrected(add_num)}")
    except TypeError as e:
        print(f"Error: {e}")

    attrs = [attr for attr in dir(string) if not attr.startswith("_")]
    for attr in attrs:
        print(attr, callable(getattr(string, attr)))