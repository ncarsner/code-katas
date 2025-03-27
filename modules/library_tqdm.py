from tqdm import tqdm
import time
from typing import List


def process_items(items: List[int]) -> List[int]:
    """
    Process a list of items with a simulated delay, showing a progress bar.

    Args:
        items (List[int]): A list of integers to process.

    Returns:
        List[int]: A list of processed integers.
    """
    processed_items = []
    for item in tqdm(items, desc="Processing items", unit="item"):
        # Simulate a time-consuming process
        time.sleep(0.1)
        processed_items.append(item * 2)
    return processed_items


def download_files(file_urls: List[str]) -> None:
    """
    Simulate downloading files from given URLs, showing a progress bar.

    Args:
        file_urls (List[str]): A list of file URLs to download.
    """
    for url in tqdm(file_urls, desc="Downloading files", unit="file"):
        # Simulate a time-consuming download
        time.sleep(0.5)
        print(f"Downloaded {url}")


if __name__ == "__main__":
    # Example usage of process_items
    items_to_process = list(range(10))
    processed_items = process_items(items_to_process)
    print(f"Processed items: {processed_items}")

    # Example usage of download_files
    urls_to_download = [
        "http://example.com/file1",
        "http://example.com/file2",
        "http://example.com/file3",
    ]
    download_files(urls_to_download)
