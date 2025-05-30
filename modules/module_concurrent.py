from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed, Future
from typing import List, Dict, Any, Callable
import time
import json
import random

"""
Provides a high-level interface for asynchronously executing callables using threads or processes. Useful for parallelize data processing, API calls, or I/O-bound tasks to improve performance and efficiency.
"""


def fetch_data_from_api(api_endpoint: str) -> Dict[str, Any]:
    """
    Simulates fetching data from an API endpoint.
    In real-world use, replace with actual requests.get or similar.

    Args:
        api_endpoint (str): The API endpoint URL.

    Returns:
        Dict[str, Any]: Simulated API response.
    """
    # Simulate network delay
    time.sleep(random.uniform(0.5, 2.0))
    return {"endpoint": api_endpoint, "data": random.randint(1, 100)}


def parallel_api_calls(endpoints: List[str], max_workers: int = 5) -> List[Dict[str, Any]]:
    """
    Fetches data from multiple API endpoints in parallel using ThreadPoolExecutor.

    Args:
        endpoints (List[str]): List of API endpoint URLs.
        max_workers (int): Maximum number of threads to use.

    Returns:
        List[Dict[str, Any]]: List of API responses.
    """
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all API calls to the thread pool
        future_to_endpoint = {executor.submit(fetch_data_from_api, ep): ep for ep in endpoints}
        for future in as_completed(future_to_endpoint):
            endpoint = future_to_endpoint[future]
            try:
                data = future.result()
                results.append(data)
            except Exception as exc:
                print(f"API call to {endpoint} generated an exception: {exc}")
    return results


def cpu_intensive_task(n: int) -> int:
    """
    Simulates a CPU-bound task (e.g., calculating factorial).

    Args:
        n (int): Input number.

    Returns:
        int: Result of computation.
    """
    def factorial(x: int) -> int:
        return 1 if x == 0 else x * factorial(x - 1)
    return factorial(n)


def parallel_cpu_tasks(numbers: List[int], max_workers: int = 4) -> List[int]:
    """
    Processes CPU-bound tasks in parallel using ProcessPoolExecutor.

    Args:
        numbers (List[int]): List of integers to process.
        max_workers (int): Maximum number of processes to use.

    Returns:
        List[int]: List of computation results.
    """
    results = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(cpu_intensive_task, n) for n in numbers]
        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as exc:
                print(f"CPU task generated an exception: {exc}")
    return results


def run_with_timeout(func: Callable, args: tuple, timeout: float) -> Any:
    """
    Runs a function asynchronously and enforces a timeout.

    Args:
        func (Callable): The function to run.
        args (tuple): Arguments to pass to the function.
        timeout (float): Timeout in seconds.

    Returns:
        Any: The result of the function, or None if timed out.
    """
    with ThreadPoolExecutor(max_workers=1) as executor:
        future: Future = executor.submit(func, *args)
        try:
            return future.result(timeout=timeout)
        except Exception as exc:
            print(f"Function {func.__name__} timed out or raised exception: {exc}")
            return None


if __name__ == "__main__":
    # Parallel API calls (I/O-bound)
    endpoints = [f"https://api.example.com/data/{i}" for i in range(5)]
    print("Fetching API data in parallel...")
    api_results = parallel_api_calls(endpoints)
    print("API Results:")
    print(json.dumps(api_results, indent=2))

    # Parallel CPU-bound tasks (e.g., factorials)
    numbers = [random.randint(2, 20) for _ in range(5)]
    print(f"{numbers=}")
    print("Processing CPU-bound tasks in parallel...")
    cpu_results = parallel_cpu_tasks(numbers)
    print("CPU Results:")
    for res in cpu_results:
        print(f"{res:_}")

    # Running a function with a timeout
    print("\nRunning a function with a timeout...")
    result = run_with_timeout(fetch_data_from_api, ("https://api.example.com/slow",), timeout=1.0)
    print(f"Timeout Result: {result}")

"""
TROUBLESHOOTING & TIPS:
- Use ThreadPoolExecutor for I/O-bound tasks (API calls, file I/O).
- Use ProcessPoolExecutor for CPU-bound tasks (data crunching, heavy computations).
- Use as_completed() to process results as soon as they're ready.
- Always handle exceptions from futures to avoid silent failures.
- Tune max_workers based on your workload and system resources.
"""
