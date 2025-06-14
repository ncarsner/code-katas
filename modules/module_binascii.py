import binascii
from typing import Union

"""
The `binascii` module provides utilities for converting between binary and ASCII.
- Encoding/decoding data for storage or transmission
- Handling binary data in ETL pipelines
- Working with checksums for data integrity
"""


def hexlify_data(data: bytes) -> str:
    """
    Convert binary data to a hexadecimal ASCII string.

    Args:
        data (bytes): The binary data to encode.

    Returns:
        str: Hexadecimal representation of the input data.

    Example:
        >>> hexlify_data(b'BI data')
        '42492064617461'
    """
    return binascii.hexlify(data).decode("ascii")


def unhexlify_data(hexstr: str) -> bytes:
    """
    Convert a hexadecimal ASCII string back to binary data.

    Args:
        hexstr (str): The hexadecimal string to decode.

    Returns:
        bytes: The original binary data.

    Example:
        >>> unhexlify_data('42492064617461')
        b'BI data'
    """
    return binascii.unhexlify(hexstr.encode("ascii"))


def base64_encode(data: bytes) -> str:
    """
    Encode binary data to a base64 ASCII string.

    Args:
        data (bytes): The binary data to encode.

    Returns:
        str: Base64 encoded string.

    Example:
        >>> base64_encode(b'BI data')
        'QkkgZGF0YQ=='
    """
    return binascii.b2a_base64(data).decode("ascii").strip()


def base64_decode(b64str: str) -> bytes:
    """
    Decode a base64 ASCII string back to binary data.

    Args:
        b64str (str): The base64 string to decode.

    Returns:
        bytes: The original binary data.

    Example:
        >>> base64_decode('QkkgZGF0YQ==')
        b'BI data'
    """
    return binascii.a2b_base64(b64str.encode("ascii"))


def compute_crc32(data: Union[bytes, str]) -> int:
    """
    Compute the CRC32 checksum of the input data.

    Args:
        data (Union[bytes, str]): Data to compute checksum for.

    Returns:
        int: CRC32 checksum as an integer.

    Example:
        >>> compute_crc32(b'important data')
        2743272262
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    return binascii.crc32(data) & 0xFFFFFFFF  # Ensure unsigned


def compute_adler32(data: Union[bytes, str]) -> int:
    """
    Compute the Adler-32 checksum of the input data.

    Args:
        data (Union[bytes, str]): Data to compute checksum for.

    Returns:
        int: Adler-32 checksum as an integer.

    Example:
        >>> compute_adler32('important data')
        212957285
    """
    if isinstance(data, str):
        data = data.encode("utf-8")
    return binascii.adler32(data) & 0xFFFFFFFF  # Ensure unsigned


if __name__ == "__main__":
    # Hexlify/unhexlify for storing binary IDs in text fields
    binary_id = b"\x01\x02\x03\x04"
    hex_id = hexlify_data(binary_id)
    print(f"Hex ID: {hex_id}")
    print(f"Original ID: {unhexlify_data(hex_id)}")

    # Base64 encode/decode for safe transmission in JSON or CSV
    sensitive_data = b"confidential_report"
    encoded = base64_encode(sensitive_data)
    print(f"Base64 Encoded: {encoded}")
    print(f"Decoded: {base64_decode(encoded)}")

    # Checksums for data integrity in ETL pipelines
    data_row = "2024-06-01,Sales,1000"
    crc = compute_crc32(data_row)
    adler = compute_adler32(data_row)
    print(f"CRC32: {crc}")
    print(f"Adler32: {adler}")

    # Troubleshooting tips:
    # - Ensure input types are correct (bytes vs str)
    # - Use .encode('utf-8') for string to bytes conversion
    # - Use .decode('ascii') for bytes to string conversion
