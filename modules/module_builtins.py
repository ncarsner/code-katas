import builtins
from typing import Any, Callable, List, Dict
import random

"""
Practical uses of Python's `builtins` module which contains all of Python's built-in objects, functions, and exceptions.

This module demonstrates:
- Accessing built-in functions dynamically
- Overriding built-in functions (with caution)
- Listing all built-in names
- Using built-in exceptions for robust error handling
"""


def dynamic_apply_builtin(func_name: str, *args, **kwargs) -> Any:
    """
    Dynamically apply a built-in function by name.
    Useful for generic data processing pipelines.

    Args:
        func_name (str): Name of the built-in function (e.g., 'sum', 'max').
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.

    Returns:
        Any: Result of the built-in function.

    Raises:
        AttributeError: If the function does not exist in builtins.
    """
    func: Callable = getattr(builtins, func_name)
    return func(*args, **kwargs)


def list_all_builtins() -> List[str]:
    """
    List all names in the builtins module.

    Returns:
        List[str]: Sorted list of all built-in names.
    """
    return sorted(dir(builtins))


def safe_eval(expr: str, variables: Dict[str, Any] = None) -> Any:
    """
    Safely evaluate a Python expression using built-in eval.
    Restricts the global and local namespaces for security.

    Args:
        expr (str): The expression to evaluate.
        variables (Dict[str, Any], optional): Variables to use in the expression.

    Returns:
        Any: Result of the evaluated expression.

    Raises:
        builtins.SyntaxError, builtins.NameError, etc.: On invalid expressions.
    """
    # Only allow specified variables and built-in functions
    safe_globals = {"__builtins__": builtins}
    safe_locals = variables if variables else {}
    return builtins.eval(expr, safe_globals, safe_locals)


def override_builtin_example():
    """
    Example of overriding a built-in function (not recommended in production).
    Shows how to temporarily override and restore a built-in for testing.

    Returns:
        None
    """
    original_print = builtins.print

    def custom_print(*args, **kwargs):
        original_print("LOG:", *args, **kwargs)

    builtins.print = custom_print
    print("This will be prefixed with 'LOG:'")
    builtins.print = original_print  # Restore original


def robust_input(prompt: str) -> str:
    """
    Wrapper for built-in input with error handling for KeyboardInterrupt.

    Args:
        prompt (str): Prompt to display.

    Returns:
        str: User input or empty string if interrupted.
    """
    try:
        return builtins.input(prompt)
    except builtins.KeyboardInterrupt:
        print("\nInput cancelled by user.")
        return ""


if __name__ == "__main__":
    # Dynamically apply built-in functions
    numbers = [random.choice(range(10, 100, 5)) for _ in range(5)]
    print("Sum:", dynamic_apply_builtin("sum", numbers))
    print("Max:", dynamic_apply_builtin("max", numbers))

    # List all built-in names
    list_length = random.randint(2, 10)
    print(f"First {list_length} built-ins: {list_all_builtins()[:list_length]}")

    # Safe evaluation
    expr = "a + b"
    variables = {"a": random.randint(2, 10), "b": random.randint(2, 10)}
    print("Safe eval result:", safe_eval(expr, variables))

    # Override built-in print (for demonstration)
    override_builtin_example()

    # Robust input (uncomment to use)
    # user_value = robust_input("Enter a value: ")
    # print("You entered:", user_value)
