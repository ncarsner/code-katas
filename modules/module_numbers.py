import numbers
from decimal import Decimal
from typing import Any, List

"""
The `numbers` module provides abstract base classes (ABCs) for numeric types, enabling type-safe and type-agnostic checks for numbers in Python. It allows you to determine whether a value is an integer, real, or complex number, regardless of its specific implementation (e.g., int, float, Decimal).

Reference:
    https://docs.python.org/3/library/numbers.html
"""


def is_numeric(value: Any) -> bool:
    """
    Check if a value is any kind of number (int, float, Decimal, Fraction, etc.).

    Args:
        value: Any value to check.

    Returns:
        True if value is a number, False otherwise.

    Example:
        is_numeric(10)        # True
        is_numeric(3.14)      # True
        is_numeric(Decimal('2.5')) # True
        is_numeric('hello')   # False
    """
    return isinstance(value, numbers.Number)


def sum_numeric(values: List[Any]) -> float:
    """
    Sum a list of numeric values, ignoring non-numeric entries.

    Args:
        values: List of values (mixed types allowed).

    Returns:
        Sum of all numeric values as float.

    Example:
        sum_numeric([1, 2.5, 'a', Decimal('3.5')]) # 7.0
    """
    return float(sum(float(v) for v in values if isinstance(v, numbers.Real)))


def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter and return only integer values from a list.

    Args:
        values: List of values (mixed types allowed).

    Returns:
        List of integers.

    Example:
        filter_integers([1, 2.5, 3, Decimal('4'), 'b']) # [1, 3]
    """
    return [int(v) for v in values if isinstance(v, numbers.Integral)]


def ensure_real(value: Any) -> float:
    """
    Ensure a value is a real number (int, float, Decimal), else raise TypeError.

    Args:
        value: Value to check.

    Returns:
        The value as a float.

    Raises:
        TypeError: If value is not a real number.

    Example:
        ensure_real(3.5)         # 3.5
        ensure_real(Decimal('2'))# 2.0
        ensure_real(1+2j)        # TypeError
    """
    if not isinstance(value, numbers.Real):
        raise TypeError(f"Value {value} is not a real number.")
    return float(value)


def is_complex_but_not_real(value: Any) -> bool:
    """
    Check if a value is a complex number but not a real number.

    Args:
        value: Value to check.

    Returns:
        True if value is complex but not real, False otherwise.

    Example:
        is_complex_but_not_real(1+2j) # True
        is_complex_but_not_real(2.0)  # False
    """
    return isinstance(value, numbers.Complex) and not isinstance(value, numbers.Real)


if __name__ == "__main__":
    data = [10, 3.14, Decimal("2.5"), "hello", 1 + 2j, 7]
    print("Is numeric:", [is_numeric(x) for x in data])
    print("Sum numeric:", sum_numeric(data))
    print("Filter integers:", filter_integers(data))
    try:
        print("Ensure real (3.14):", ensure_real(3.14))
        print("Ensure real (1+2j):", ensure_real(1 + 2j))
    except TypeError as e:
        print("Error:", e)
    print("Is complex but not real:", [is_complex_but_not_real(x) for x in data])
