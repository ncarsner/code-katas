import gc
from typing import List

"""
This script demonstrates the concept of memory leaks in Python, and how to recognize and troubleshoot them. Memory leaks in Python are rare due to garbage collection, but they can still occur in certain scenarios, such as circular references or improper resource management.

The examples below are tailored for BI developers or analysts who work with large datasets.
"""


# Memory Leak Due to Circular References
class Node:
    """
    A simple class to demonstrate circular references.
    """

    def __init__(self, value: int):
        self.value = value
        self.next: "Node | None" = None


def create_circular_reference() -> None:
    """
    Creates a circular reference that prevents garbage collection.
    """
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node2.next = node1  # Circular reference

    # These objects will not be garbage collected due to the circular reference.
    print("Circular reference created. Nodes are not garbage collected.")


# Memory Leak Due to Unreleased Resources
def load_large_dataset() -> List[int]:
    """
    Simulates loading a large dataset into memory.
    """
    return [i for i in range(10**6)]  # Large dataset


def process_data_with_leak() -> None:
    """
    Processes data but forgets to release the reference, causing a memory leak.
    """
    large_data = load_large_dataset()
    # Forgetting to release `large_data` after processing can cause memory issues.
    print("Large dataset loaded but not released.")


# Proper Resource Management to Avoid Memory Leaks
def process_data_properly() -> None:
    """
    Processes data and ensures proper resource management.
    """
    large_data = load_large_dataset()
    # Process the data here...
    print("Processing data...")
    del large_data  # Explicitly release the reference to free memory.
    print("Large dataset released.")


# Troubleshooting Memory Leaks
def detect_memory_leaks() -> None:
    """
    Demonstrates how to detect memory leaks using garbage collection.
    """
    gc.collect()  # Force garbage collection
    print(f"Unreachable objects: {gc.garbage}")
    print(
        "If there are unreachable objects, investigate circular references or unclosed resources."
    )


if __name__ == "__main__":
    # Memory leak due to circular reference
    create_circular_reference()

    # Memory leak due to unreleased resources
    process_data_with_leak()

    # Proper resource management
    process_data_properly()

    # Detect memory leaks
    detect_memory_leaks()
