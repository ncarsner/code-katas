import codecs
from typing import Iterator, List, Optional

"""
Useful when working with text data files in various encodings (UTF-8, UTF-16, Latin-1)
"""


def read_encoded_file(filepath: str, encoding: str = "utf-8") -> List[str]:
    """
    Reads a text file with the specified encoding and returns its lines.

    Args:
        filepath (str): Path to the file.
        encoding (str): Encoding to use (e.g., 'utf-8', 'latin-1', 'utf-16').

    Returns:
        List[str]: List of lines from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        UnicodeDecodeError: If the file cannot be decoded with the given encoding.

    Example:
        lines = read_encoded_file("data/report.csv", encoding="utf-16")
    """
    with codecs.open(filepath, "r", encoding=encoding) as f:
        return f.readlines()


def write_encoded_file(filepath: str, lines: List[str], encoding: str = "utf-8") -> None:
    """
    Writes a list of strings to a file using the specified encoding.

    Args:
        filepath (str): Path to the file.
        lines (List[str]): List of strings to write.
        encoding (str): Encoding to use.

    Example:
        write_encoded_file("output.txt", ["hello", "world"], encoding="utf-16")
    """
    with codecs.open(filepath, "w", encoding=encoding) as f:
        f.writelines(lines)


def convert_file_encoding(
    src_path: str,
    dest_path: str,
    src_encoding: str = "utf-8",
    dest_encoding: str = "utf-8",
) -> None:
    """
    Converts a file from one encoding to another.

    Args:
        src_path (str): Source file path.
        dest_path (str): Destination file path.
        src_encoding (str): Source file encoding.
        dest_encoding (str): Destination file encoding.

    Example:
        convert_file_encoding("input.csv", "output.csv", "latin-1", "utf-8")
    """
    lines = read_encoded_file(src_path, encoding=src_encoding)
    write_encoded_file(dest_path, lines, encoding=dest_encoding)


def encode_text(text: str, encoding: str = "utf-8") -> bytes:
    """
    Encodes a string into bytes using the specified encoding.

    Args:
        text (str): The text to encode.
        encoding (str): The encoding to use.

    Returns:
        bytes: The encoded bytes.

    Example:
        b = encode_text("café", encoding="latin-1")
    """
    return codecs.encode(text, encoding)


def decode_bytes(data: bytes, encoding: str = "utf-8") -> str:
    """
    Decodes bytes into a string using the specified encoding.

    Args:
        data (bytes): The bytes to decode.
        encoding (str): The encoding to use.

    Returns:
        str: The decoded string.

    Example:
        s = decode_bytes(b"caf\xe9", encoding="latin-1")
    """
    return codecs.decode(data, encoding)


def iter_decode_lines(lines: Iterator[bytes], encoding: str = "utf-8") -> Iterator[str]:
    """
    Lazily decodes an iterator of byte strings to strings.

    Args:
        lines (Iterator[bytes]): Iterator of byte strings.
        encoding (str): Encoding to use.

    Yields:
        str: Decoded lines.

    Example:
        with open("data.txt", "rb") as f:
            for line in iter_decode_lines(f, encoding="utf-16"):
                process(line)
    """
    decoder = codecs.getincrementaldecoder(encoding)()
    for line in lines:
        yield decoder.decode(line)


def detect_encoding(
    filepath: str, encodings: Optional[List[str]] = None) -> Optional[str]:
    """
    Tries to detect the encoding of a file by attempting to decode with a list of encodings.

    Args:
        filepath (str): Path to the file.
        encodings (Optional[List[str]]): List of encodings to try.

    Returns:
        Optional[str]: The detected encoding, or None if not found.

    Example:
        enc = detect_encoding("unknown.csv", ["utf-8", "utf-16", "latin-1"])
    """
    encodings = encodings or ["utf-8", "utf-16", "latin-1"]
    for enc in encodings:
        try:
            with codecs.open(filepath, "r", encoding=enc) as f:
                f.read()
            return enc
        except Exception:
            continue
    return None


if __name__ == "__main__":
    # Use Case: Read a CSV file in UTF-16 encoding and write it as UTF-8.

    # 1. Convert file encoding
    convert_file_encoding("input_utf16.csv", "output_utf8.csv", "utf-16", "utf-8")

    # 2. Detect encoding of the file
    detected = detect_encoding("unknown_encoding.csv")
    print(f"Detected encoding: {detected}")

    # 3. Encode/decode text for data processing
    b = encode_text("café", "latin-1")
    s = decode_bytes(b, "latin-1")
    print(s)
    pass
