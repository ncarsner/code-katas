from typing import Any
import random


class PositiveNumber:
    """
    Descriptor to ensure a value is a positive number.
    Useful for validating business metrics like revenue, profit, etc.
    """

    def __init__(self, name: str):
        # Initialize the descriptor with the name of the attribute it will manage.
        self.name = name

    def __get__(self, instance: Any, owner: Any) -> Any:
        # Retrieve the value of the attribute from the instance's dictionary.
        return instance.__dict__[self.name]

    def __set__(self, instance: Any, value: float) -> None:
        # Validate that the value is a positive number before setting it.
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"{self.name} must be a positive number.")
        instance.__dict__[self.name] = value

    def __delete__(self, instance: Any) -> None:
        # Prevent deletion of the attribute by raising an AttributeError.
        raise AttributeError(f"Cannot delete attribute {self.name}")


class LazyProperty:
    """
    Descriptor for lazy loading of expensive computations.
    Useful for calculating KPIs or aggregations only when needed.
    """

    def __init__(self, func):
        # Store the function to be lazily evaluated and its name.
        self.func = func
        self.name = func.__name__

    def __get__(self, instance: Any, owner: Any) -> Any:
        if instance is None:
            # If accessed from the class, return the descriptor itself.
            return self
        # Compute the value once and store it in the instance dictionary.
        value = self.func(instance)
        instance.__dict__[self.name] = value
        return value


class BusinessMetrics:
    """
    Demonstrates the use of descriptors for validation and lazy loading.
    """

    # Use the PositiveNumber descriptor to validate revenue and expenses.
    revenue = PositiveNumber("revenue")
    expenses = PositiveNumber("expenses")

    def __init__(self, revenue: float, expenses: float):
        # Initialize the revenue and expenses attributes using the descriptors.
        self.revenue = revenue
        self.expenses = expenses

    @LazyProperty
    def profit(self) -> float:
        """
        Lazy computation of profit (revenue - expenses).
        This avoids unnecessary computation until the value is accessed.
        """
        print("\nCalculating profit...")
        return self.revenue - self.expenses


if __name__ == "__main__":
    # Create an instance of BusinessMetrics with random revenue and expenses.
    metrics = BusinessMetrics(
        revenue=random.randint(50_000, 250_000),
        expenses=random.randint(20_000, 100_000),
    )

    # Accessing revenue and expenses
    # Demonstrates the PositiveNumber descriptor ensuring valid values.
    print(f"Revenue: {metrics.revenue:,}")
    print(f"Expenses: {metrics.expenses:,}")

    # Accessing profit (lazy-loaded)
    # Demonstrates the LazyProperty descriptor calculating profit only when accessed.
    print(f"Profit: {metrics.profit:,}")  # Triggers calculation
    print(f"Profit (cached): {metrics.profit:,}")  # Uses cached value

    # Attempting to set invalid values
    # Demonstrates the PositiveNumber descriptor raising an error for invalid input.
    try:
        metrics.revenue = random.randint(-5_000, 5_000)  # Raises ValueError if negative
    except ValueError as e:
        print(e)
