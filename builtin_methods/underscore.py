from typing import List, Tuple
import random


def calculate_total_sales(sales_data: List[Tuple[str, float]]) -> float:
    """
    Calculate the total sales from a list of sales data.

    Args:
        sales_data (List[Tuple[str, float]]): A list of tuples where each tuple contains
                                              a product name and its sales amount.

    Returns:
        float: The total sales amount.
    """
    # _ ignores str value in a tuple
    total_sales = sum(amount for _, amount in sales_data)
    return total_sales


def format_large_number(number: int) -> str:
    """
    Format a large number with underscores for better readability.

    Args:
        number (int): A large integer to format.

    Returns:
        str: The formatted number as a string.
    """
    return f"{number:_}"


def extract_special_methods(obj: object) -> List[str]:
    """
    Extract all special methods (methods with double underscores) of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        List[str]: A list of special method names.
    """
    return [
        method
        for method in dir(obj)
        if method.startswith("__") and method.endswith("__")
    ]


def ignore_unused_values(data: List[Tuple[str, int, float]]) -> List[float]:
    """
    Extract only the third value from each tuple in the data, ignoring the others.

    Args:
        data (List[Tuple[str, int, float]]): A list of tuples containing three elements.

    Returns:
        List[float]: A list of the third values from each tuple.
    """
    return [value for _, _, value in data]


if __name__ == "__main__":
    # Ignoring values in tuples
    product_list = ["Shirts", "Pants", "Shoes", "Hats", "Accessories", "Jackets"]
    random.shuffle(product_list)
    selected_products = product_list[:3]
    # print(f"Selected Products: {selected_products}")

    sales = [
        (selected_products[0], random.uniform(1000, 2000)),
        (selected_products[1], random.uniform(3000, 4000)),
        (selected_products[2], random.uniform(500, 1000)),
    ]
    total = calculate_total_sales(sales)
    print(f"Total Sales: ${total:.2f}")

    # Readable large numbers
    large_number = int(round(random.uniform(1, 2), 5) * 10000000)
    formatted_number = format_large_number(large_number)
    print(f"Formatted Large Number: {formatted_number}")

    # Accessing special methods
    special_methods = extract_special_methods("")
    print(f"Special Methods of a String: {special_methods}")

    # Ignoring unused values in tuples
    data = [
        ("Alex", random.randint(21, 65), random.choice(range(50000, 125001, 5000))),
        ("Blake", random.randint(21, 65), random.choice(range(50000, 125001, 5000))),
        ("Chris", random.randint(21, 65), random.choice(range(50000, 125001, 5000))),
    ]
    salaries = ignore_unused_values(data)
    print(f"Salaries: {salaries}")
    print(f"Formatted: {[format_large_number(salary) for salary in salaries]}")
