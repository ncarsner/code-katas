import array
from typing import List
import random
from statistics import median

"""
The `array` module provides an efficient way to store and manipulate homogeneous data types. The examples below are tailored for business intelligence developers/analysts who may need to handle large datasets efficiently.
"""


def create_sales_array(sales: List[int]) -> array.array:
    """
    Create an array of integers to store daily sales data.

    Args:
        sales (List[int]): A list of daily sales figures.

    Returns:
        array.array: An array containing the sales data.
    """
    # Using 'i' type code for signed integers
    return array.array("i", sales)


def calculate_total_sales(sales_array: array.array) -> int:
    """
    Calculate the total sales from the sales array.

    Args:
        sales_array (array.array): An array of daily sales figures.

    Returns:
        int: The total sales.
    """
    return sum(sales_array)


def filter_high_sales(sales_array: array.array, threshold: int) -> array.array:
    """
    Filter sales that exceed a given threshold.

    Args:
        sales_array (array.array): An array of daily sales figures.
        threshold (int): The sales threshold.

    Returns:
        array.array: An array containing sales figures above the threshold.
    """
    # Using list comprehension to filter and create a new array
    return array.array(
        sales_array.typecode, (sale for sale in sales_array if sale > threshold)
    )


def scale_sales_data(sales_array: array.array, scale_factor: float) -> array.array:
    """
    Scale sales data by a given factor (e.g., for currency conversion).

    Args:
        sales_array (array.array): An array of daily sales figures.
        scale_factor (float): The factor by which to scale the sales data.

    Returns:
        array.array: An array containing the scaled sales data.
    """
    # Using list comprehension to apply scaling
    return array.array(
        sales_array.typecode, (int(sale * scale_factor) for sale in sales_array)
    )


if __name__ == "__main__":
    daily_sales = [random.choice(range(50, 500, 10)) for _ in range(8)]

    # Create an array from the sales data
    sales_array = create_sales_array(daily_sales)
    print(f"{sales_array=}")

    # Calculate total sales
    total_sales = calculate_total_sales(sales_array)
    print(f"{total_sales=:,}")

    # Filter sales above a threshold
    threshold = median(daily_sales)
    high_sales = filter_high_sales(sales_array, threshold)
    print(f"Sales above {threshold}:", high_sales)

    # Scale sales data (e.g., convert to another currency)
    increase = random.choice([x / 100 for x in range(5, 35, 5)]) + 1
    scaled_sales = scale_sales_data(sales_array, increase)
    print(f"Scaled Sales ({increase - 1:.0%} increase):", scaled_sales)
