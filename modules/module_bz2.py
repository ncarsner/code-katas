import bz2
from typing import Optional

"""
Python's built-in bz2 module includes functions for compressing and decompressing data and files, which are useful for efficient storage and transfer of large datasets.
"""


def compress_data(data: bytes, compresslevel: int = 9) -> bytes:
    """
    Compress bytes data using bz2.

    Args:
        data (bytes): Data to compress.
        compresslevel (int): Compression level (1-9). Higher is more compressed but slower.

    Returns:
        bytes: Compressed data.

    Example:
        compressed = compress_data(b"large csv or json data")
    """
    return bz2.compress(data, compresslevel=compresslevel)


def decompress_data(data: bytes) -> bytes:
    """
    Decompress bz2-compressed bytes data.

    Args:
        data (bytes): Compressed data.

    Returns:
        bytes: Decompressed data.

    Example:
        decompressed = decompress_data(compressed)
    """
    return bz2.decompress(data)


def compress_file(input_path: str, output_path: Optional[str] = None, compresslevel: int = 9) -> str:
    """
    Compress a file using bz2.

    Args:
        input_path (str): Path to the input file.
        output_path (Optional[str]): Path to save the compressed file. If None, appends '.bz2'.
        compresslevel (int): Compression level (1-9).

    Returns:
        str: Path to the compressed file.

    Example:
        compress_file("data.csv")
    """
    if output_path is None:
        output_path = input_path + ".bz2"
    with open(input_path, "rb") as f_in, bz2.open(
        output_path, "wb", compresslevel=compresslevel
    ) as f_out:
        for chunk in iter(lambda: f_in.read(1024 * 1024), b""):
            f_out.write(chunk)
    return output_path


def decompress_file(input_path: str, output_path: Optional[str] = None) -> str:
    """
    Decompress a bz2-compressed file.

    Args:
        input_path (str): Path to the compressed file.
        output_path (Optional[str]): Path to save the decompressed file. If None, removes '.bz2'.

    Returns:
        str: Path to the decompressed file.

    Example:
        decompress_file("data.csv.bz2")
    """
    if output_path is None:
        if input_path.endswith(".bz2"):
            output_path = input_path[:-4]
        else:
            output_path = input_path + ".decompressed"
    with bz2.open(input_path, "rb") as f_in, open(output_path, "wb") as f_out:
        for chunk in iter(lambda: f_in.read(1024 * 1024), b""):
            f_out.write(chunk)
    return output_path


def read_bz2_lines(file_path: str, encoding: str = "utf-8"):
    """
    Generator to read lines from a bz2-compressed text file.

    Args:
        file_path (str): Path to the bz2 file.
        encoding (str): Text encoding.

    Yields:
        str: Lines from the file.

    Example:
        for line in read_bz2_lines("data.csv.bz2"):
            process(line)
    """
    with bz2.open(file_path, "rt", encoding=encoding) as f:
        for line in f:
            yield line


# Troubleshooting tips:
# - If you get an OSError: Invalid data stream, the file may not be a valid bz2 file.
# - For large files, process in chunks (as above) to avoid memory issues.
# - Always close files (use 'with' statements as shown).
# - Use compresslevel=1 for faster, less compressed output; 9 for maximum compression.

if __name__ == "__main__":
    # Compress a CSV file
    compressed_path = compress_file("example_data.csv")
    print(f"Compressed file saved to: {compressed_path}")

    # Decompress it back
    decompressed_path = decompress_file(compressed_path)
    print(f"Decompressed file saved to: {decompressed_path}")

    # Read lines from a compressed CSV
    for i, line in enumerate(read_bz2_lines(compressed_path)):
        if i < 5:
            print(line.strip())
        else:
            break
