import mmap
from typing import Iterator, Optional

"""
Python's `mmap` module contains functions for reading large files efficiently, searching for patterns, and updating files in-place.
"""


def read_large_file_by_line(file_path: str, encoding: str = "utf-8") -> Iterator[str]:
    """
    Efficiently reads a large text file line by line using mmap.
    Useful for processing logs, CSVs, or data extracts too large to fit in memory.

    Args:
        file_path: Path to the file to read.
        encoding: Encoding of the file (default: "utf-8").

    Yields:
        Lines as strings.

    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If the file cannot be decoded with the given encoding.
    """
    with open(file_path, "r+b") as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            for line in iter(mm.readline, b""):
                yield line.decode(encoding).rstrip('\n')


def search_pattern_in_file(file_path: str, pattern: bytes) -> Optional[int]:
    """
    Searches for a byte pattern in a file using mmap.
    Useful for finding headers, delimiters, or specific data markers.

    Args:
        file_path: Path to the file to search.
        pattern: Byte pattern to search for (e.g., b"HEADER").

    Returns:
        The byte offset where the pattern is found, or None if not found.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(file_path, "rb") as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
            pos = mm.find(pattern)
            return pos if pos != -1 else None


def update_value_in_file(file_path: str, old_value: bytes, new_value: bytes) -> bool:
    """
    Updates the first occurrence of old_value with new_value in a file using mmap.
    Useful for patching configuration files or correcting data in-place.

    Args:
        file_path: Path to the file to update.
        old_value: Byte string to replace.
        new_value: Byte string to write (must be same length as old_value).

    Returns:
        True if the value was updated, False otherwise.

    Raises:
        ValueError: If new_value and old_value are not the same length.
        FileNotFoundError: If the file does not exist.
    """
    if len(old_value) != len(new_value):
        raise ValueError("old_value and new_value must be the same length for in-place update.")

    with open(file_path, "r+b") as f:
        with mmap.mmap(f.fileno(), 0) as mm:
            pos = mm.find(old_value)
            if pos != -1:
                mm[pos:pos+len(new_value)] = new_value
                mm.flush()
                return True
            return False


# if __name__ == "__main__":
#     # Read a large CSV file line by line
#     for line in read_large_file_line_by_line("large_data.csv"):
#         print(line)
#
#     # Search for a header in a binary file
#     offset = search_pattern_in_file("data_export.bin", b"HEADER")
#     print(f"HEADER found at offset: {offset}")
#
#     # Update a value in a config file
#     updated = update_value_in_file("config.ini", b"oldval", b"newval")
#     print(f"Update successful: {updated}")

"""
Troubleshooting Tips:
- Ensure files are opened in binary mode ("rb" or "r+b") for mmap.
- For text files, decode bytes to strings using the correct encoding.
- When updating, new_value must be the same length as old_value.
- Use try/except blocks to handle FileNotFoundError or UnicodeDecodeError.
- For very large files, mmap avoids loading the entire file into memory.
"""
