import urllib3
from typing import Dict, Any, Optional, Tuple
import json

"""
Practical examples including functions for making GET requests, downloading files, and handling errors.
"""


# Create a reusable PoolManager instance for efficient HTTP connections
http = urllib3.PoolManager()


def fetch_json(url: str, headers: Optional[Dict[str, str]] = None) -> Optional[Dict[str, Any]]:
    """
    Fetches JSON data from a given URL using a GET request.

    Args:
        url (str): The URL to fetch data from.
        headers (Optional[Dict[str, str]]): Optional HTTP headers.

    Returns:
        Optional[Dict[str, Any]]: Parsed JSON data if successful, None otherwise.

    Raises:
        urllib3.exceptions.HTTPError: For network-related errors.
    """
    try:
        response = http.request("GET", url, headers=headers)
        if response.status == 200:
            # Decode JSON response
            return json.loads(response.data.decode("utf-8"))
        else:
            print(f"Error: Received status code {response.status}")
            return None
    except urllib3.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None


def download_file(url: str, output_path: str) -> bool:
    """
    Downloads a file from the specified URL and saves it locally.

    Args:
        url (str): The file URL.
        output_path (str): Local path to save the file.

    Returns:
        bool: True if download succeeded, False otherwise.
    """
    try:
        with http.request("GET", url, preload_content=False) as response:
            if response.status == 200:
                with open(output_path, "wb") as out_file:
                    for chunk in response.stream(1024):
                        out_file.write(chunk)
                return True
            else:
                print(f"Failed to download file. Status code: {response.status}")
                return False
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False


def get_status_and_headers(url: str) -> Tuple[int, Dict[str, str]]:
    """
    Retrieves the HTTP status code and headers from a URL.

    Args:
        url (str): The URL to check.

    Returns:
        Tuple[int, Dict[str, str]]: Status code and headers dictionary.
    """
    try:
        response = http.request("HEAD", url)
        return response.status, dict(response.headers)
    except Exception as e:
        print(f"Error fetching headers: {e}")
        return 0, {}


if __name__ == "__main__":
    # Fetch JSON data from a public API
    api_url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_json(api_url)
    print("Fetched JSON:", data)

    # Download a sample file
    file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
    if download_file(file_url, "dummy.pdf"):
        print("File downloaded successfully.")

    # Get status and headers
    status, headers = get_status_and_headers(api_url)
    print(f"Status: {status}, Headers: {headers}")

"""
Troubleshooting tips:
- Ensure URLs are correct and accessible.
- Handle exceptions for network errors and invalid responses.
- Use PoolManager for efficient connection reuse in production scripts.
- For HTTPS requests, urllib3 handles SSL by default, but you can customize certificates if needed.
"""
