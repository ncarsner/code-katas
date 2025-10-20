import heapq
from typing import List, Tuple, Iterable
import random


def get_top_n_sales(sales: List[Tuple[str, float]], n: int) -> List[Tuple[str, float]]:
    """
    Returns the top n sales records by amount.

    Args:
        sales: List of tuples (customer, sale_amount).
        n: Number of top sales to retrieve.

    Returns:
        List of top n sales records sorted by amount descending.
    """
    # heapq.nlargest is efficient for small n compared to len(sales)
    return heapq.nlargest(n, sales, key=lambda x: x[1])


def get_bottom_n_sales(sales: List[Tuple[str, float]], n: int) -> List[Tuple[str, float]]:
    """
    Returns the bottom n sales records by amount.

    Args:
        sales: List of tuples (customer, sale_amount).
        n: Number of bottom sales to retrieve.

    Returns:
        List of bottom n sales records sorted by amount ascending.
    """
    # heapq.nsmallest is efficient for small n compared to len(sales)
    return heapq.nsmallest(n, sales, key=lambda x: x[1])


def maintain_top_n_heap(stream: Iterable[Tuple[str, float]], n: int) -> List[Tuple[float, str]]:
    """
    Maintains a min-heap of the top n sales as data streams in.

    Args:
        stream: Iterable of (customer, sale_amount).
        n: Number of top sales to keep.

    Returns:
        List of top n sales as a heap (sale_amount, customer).
    """
    heap: List[Tuple[float, str]] = []
    for customer, amount in stream:
        if len(heap) < n:
            heapq.heappush(heap, (amount, customer))
        else:
            # Push new item and pop smallest if necessary
            heapq.heappushpop(heap, (amount, customer))
    # The heap is not sorted; use heapq.nlargest to get sorted results if needed
    return heap


def heap_sort(data: List[float]) -> List[float]:
    """
    Sorts a list of numbers using a heap.

    Args:
        data: List of numbers.

    Returns:
        Sorted list of numbers.
    """
    heapq.heapify(data)  # In-place transform to heap
    return [heapq.heappop(data) for _ in range(len(data))]


def merge_sorted_sales(*sales_lists: List[Tuple[str, float]]) -> List[Tuple[str, float]]:
    """
    Merges multiple sorted sales lists into a single sorted list.

    Args:
        *sales_lists: Variable number of sorted sales lists.

    Returns:
        Single merged and sorted list.
    """
    # heapq.merge returns an iterator over the sorted values
    return list(heapq.merge(*sales_lists, key=lambda x: x[1]))


if __name__ == "__main__":
    sales = [*(range(400, 2100, 50))]
    sales_data = [
        ("Alex", random.choice(sales)),
        ("Blake", random.choice(sales)),
        ("Chris", random.choice(sales)),
        ("Dillon", random.choice(sales)),
        ("Elliott", random.choice(sales)),
    ]

    print("Top 3 sales:")
    print(get_top_n_sales(sales_data, 3))

    print("\nBottom 2 sales:")
    print(get_bottom_n_sales(sales_data, 2))

    print("\nMaintaining top 2 sales in a stream:")
    stream = random.sample(sales_data, 3)

    heap = maintain_top_n_heap(stream, 2)
    print(heapq.nlargest(2, heap))  # Sorted output

    print("\nHeap sort example:")
    amounts = [x[1] for x in sales_data]
    print(heap_sort(amounts.copy()))

    print("\nMerging two sorted sales lists:")
    sales1 = [("Alex", random.choice(sales)), ("Chris", random.choice(sales))]
    sales2 = [("Blake", random.choice(sales)), ("Dillon", random.choice(sales))]
    print(merge_sorted_sales(sales1, sales2))

"""
Troubleshooting & Efficiency Tips:
- heapq.nlargest/nsmallest are best for small n; for large n, consider sorting.
- heapq.heapify is O(n), heappush/heappop are O(log n).
- Heaps are not sorted; use heapq.nlargest/nsmallest to get sorted output.
- For merging, input lists must be sorted.
- For large data streams, maintain a fixed-size heap for top/bottom n.
"""
