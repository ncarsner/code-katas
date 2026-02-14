import bisect
from typing import List, Any, Sequence
import random


"""
Useful for maintaining sorted lists, searching, and categorizing data efficiently.
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


def categorize_value(buckets: Sequence[float], value: float) -> int:
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


def get_grade(score: float) -> str:
    """
    Example of categorizing a score into letter grades using bisect.
    Uses standard US academic grading scale.

    Args:
        score: A numeric score (0-100).

    Returns:
        Letter grade (A+, A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F).
    """
    thresholds = [60, 63, 67, 70, 73, 77, 80, 83, 87, 90, 93, 97]  # Grade thresholds (minimum scores)
    grades = ['F', 'D-', 'D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+']  # Corresponding grades
    return grades[bisect.bisect(thresholds, score)]


def find_percentile_rank(scores: List[float], new_score: float) -> float:
    """
    Determine what percentile a new score falls into based on existing scores.
    Useful for test score analysis or performance tracking.

    Args:
        scores: Sorted list of existing scores.
        new_score: The score to rank.

    Returns:
        Percentile rank (0-100).
    """
    if not scores:
        return 0.0
    position = bisect.bisect_right(scores, new_score)
    return (position / len(scores)) * 100


if __name__ == "__main__":
    # Maintain a sorted list of sales figures
    sales_figures = [random.randrange(1000, 5000, 250) for _ in range(5)]
    sales_figures.sort()
    print(f"Original sales: {sales_figures}")
    new_sale = random.randrange(1000, 5000, 250)
    insert_sorted(sales_figures, new_sale)
    print(f"After inserting {new_sale}: {sales_figures}")

    # Find insert position for a new KPI score
    kpi_scores = [round(random.uniform(0, 1), 2) for _ in range(5)]
    kpi_scores.sort()
    print(f"\nOriginal KPI scores: {kpi_scores}")
    score = round(random.uniform(0, 1), 2)
    pos = find_insert_position(kpi_scores, score)
    print(f"Insert position for KPI score {score}: {pos}")

    # Categorize a value into buckets (e.g., sales tiers)
    sales_buckets = [random.randrange(500, 2000, 250) for _ in range(5)]
    sale_amount = random.randrange(1000, 5000, 250)
    bucket_index = categorize_value(sales_buckets, sale_amount)
    print(f"\nSale amount {sale_amount} falls into bucket index: {bucket_index}")

    # Troubleshooting - inserting duplicate values
    print("\nInserting value 1700 into sales_figures.")
    insert_sorted(sales_figures, 1700)
    print(f"After inserting duplicate: {sales_figures}")

    # Categorize a score into letter grades
    score = random.randint(0, 100)
    grade = get_grade(score)
    print(f"\nScore {score} receives grade: {grade}")

    # Find percentile rank
    existing_scores = sorted([random.uniform(0, 100) for _ in range(20)])
    new_score = random.uniform(0, 100)
    percentile = find_percentile_rank(existing_scores, new_score)
    print(f"\nNew score {new_score:.2f} is in the {percentile:.0f}th percentile among existing scores.")

    # Note: bisect_left vs bisect_right
    # bisect_left returns the first suitable position (for stable sorting)
    # bisect_right returns the last suitable position (for grouping duplicates)
