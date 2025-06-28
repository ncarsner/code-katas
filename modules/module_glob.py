import glob
from pathlib import Path
from typing import List

"""
THe `glob` module is useful for file pattern matching,  directory traversal, file discovery, batch processing, and data ingestion.
"""


def list_csv_files(directory: str) -> List[str]:
    """
    List all CSV files in the given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        List[str]: List of CSV file paths.

    Example:
        >>> list_csv_files('/data/reports')
        ['/data/reports/jan.csv', '/data/reports/feb.csv']
    """
    pattern = str(Path(directory) / "*.csv")
    return glob.glob(pattern)


def list_files_recursive(directory: str, extension: str) -> List[str]:
    """
    Recursively list all files with a given extension in a directory tree.

    Args:
        directory (str): Root directory to search.
        extension (str): File extension (e.g., 'xlsx', 'csv').

    Returns:
        List[str]: List of matching file paths.

    Example:
        >>> list_files_recursive('/data', 'xlsx')
        ['/data/2023/report.xlsx', '/data/archive/old.xlsx']
    """
    pattern = str(Path(directory) / "**" / f"*.{extension}")
    return glob.glob(pattern, recursive=True)


def find_latest_file(directory: str, pattern: str) -> str:
    """
    Find the most recently modified file matching a pattern.

    Args:
        directory (str): Directory to search.
        pattern (str): Glob pattern (e.g., '*.csv').

    Returns:
        str: Path to the latest file, or empty string if none found.

    Example:
        >>> find_latest_file('/exports', '*.csv')
        '/exports/data_2024-06-01.csv'
    """
    files = glob.glob(str(Path(directory) / pattern))
    if not files:
        return ""
    return max(files, key=lambda f: Path(f).stat().st_mtime)


def troubleshoot_glob_patterns():
    """
    Tips for troubleshooting glob patterns:
    - Ensure you use raw strings (r'pattern') if your pattern contains backslashes.
    - Use '**' with recursive=True for deep directory searches.
    - Test your pattern in a Python shell with print(glob.glob(pattern)).
    - Remember that glob is case-sensitive on Unix but not on Windows.
    """
    pass


if __name__ == "__main__":
    # List all CSV files in a directory
    csv_files = list_csv_files("./data")
    print("CSV files:", csv_files)

    # Recursively find all Excel files with a specific extension
    excel_files = list_files_recursive("./data", "xlsx")
    print("Excel files:", excel_files)

    # Recursively find all Excel files with specific extensions
    excel_files = []
    for ext in ["xls", "xlsx", "xlsb", "xlsm"]:
        excel_files.extend(list_files_recursive("./data", ext))
    print("Excel files:", excel_files)

    # Find all files with extensions containing 'xls' (e.g., xls, xlsx, xlsb, xlsm)
    excel_files = []
    for path in glob.glob(str(Path("./data") / "**" / "*.*"), recursive=True):
        if "xls" in Path(path).suffix.lower():
            excel_files.append(path)
    print("Excel files with 'xls' in extension:", excel_files)

    # 3. Find the latest exported CSV file
    latest_csv = find_latest_file("./exports", "*.csv")
    print("Latest CSV export:", latest_csv)
