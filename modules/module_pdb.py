import pdb
import random


INT = random.randint(1, 20)  # Random integer for demonstration
INT_LIST = [random.randint(1, 20) for _ in range(10)]  # Random list of integers


def add(a, b):
    pdb.set_trace()
    return a + b


def subtract(a, b):
    pdb.set_trace()
    return a - b


def multiply(a, b):
    pdb.set_trace()
    return a * b


def divide(a, b):
    pdb.set_trace()
    if not b:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a given number using recursion.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)


def find_maximum(numbers: list[int]) -> int:
    """
    Find the maximum number in a list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The maximum number in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot find the maximum of an empty list.")
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


def main():
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    result_add = add(x, y)
    print(f"Add: {x} + {y} = {result_add}")

    result_subtract = subtract(x, y)
    print(f"Subtract: {x} - {y} = {result_subtract}")

    result_multiply = multiply(x, y)
    print(f"Multiply: {x} * {y} = {result_multiply}")

    result_divide = divide(x, y)
    print(f"Divide: {x} / {y} = {result_divide}")

    # Debugging the factorial function
    try:
        pdb.set_trace()  # Set a breakpoint here
        print(f"Calculating factorial of {INT}")
        result = calculate_factorial(INT)
        print(f"Factorial of {INT} is {result}")
    except Exception as e:
        print(f"Error: {e}")

    # Debugging the find_maximum function
    try:
        pdb.set_trace()  # Set another breakpoint here
        print(f"Finding maximum in the list: {INT_LIST}")
        max_value = find_maximum(INT_LIST)
        print(f"Maximum value in the list is {max_value}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """
    How to use the debugger:
    1. Run this script in the terminal: `python -m pdb module_debug.py`.
    2. Use the following pdb commands at the breakpoints:
    - `n` (next): Execute the next line of code.
    - `s` (step): Step into a function call.
    - `c` (continue): Continue execution until the next breakpoint.
    - `p <variable>`: Print the value of a variable.
    - `q` (quit): Exit the debugger.
    3. Analyze the flow of execution and variable values to troubleshoot issues.
    """
    main()
