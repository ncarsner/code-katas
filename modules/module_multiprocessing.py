from multiprocessing import Pool, Process, Queue, cpu_count
from typing import List, Any, Callable, Optional
import time
import random

"""
Python's `multiprocessing` module is useful for parallel processing tasks such as data transformation and large dataset summation; processing large volumes of data efficiently and in parallel.
"""


def parallel_map(func: Callable[[Any], Any], data: List[Any], processes: Optional[int] = None) -> List[Any]:
    """
    Applies a function to a list of data in parallel using a process pool.

    Args:
        func: Function to apply to each element.
        data: List of data to process.
        processes: Number of worker processes to use (defaults to number of CPUs).

    Returns:
        List of results.
    """
    with Pool(processes=processes or cpu_count()) as pool:
        results = pool.map(func, data)
    return results


def worker_sum(numbers: List[int], output: Queue) -> None:
    """
    Worker function to sum a list of numbers and put the result in a queue.

    Args:
        numbers: List of integers to sum.
        output: Multiprocessing queue to store the result.
    """
    result = sum(numbers)
    output.put(result)


def parallel_sum(data: List[int], chunk_size: int = 1000) -> int:
    """
    Sums a large list of numbers in parallel by splitting into chunks.

    Args:
        data: List of integers to sum.
        chunk_size: Size of each chunk to process in parallel.

    Returns:
        The total sum as an integer.
    """
    output = Queue()
    processes = []
    # Split data into chunks
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        p = Process(target=worker_sum, args=(chunk, output))
        processes.append(p)
        p.start()
    # Collect results
    total = 0
    for _ in processes:
        total += output.get()
    for p in processes:
        p.join()
    return total


def business_task(record: dict) -> dict:
    """
    Process a business record (e.g. data transformation).

    Args:
        record: Dictionary representing a data record.

    Returns:
        Processed record as a dictionary.
    """
    # Simulate a transformation (e.g., currency conversion, data cleaning)
    time.sleep(round(random.uniform(0.1, 1), 1))  # Simulate I/O or computation
    record['processed'] = True
    return record


def main():
    # Parallel map for data transformation
    records = [{'id': i, 'value': i * 10} for i in range(10)]
    print("Processing records in parallel...")
    processed_records = parallel_map(business_task, records)
    print(processed_records)

    # Parallel sum for large datasets
    large_data = list(range(1_000_000))
    print("Summing large dataset in parallel...")
    total = parallel_sum(large_data, chunk_size=100_000)
    print(f"Total sum: {total}")

    # Troubleshooting tips:
    # - Ensure all functions used by multiprocessing are defined at the top level (not nested).
    # - Use if __name__ == '__main__': guard for Windows compatibility.
    # - Use cpu_count() to scale processes to available hardware.
    # - Use Pool for simple parallel map/reduce, Process/Queue for custom workflows.


if __name__ == '__main__':
    main()
