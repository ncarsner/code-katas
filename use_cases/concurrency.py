import time
from typing import List, Dict

import concurrent.futures


def fetch_data_from_api(api_url: str) -> Dict:
    """
    Simulates fetching data from an API.

    Args:
        api_url (str): The URL of the API endpoint.

    Returns:
        Dict: Simulated JSON response from the API.
    """
    time.sleep(2)  # Simulate network delay
    return {"url": api_url, "data": f"Sample data from {api_url}"}


def process_data(data: Dict) -> Dict:
    """
    Simulates processing the fetched data.

    Args:
        data (Dict): The raw data fetched from the API.

    Returns:
        Dict: Processed data.
    """
    time.sleep(1)  # Simulate processing time
    data["processed"] = True
    return data


def main(api_urls: List[str]) -> List[Dict]:
    """
    Fetches and processes data concurrently from multiple API endpoints.

    Args:
        api_urls (List[str]): List of API URLs to fetch data from.

    Returns:
        List[Dict]: List of processed data.
    """
    processed_results = []

    # Use ThreadPoolExecutor for I/O-bound tasks like API calls
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Step 1: Fetch data concurrently
        fetch_futures = {
            executor.submit(fetch_data_from_api, url): url for url in api_urls
        }
        fetched_data = []
        for future in concurrent.futures.as_completed(fetch_futures):
            try:
                fetched_data.append(future.result())
            except Exception as e:
                print(f"Error fetching data from {fetch_futures[future]}: {e}")

        # Step 2: Process data concurrently
        process_futures = {
            executor.submit(process_data, data): data for data in fetched_data
        }
        for future in concurrent.futures.as_completed(process_futures):
            try:
                processed_results.append(future.result())
            except Exception as e:
                print(f"Error processing data: {e}")

    return processed_results


if __name__ == "__main__":
    # Example API URLs
    api_urls = [
        "https://api.example.com/data1",
        "https://api.example.com/data2",
        "https://api.example.com/data3",
        "https://api.example.com/data4",
    ]

    start_time = time.time()
    results = main(api_urls)
    end_time = time.time()

    print("Processed Results:")
    for result in results:
        print(result)

    print(f"Time taken: {end_time - start_time:.2f} seconds")
