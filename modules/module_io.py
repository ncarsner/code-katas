import io
from typing import Iterator, List

"""
Useful for handling streams (file-like objects), large data files, in-memory data processing, and efficient file operations, this module provides functions to read large CSV files in chunks, write reports to memory, process binary data, and safely write files.
"""


def read_large_csv_in_chunks(file_path: str, chunk_size: int = 1024) -> Iterator[List[str]]:
    """
    Reads a large CSV file in chunks using io.open for memory efficiency.

    Args:
        file_path (str): Path to the CSV file.
        chunk_size (int): Number of lines per chunk.

    Yields:
        Iterator[List[str]]: Yields lists of lines (as strings) per chunk.

    Example:
        for chunk in read_large_csv_in_chunks('data.csv', 1000):
            process(chunk)
    """
    with io.open(file_path, mode="r", encoding="utf-8") as f:
        chunk = []
        for line in f:
            chunk.append(line.rstrip("\n"))
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk


def write_report_to_memory(report_lines: List[str]) -> io.StringIO:
    """
    Writes report lines to an in-memory text stream (StringIO).

    Args:
        report_lines (List[str]): List of report lines as strings.

    Returns:
        io.StringIO: In-memory text stream containing the report.

    Example:
        report_stream = write_report_to_memory(['Header', 'Row1', 'Row2'])
        print(report_stream.getvalue())
    """
    output = io.StringIO()
    for line in report_lines:
        output.write(line + "\n")
    output.seek(0)  # Reset pointer to start for reading
    return output


def process_binary_data_in_memory(binary_data: bytes) -> bytes:
    """
    Processes binary data using BytesIO, e.g., for image or Excel file manipulation.

    Args:
        binary_data (bytes): The binary data to process.

    Returns:
        bytes: The processed binary data.

    Example:
        with open('image.png', 'rb') as f:
            processed = process_binary_data_in_memory(f.read())
    """
    with io.BytesIO(binary_data) as bio:
        # Example: Read first 10 bytes, then return the rest
        _ = bio.read(10)
        remaining = bio.read()
        return remaining


def safe_file_write(file_path: str, data: str) -> None:
    """
    Safely writes data to a file using io.open with context management.

    Args:
        file_path (str): Path to the output file.
        data (str): Data to write.

    Example:
        safe_file_write('output.txt', 'Some important data')
    """
    try:
        with io.open(file_path, mode="w", encoding="utf-8") as f:
            f.write(data)
    except IOError as e:
        print(f"Error writing to {file_path}: {e}")



if __name__ == "__main__":
    # Read a large CSV in chunks
    for chunk in read_large_csv_in_chunks('large_data.csv', 5000):
        print(f"Processing chunk of {len(chunk)} lines")

    # Write a report to memory and print
    report = ["Name,Value", "Alice,100", "Bob,200"]
    report_stream = write_report_to_memory(report)
    print(report_stream.getvalue())

    # Process binary data in memory
    sample_bytes = b"0123456789abcdef"
    processed = process_binary_data_in_memory(sample_bytes)
    print(processed)

    # Safe file write
    # safe_file_write('output.txt', 'This is a test.')
