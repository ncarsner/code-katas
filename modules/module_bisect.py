import bisect
from typing import List, Any
import random


"""
The `bisect` module is useful for maintaining sorted lists, searching, and categorizing data efficiently.

Functions demonstrated:
- bisect.bisect_left
- bisect.bisect_right
- bisect.insort_left
- bisect.insort_right
"""


def find_insert_position(sorted_list: List[Any], value: Any) -> int:
    """
    Find the index where `value` should be inserted to keep `sorted_list` sorted (leftmost position).
    Useful for categorizing or bucketing data.

    Args:
        sorted_list: A list sorted in ascending order.
        value: The value to locate.

    Returns:
        Index where value should be inserted.
    """
    return bisect.bisect_left(sorted_list, value)


def insert_sorted(sorted_list: List[Any], value: Any) -> None:
    """
    Insert `value` into `sorted_list` in sorted order (rightmost position).
    Useful for maintaining a sorted list of KPIs, thresholds, or scores.

    Args:
        sorted_list: A list sorted in ascending order.
        value: The value to insert.

    Returns:
        None. The list is modified in place.
    """
    bisect.insort_right(sorted_list, value)


def categorize_value(buckets: List[float], value: float) -> int:
    """
    Categorize a value into a bucket using bisect.
    For example, segmenting sales amounts into predefined ranges.

    Args:
        buckets: Sorted list of bucket thresholds (e.g., [100, 500, 1000]).
        value: The value to categorize.

    Returns:
        The index of the bucket the value falls into.
    """
    return bisect.bisect_right(buckets, value)


if __name__ == "__main__":
    # Maintaining a sorted list of sales figures
    sales_figures = [random.randrange(1000, 5000, 250) for _ in range(5)]
    sales_figures.sort()
    print(f"Original sales: {sales_figures}")
    new_sale = random.randrange(1000, 5000, 250)
    insert_sorted(sales_figures, new_sale)
    print(f"After inserting {new_sale}: {sales_figures}")

    # Finding where to insert a new KPI score
    kpi_scores = [round(random.uniform(0, 1), 2) for _ in range(5)]
    kpi_scores.sort()
    print(f"\nOriginal KPI scores: {kpi_scores}")
    score = round(random.uniform(0, 1), 2)
    pos = find_insert_position(kpi_scores, score)
    print(f"Insert position for KPI score {score}: {pos}")

    # Categorizing a value into buckets (e.g., sales tiers)
    sales_buckets = [random.randrange(500, 2000, 250) for _ in range(5)]
    sale_amount = random.randrange(1000, 5000, 250)
    bucket_index = categorize_value(sales_buckets, sale_amount)
    print(f"\nSale amount {sale_amount} falls into bucket index: {bucket_index}")

    # Troubleshooting - inserting duplicate values
    print("\nInserting value 1700 into sales_figures.")
    insert_sorted(sales_figures, 1700)
    print(f"After inserting duplicate: {sales_figures}")

    # Note: bisect_left vs bisect_right
    # bisect_left returns the first suitable position (for stable sorting)
    # bisect_right returns the last suitable position (for grouping duplicates)
