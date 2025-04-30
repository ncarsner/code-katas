import requests
from typing import Any, Dict, Optional


def fetch_json_data(
    url: str, params: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Fetches JSON data from a given API endpoint.

    Args:
        url (str): The API endpoint URL.
        params (Optional[Dict[str, Any]]): Query parameters to include in the request.

    Returns:
        Dict[str, Any]: The JSON response from the API.

    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        response = requests.get(url, params=params, timeout=10)
        # Raise HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        raise


def download_file(url: str, save_path: str) -> None:
    """
    Downloads a file from a given URL and saves it to the specified path.

    Args:
        url (str): The URL of the file to download.
        save_path (str): The local path where the file will be saved.

    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        with requests.get(url, stream=True, timeout=10) as response:
            response.raise_for_status()
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(f"File downloaded successfully: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file from {url}: {e}")
        raise


def post_data(url: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sends a POST request with JSON data to a given API endpoint.

    Args:
        url (str): The API endpoint URL.
        data (Dict[str, Any]): The JSON data to send in the request body.

    Returns:
        Dict[str, Any]: The JSON response from the API.

    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting data to {url}: {e}")
        raise


if __name__ == "__main__":
    # Fetch JSON data from an API
    api_url = "https://jsonplaceholder.typicode.com/posts"
    try:
        posts = fetch_json_data(api_url, params={"userId": 1})
        print("Fetched posts:", posts)
    except Exception as e:
        print("Failed to fetch posts:", e)

    # Download a file
    file_url = "https://www.example.com/sample.pdf"
    try:
        download_file(file_url, "sample.pdf")
    except Exception as e:
        print("Failed to download file:", e)

    # Send a POST request
    post_url = "https://jsonplaceholder.typicode.com/posts"
    post_data_payload = {"title": "foo", "body": "bar", "userId": 1}
    try:
        response = post_data(post_url, post_data_payload)
        print("Post response:", response)
    except Exception as e:
        print("Failed to post data:", e)
