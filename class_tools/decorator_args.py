from functools import wraps
from typing import Callable, Any, Optional
import random


def log_execution(log_message: Optional[str] = None) -> Callable:
    """
    A decorator with an optional argument to log the execution of a function.

    Args:
        log_message (Optional[str]): A custom message to log.
        If not provided, a default message is used.

    Returns:
        Callable: The decorated function.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            message = (
                log_message
                or f"Executing {func.__name__} with args={args} and kwargs={kwargs}"
            )
            print(f"[LOG]: {message}")
            result = func(*args, **kwargs)
            print(f"[LOG]: {func.__name__} completed with result={result}")
            return result

        return wrapper

    return decorator


# Using the decorator without arguments
@log_execution()
def calculate_sum(a: int, b: int) -> int:
    """Calculates the sum of two integers."""
    return a + b


# Using the decorator with a custom log message
@log_execution(log_message="Custom log: Running the data aggregation function")
def aggregate_data(data: list[int]) -> int:
    """Aggregates a list of integers by summing them."""
    return sum(data)


# Use case for a BI developer
@log_execution(log_message="Fetching sales data for analysis")
def fetch_sales_data(region: str, year: int) -> list[dict]:
    """
    Simulates fetching sales data for a specific region and year.

    Args:
        region (str): The region for which to fetch sales data.
        year (int): The year for which to fetch sales data.

    Returns:
        list[dict]: A list of sales records.
    """
    # Simulated data fetch
    return [
        {"region": region, "year": year, "sales": 1000},
        {"region": region, "year": year, "sales": 1500},
    ]


if __name__ == "__main__":
    calculate_sum(random.randint(1, 10), random.randint(1, 10))

    aggregate_data([random.randint(50, 300) for _ in range(3)])

    sales_data = fetch_sales_data("North America", 2023)
    print(sales_data)
