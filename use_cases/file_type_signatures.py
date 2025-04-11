import os
from typing import Optional


def get_file_magic_number(file_path: str, num_bytes: int = 4) -> Optional[bytes]:
    """
    Reads the first few bytes (magic number) of a file.

    Args:
        file_path (str): Path to the file.
        num_bytes (int): Number of bytes to read for the magic number.

    Returns:
        Optional[bytes]: The magic number bytes, or None if the file cannot be read.
    """
    try:
        with open(file_path, "rb") as file:
            return file.read(num_bytes)
    except (FileNotFoundError, IOError):
        return None


def is_png(file_path: str) -> bool:
    """
    Checks if a file is a PNG image by its magic number.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a PNG, False otherwise.
    """
    png_magic_number = b"\x89PNG"
    magic_number = get_file_magic_number(file_path, len(png_magic_number))
    return magic_number == png_magic_number


def is_jpeg(file_path: str) -> bool:
    """
    Checks if a file is a JPEG image by its magic number.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a JPEG, False otherwise.
    """
    jpeg_magic_numbers = [b"\xff\xd8\xff\xe0", b"\xff\xd8\xff\xe1", b"\xff\xd8\xff\xe8"]
    magic_number = get_file_magic_number(file_path, 4)
    return magic_number in jpeg_magic_numbers


def is_gif(file_path: str) -> bool:
    """
    Checks if a file is a GIF image by its magic number.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a GIF, False otherwise.
    """
    gif_magic_numbers = [b"GIF87a", b"GIF89a"]
    magic_number = get_file_magic_number(file_path, 6)
    return magic_number in gif_magic_numbers


def is_pdf(file_path: str) -> bool:
    """
    Checks if a file is a PDF document by its magic number.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a PDF, False otherwise.
    """
    pdf_magic_number = b"%PDF"
    magic_number = get_file_magic_number(file_path, len(pdf_magic_number))
    return magic_number == pdf_magic_number


def is_excel(file_path: str) -> bool:
    """
    Checks if a file is an Excel document by its magic number and specific file markers.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is an Excel document, False otherwise.
    """
    excel_magic_number = b"\x50\x4b\x03\x04"  # XLSX files (ZIP-based format)
    magic_number = get_file_magic_number(file_path, 4)
    if magic_number == excel_magic_number:
        try:
            with open(file_path, "rb") as file:
                content = file.read()
                return b"[Content_Types].xml" in content and b"xl/" in content
        except IOError:
            return False
    return False


def is_text(file_path: str) -> bool:
    """
    Checks if a file is a plain text file by attempting to read its content.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a plain text file, False otherwise.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            file.read(1024)  # Read a small portion to check if it's text
        return True
    except (UnicodeDecodeError, IOError):
        return False


def is_word(file_path: str) -> bool:
    """
    Checks if a file is a Word document by its magic number and specific file markers.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a Word document, False otherwise.
    """
    word_magic_number = b"\x50\x4b\x03\x04"  # DOCX files (ZIP-based format)
    magic_number = get_file_magic_number(file_path, 4)
    if magic_number == word_magic_number:
        try:
            with open(file_path, "rb") as file:
                content = file.read()
                return b"[Content_Types].xml" in content and b"word/" in content
        except IOError:
            return False
    return False


def is_zip(file_path: str) -> bool:
    """
    Checks if a file is a ZIP archive by its magic number.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if the file is a ZIP archive, False otherwise.
    """
    zip_magic_number = b"PK\x03\x04"
    magic_number = get_file_magic_number(file_path, len(zip_magic_number))
    return magic_number == zip_magic_number


def identify_file_type(file_path: str) -> str:
    """
    Identifies the type of a file based on its magic number.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: The identified file type, or 'Unknown' if the type cannot be determined.
    """
    if is_png(file_path):
        return "PNG Image"
    elif is_jpeg(file_path):
        return "JPEG Image"
    elif is_gif(file_path):
        return "GIF Image"
    elif is_word(file_path):
        return "Word Document"
    elif is_excel(file_path):
        return "Excel Document"
    elif is_text(file_path):
        return "Text File"
    elif is_pdf(file_path):
        return "PDF Document"
    elif is_zip(file_path):
        return "ZIP Archive"
    else:
        return "Unknown"


if __name__ == "__main__":
    test_files = [
        "data/raw/test_files/bird.png",
        "data/raw/test_files/bird.jpg",
        "data/raw/test_files/bird.jpeg",
        "data/raw/test_files/bird.gif",
        "data/raw/test_files/example.xlsx",
        "data/raw/test_files/example.docx",
        "example.pdf",
        "data/raw/test_files/example.zip",
        "example_lorem.txt",
    ]

    for file in test_files:
        if os.path.exists(file):
            print(f"{file}: {identify_file_type(file)}")
        else:
            print(f"{file}: File not found.")
