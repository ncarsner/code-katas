import threading
import time
from typing import List, Any, Dict

"""
Useful for parallel data fetching, concurrent file processing, and thread-safe data aggregation.
"""


def fetch_data_from_source(
    source: str, results: Dict[str, Any], lock: threading.Lock
) -> None:
    """
    Simulates fetching data from a data source (e.g., API, database).
    Stores the result in a shared dictionary in a thread-safe manner.

    Args:
        source (str): The data source identifier.
        results (dict): Shared dictionary to store results.
        lock (threading.Lock): Lock to ensure thread-safe writes.
    """
    print(f"Fetching data from {source}...")
    time.sleep(1)  # Simulate network/database delay
    data = f"Data from {source}"
    with lock:
        results[source] = data
    print(f"Finished fetching from {source}.")


def parallel_data_fetch(sources: List[str]) -> Dict[str, Any]:
    """
    Fetches data from multiple sources in parallel using threads.

    Args:
        sources (List[str]): List of data source identifiers.

    Returns:
        Dict[str, Any]: Dictionary mapping source to fetched data.
    """
    threads = []
    results: Dict[str, Any] = {}
    lock = threading.Lock()

    for source in sources:
        thread = threading.Thread(
            target=fetch_data_from_source, args=(source, results, lock)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


def process_file(filename: str) -> int:
    """
    Simulates processing a file and returns the number of lines.

    Args:
        filename (str): The file to process.

    Returns:
        int: Number of lines in the file (simulated).
    """
    print(f"Processing {filename}...")
    time.sleep(0.5)  # Simulate file processing time
    lines = len(filename) * 10  # Dummy calculation
    print(f"Finished processing {filename}. Lines: {lines}")
    return lines


def concurrent_file_processing(filenames: List[str]) -> List[int]:
    """
    Processes multiple files concurrently using threads.

    Args:
        filenames (List[str]): List of filenames.

    Returns:
        List[int]: List of line counts for each file.
    """
    results: List[int] = [0] * len(filenames)
    threads = []

    def worker(idx: int, fname: str):
        results[idx] = process_file(fname)

    for i, fname in enumerate(filenames):
        thread = threading.Thread(target=worker, args=(i, fname))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


class ThreadSafeAggregator:
    """
    Thread-safe aggregator for collecting results from multiple threads.
    Useful for BI tasks like aggregating metrics from parallel computations.
    """

    def __init__(self):
        self.lock = threading.Lock()
        self.data: List[Any] = []

    def add(self, value: Any) -> None:
        with self.lock:
            self.data.append(value)

    def get_all(self) -> List[Any]:
        with self.lock:
            return list(self.data)


def example_usage():
    # Use case: Parallel data fetch
    sources = ["db1", "api2", "csv3"]
    print("Starting parallel data fetch...")
    data = parallel_data_fetch(sources)
    print("Fetched data:", data)

    # Use case: Concurrent file processing
    files = ["sales.csv", "inventory.csv", "customers.csv"]
    print("\nStarting concurrent file processing...")
    line_counts = concurrent_file_processing(files)
    print("Line counts:", line_counts)

    # Use case: Thread-safe aggregation
    aggregator = ThreadSafeAggregator()

    def compute_metric(x: int):
        time.sleep(0.2)
        aggregator.add(x * x)

    threads = [threading.Thread(target=compute_metric, args=(i,)) for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("\nAggregated metrics:", aggregator.get_all())


if __name__ == "__main__":
    example_usage()

"""
TROUBLESHOOTING & EFFICIENCY TIPS:
- Use locks (threading.Lock) when sharing data between threads.
- Use threading.Thread.join() to ensure all threads complete before proceeding.
- For CPU-bound tasks, consider multiprocessing instead of threading due to Python's GIL.
- For I/O-bound tasks (API calls, file I/O), threading can improve performance.
- Use concurrent.futures.ThreadPoolExecutor for managing many threads efficiently.
"""
