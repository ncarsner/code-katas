import base64
import json
from typing import Dict, Optional, Union
from pathlib import Path

"""
Practical uses of Python's base64 module are:
- Encoding/decoding API credentials
- Handling binary data in JSON/REST APIs
- Image data encoding for web applications
- Database BLOB handling
- Secure configuration management
"""


def encode_api_credentials(username: str, password: str) -> str:
    """
    Encode API credentials in Base64 format (commonly used in HTTP Basic Auth).

    Args:
        username: API username
        password: API password

    Returns:
        Base64 encoded string in format "username:password"

    Example:
        >>> token = encode_api_credentials("user@company.com", "secret123")
        >>> # Use in headers: {"Authorization": f"Basic {token}"}
    """
    credentials = f"{username}:{password}"
    encoded_bytes = base64.b64encode(credentials.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decode_api_credentials(encoded_token: str) -> Dict[str, str]:
    """
    Decode Base64 encoded credentials back to username and password.

    Args:
        encoded_token: Base64 encoded credential string

    Returns:
        Dictionary with 'username' and 'password' keys

    Raises:
        ValueError: If token format is invalid
    """
    try:
        decoded_bytes = base64.b64decode(encoded_token)
        credentials = decoded_bytes.decode("utf-8")
        username, password = credentials.split(":", 1)
        return {"username": username, "password": password}
    except Exception as e:
        raise ValueError(f"Invalid credential token: {e}")


def encode_image_for_api(image_path: Union[str, Path]) -> str:
    """
    Encode an image file to Base64 for embedding in JSON/REST APIs.

    Common use case: Sending images to ML models, document processing APIs,
    or storing small images in databases.

    Args:
        image_path: Path to the image file

    Returns:
        Base64 encoded string of the image

    Example:
        >>> encoded = encode_image_for_api("logo.png")
        >>> payload = {"image": encoded, "format": "png"}
    """
    image_path = Path(image_path)
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
        encoded = base64.b64encode(image_bytes)
        return encoded.decode("utf-8")


def decode_image_from_api(encoded_data: str, output_path: Union[str, Path]) -> None:
    """
    Decode Base64 image data and save to file.

    Args:
        encoded_data: Base64 encoded image string
        output_path: Where to save the decoded image

    Example:
        >>> api_response = {"image": "iVBORw0KG..."}
        >>> decode_image_from_api(api_response["image"], "output.png")
    """
    output_path = Path(output_path)
    image_bytes = base64.b64decode(encoded_data)
    with open(output_path, "wb") as output_file:
        output_file.write(image_bytes)


def encode_binary_data_for_json(binary_data: bytes) -> str:
    """
    Encode binary data for safe transmission in JSON (which only supports text).

    Use cases:
    - Storing BLOB data from databases in JSON format
    - API responses containing binary attachments
    - ETL pipelines moving binary data between systems

    Args:
        binary_data: Raw bytes to encode

    Returns:
        Base64 encoded string safe for JSON
    """
    return base64.b64encode(binary_data).decode("utf-8")


def decode_binary_data_from_json(encoded_str: str) -> bytes:
    """
    Decode Base64 string back to binary data.

    Args:
        encoded_str: Base64 encoded string from JSON

    Returns:
        Original binary data as bytes
    """
    return base64.b64decode(encoded_str)


def create_data_uri(file_path: Union[str, Path], mime_type: str) -> str:
    """
    Create a data URI for embedding files in HTML/CSS (useful for BI dashboards).

    Args:
        file_path: Path to the file
        mime_type: MIME type (e.g., 'image/png', 'application/pdf')

    Returns:
        Complete data URI string

    Example:
        >>> uri = create_data_uri("chart.png", "image/png")
        >>> html = f'<img src="{uri}" alt="Chart"/>'
    """
    file_path = Path(file_path)
    with open(file_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode("utf-8")
        return f"data:{mime_type};base64,{encoded}"


def encode_config_value(value: str) -> str:
    """
    Encode configuration values (simple obfuscation, NOT encryption).

    Note: This is NOT secure encryption. Use only for:
    - Avoiding plain text exposure in config files
    - Simple obfuscation in version control
    - For real security, use proper encryption libraries

    Args:
        value: Configuration value to encode

    Returns:
        Base64 encoded string
    """
    return base64.b64encode(value.encode("utf-8")).decode("utf-8")


def decode_config_value(encoded_value: str) -> str:
    """
    Decode configuration values encoded with encode_config_value().

    Args:
        encoded_value: Base64 encoded configuration value

    Returns:
        Decoded string
    """
    return base64.b64decode(encoded_value).decode("utf-8")


def url_safe_encode(data: str) -> str:
    """
    Encode data using URL-safe Base64 (replaces +/ with -_).

    Use cases:
    - Encoding data for URL parameters
    - JWT tokens
    - Filenames that need to be URL-safe

    Args:
        data: String to encode

    Returns:
        URL-safe Base64 encoded string (without padding)
    """
    encoded_bytes = base64.urlsafe_b64encode(data.encode("utf-8"))
    return encoded_bytes.decode("utf-8").rstrip("=")


def url_safe_decode(encoded_data: str) -> str:
    """
    Decode URL-safe Base64 encoded data.

    Args:
        encoded_data: URL-safe Base64 string

    Returns:
        Decoded string
    """
    # Add padding if needed
    padding = 4 - (len(encoded_data) % 4)
    if padding != 4:
        encoded_data += "=" * padding

    decoded_bytes = base64.urlsafe_b64decode(encoded_data)
    return decoded_bytes.decode("utf-8")


def batch_encode_database_blobs(blob_data_list: list[bytes]) -> list[str]:
    """
    Batch encode multiple BLOB fields for ETL operations.

    Useful for:
    - Extracting binary data from SQL databases
    - Preparing data for NoSQL/document stores
    - Data migration pipelines

    Args:
        blob_data_list: List of binary data objects

    Returns:
        List of Base64 encoded strings
    """
    return [base64.b64encode(blob).decode("utf-8") for blob in blob_data_list]


if __name__ == "__main__":
    # API Authentication
    print("=== API Credentials Example ===")
    auth_token = encode_api_credentials("data_engineer@company.com", "myP@ssw0rd")
    print(f"Auth Token: {auth_token}")
    decoded_creds = decode_api_credentials(auth_token)
    print(f"Decoded: {decoded_creds}")

    # URL-safe encoding for query parameters
    print("\n=== URL-Safe Encoding Example ===")
    query_filter = '{"status": "active", "date": "2024-01-01"}'
    encoded_filter = url_safe_encode(query_filter)
    print(f"Encoded Filter: {encoded_filter}")
    print(f"Decoded Filter: {url_safe_decode(encoded_filter)}")

    # Configuration obfuscation
    print("\n=== Configuration Example ===")
    db_password = "SuperSecretPassword123!"
    encoded_pwd = encode_config_value(db_password)
    print(f"Config file value: {encoded_pwd}")
    print(f"Decoded at runtime: {decode_config_value(encoded_pwd)}")

    # Binary data in JSON
    print("\n=== Binary Data in JSON Example ===")
    sample_binary = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR"
    json_safe = encode_binary_data_for_json(sample_binary)
    print(f"JSON-safe binary: {json_safe}")
    print(f"Original binary recovered: {decode_binary_data_from_json(json_safe)}")
