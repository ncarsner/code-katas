from pathlib import Path
from typing import List, Union
import fnmatch


def scan_and_filter_files(dir: Union[str, Path], patterns: List[str], recursive: bool = True
) -> List[Path]:
    """
    Scans a directory for files matching specific patterns using pathlib and fnmatch.

    Args:
        directory (Union[str, Path]): The directory to scan.
        patterns (List[str]): A list of glob-style patterns (e.g., '*.csv', '*.log').
        recursive (bool): Whether to scan subdirectories recursively. Defaults to True.

    Returns:
        List[Path]: A list of Path objects representing the matching files.
    """
    dir_path = Path(dir)
    if not dir_path.is_dir():
        raise ValueError(f"The provided path '{dir}' is not a valid directory.")

    # Use glob for recursive or non-recursive scanning
    glob_pattern = "**/*" if recursive else "*"
    all_files = dir_path.glob(glob_pattern)

    # Filter files based on patterns
    matching_files = [
        file
        for file in all_files
        if file.is_file()
        and any(fnmatch.fnmatch(file.name, pattern) for pattern in patterns)
    ]

    return matching_files


def main():
    # Scan for CSV and log files in a directory
    directory_to_scan = "./data"
    file_patterns = ["*.csv", "*.log"]

    try:
        matching_files = scan_and_filter_files(directory_to_scan, file_patterns)
        print(f"Found {len(matching_files)} matching files:")
        for file in matching_files:
            print(f"- {file}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
