from typing import List, Dict, Tuple, Union, Optional, Callable, Any, TypeVar, Generic
import random
import string

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

numbers = [random.randint(1, 20) for _ in range(5)]
letters = [random.choice(string.ascii_lowercase) for _ in range(5)]
items = ["apple", "banana", "cherry", "date", "eggplant"]


def add_numbers(a: int, b: int) -> int:
    """
    Adds two integers together.

    :param a: First integer
    :param b: Second integer
    :return: Sum of a and b
    """
    return a + b


def get_user_info(user_id: int) -> Dict[str, Union[str, int]]:
    """Retrieves user information.

    :param user_id: ID of the user
    :return: Dictionary containing user information
    """
    return {"name": "John Doe", "age": 30, "user_id": user_id}


def process_items(items: List[str]) -> List[str]:
    """
    Processes a list of items.

    :param items: List of items
    :return: List of processed items
    """
    return [item.upper() for item in items]


def find_max(values: Tuple[int, ...]) -> int:
    """Finds the maximum value in a tuple of integers.

    :param values: Tuple of integers
    :return: Maximum integer value
    """
    return max(values)


def safe_divide(a: int, b: int) -> Optional[float]:
    """Safely divides two integers.

    :param a: Numerator
    :param b: Denominator
    :return: Result of division or None if division by zero
    """
    if b == 0:
        return None
    return a / b


def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    """Applies a function to two integers.

    :param func: Function that takes two integers and returns an integer
    :param x: First integer
    :param y: Second integer
    :return: Result of the function
    """
    return func(x, y)


class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get_value(self) -> T:
        """
        Gets the value stored in the container.

        :return: Value stored in the container
        """
        return self.value


def get_any_value(data: Dict[K, V], key: K) -> Optional[V]:
    """
    Retrieves a value from a dictionary by key.

    :param data: Dictionary containing key-value pairs
    :param key: Key to look up
    :return: Value associated with the key or None if key is not found
    """
    return data.get(key)


if __name__ == "__main__":
    a = random.choice(numbers)
    b = random.choice(numbers)

    print(f"\nadd_numbers({a}, {b}) = {add_numbers(a, b)}")
    print(f"{get_user_info(1) = }")
    print(f"{process_items(items) = }")
    print(f"find_max({numbers}) = {find_max(numbers)}")

    print(f"\nsafe_divide({a}, {b})= {safe_divide(a, b)}")
    print(f"safe_divide({a}, {0})= {safe_divide(a, 0)}")

    print(f"\napply_function(add_numbers,{a},{b})={apply_function(add_numbers, a, b)}")

    container = Container[int](random.randint(1, 100))
    print(f"{container.get_value() = }")

    data = dict(zip(letters, [i for i in range(len(letters))]))

    letter = random.choice(letters)
    print(f"\nget_any_value({data=}, {letter}={get_any_value(data, letter)}")
    print(f"{get_any_value(data, 'ab') = }")
