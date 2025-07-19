import fnmatch
from pathlib import Path
from typing import List

"""
Python's built-in `fnmatch` module is useful for pattern-based filename matching when working with file systems, ETL pipelines, and data ingestion.

Functions:
    filter_files: Filter a list of filenames using Unix shell-style wildcards.
    match_file: Check if a single filename matches a pattern.
    filter_files_case_insensitive: Case-insensitive filtering of filenames.
"""


def filter_files(filenames: List[str], pattern: str) -> List[str]:
    """
    Filter a list of filenames using a Unix shell-style wildcard pattern.

    Args:
        filenames (List[str]): List of filenames to filter.
        pattern (str): Pattern to match (e.g., '*.csv', 'data_2024-*.xlsx').

    Returns:
        List[str]: Filenames matching the pattern.

    Example:
        >>> filter_files(['sales.csv', 'data_2024-01.xlsx', 'notes.txt'], '*.csv')
        ['sales.csv']
    """
    return fnmatch.filter(filenames, pattern)


def match_file(filename: str, pattern: str) -> bool:
    """
    Check if a single filename matches a given pattern.

    Args:
        filename (str): Filename to check.
        pattern (str): Pattern to match.

    Returns:
        bool: True if filename matches pattern, False otherwise.

    Example:
        >>> match_file('report_final.xlsx', '*.xlsx')
        True
    """
    return fnmatch.fnmatch(filename, pattern)


def filter_files_case_insensitive(filenames: List[str], pattern: str) -> List[str]:
    """
    Case-insensitive filtering of filenames using fnmatchcase.

    Args:
        filenames (List[str]): List of filenames.
        pattern (str): Pattern to match.

    Returns:
        List[str]: Filenames matching the pattern, case-insensitive.

    Example:
        >>> filter_files_case_insensitive(['SALES.CSV', 'sales.csv'], '*.csv')
        ['SALES.CSV', 'sales.csv']
    """
    return [f for f in filenames if fnmatch.fnmatchcase(f.lower(), pattern.lower())]


def get_matching_files_in_directory(directory: str, pattern: str) -> List[str]:
    """
    List files in a directory matching a pattern.

    Args:
        directory (str): Path to directory.
        pattern (str): Pattern to match.

    Returns:
        List[str]: Filenames in directory matching the pattern.

    Example:
        >>> get_matching_files_in_directory('/data', '*.csv')
        ['sales.csv', 'inventory.csv']
    """
    try:
        files = [f.name for f in Path(directory).iterdir() if f.is_file()]
        return fnmatch.filter(files, pattern)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return []


if __name__ == "__main__":
    files = [
        "sales_2024-06.csv",
        "sales_2024-05.csv",
        "notes.txt",
        "inventory_2024-06.xlsx",
        "report_final.xlsx",
        "README.md",
    ]

    print("CSV files:", filter_files(files, "*.csv"))
    print("Files starting with 'sales':", filter_files(files, "sales*"))
    print(
        "Is 'report_final.xlsx' an Excel file?",
        match_file("report_final.xlsx", "*.xlsx"),
    )
    print(
        "Case-insensitive match for '*.CSV':",
        filter_files_case_insensitive(files, "*.CSV"),
    )

    # Directory listing example (update path as needed)
    print("TXT files in /data:", get_matching_files_in_directory("./data/raw", "*.txt"))
