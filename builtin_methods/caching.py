from functools import lru_cache
from typing import List, Dict


def fetch_data_from_database(query: str) -> List[Dict]:
    """
    Simulates a database query. In a real-world scenario, this function would
    connect to a database and execute the query. Here, it simply returns a mock result.
    """
    print(f"Executing query: {query}")
    # Simulated delay for database query
    import time

    time.sleep(2)
    return [{"id": 1, "value": "A"}, {"id": 2, "value": "B"}]


@lru_cache(maxsize=128)
def get_cached_data(query: str) -> List[Dict]:
    """
    Fetches data from the database and caches the result to avoid redundant queries.

    Args:
        query (str): The SQL query string to execute.

    Returns:
        List[Dict]: The result of the query as a list of dictionaries.
    """
    return fetch_data_from_database(query)


def process_data(data: List[Dict]) -> List[str]:
    """
    Processes the data into a list of formatted strings.

    Args:
        data (List[Dict]): The data to process.

    Returns:
        List[str]: A list of formatted strings based on the input data.
    """
    return [f"ID: {item['id']}, Value: {item['value']}" for item in data]


def main():
    query = "SELECT * FROM example_table"

    # First call - fetched from the database
    print("First call:")
    data = get_cached_data(query)
    print(process_data(data))

    # Second call - retrieved from the cache
    print("\nSecond call (cached):")
    data = get_cached_data(query)
    print(process_data(data))

    # Cache invalidated by clearing the cache
    print("\nClearing cache and re-fetching:")
    get_cached_data.cache_clear()
    data = get_cached_data(query)
    print(process_data(data))


if __name__ == "__main__":
    main()
