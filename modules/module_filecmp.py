import filecmp
from typing import List, Dict

"""
Python's built-in `filecmp` module is useful for comparing files and directories, automating data validation, auditing file changes, or ensuring data pipeline consistency.
"""


def compare_two_files(file1: str, file2: str) -> bool:
    """
    Compare two files for equality.

    Args:
        file1 (str): Path to the first file.
        file2 (str): Path to the second file.

    Returns:
        bool: True if files are identical, False otherwise.

    Example:
        >>> compare_two_files('data1.csv', 'data2.csv')
        False
    """
    # shallow=True (default) compares os.stat() info first for speed.
    # Set shallow=False to force byte-by-byte comparison.
    return filecmp.cmp(file1, file2, shallow=False)


def compare_file_lists(file_list1: List[str], file_list2: List[str], dir1: str, dir2: str) -> List[str]:
    """
    Compare lists of files in two directories and return the list of files that differ.

    Args:
        file_list1 (List[str]): List of filenames in dir1.
        file_list2 (List[str]): List of filenames in dir2.
        dir1 (str): Path to the first directory.
        dir2 (str): Path to the second directory.

    Returns:
        List[str]: List of filenames that differ.

    Example:
        >>> compare_file_lists(['a.csv'], ['a.csv'], 'dirA', 'dirB')
        []
    """
    # Only compare files present in both lists
    common_files = list(set(file_list1) & set(file_list2))
    return filecmp.cmpfiles(dir1, dir2, common_files, shallow=False)[1]  # [1] is the list of diffs


def compare_directories(dir1: str, dir2: str) -> Dict[str, List[str]]:
    """
    Recursively compare two directories.

    Args:
        dir1 (str): Path to the first directory.
        dir2 (str): Path to the second directory.

    Returns:
        Dict[str, List[str]]: Dictionary with keys:
            - 'common_files': files present and identical in both
            - 'diff_files': files present in both but differ
            - 'left_only': files only in dir1
            - 'right_only': files only in dir2
            - 'funny_files': files that could not be compared

    Example:
        >>> compare_directories('dirA', 'dirB')
        {'common_files': [...], 'diff_files': [...], ...}
    """
    dcmp = filecmp.dircmp(dir1, dir2)
    result = {
        "common_files": dcmp.same_files,
        "diff_files": dcmp.diff_files,
        "left_only": dcmp.left_only,
        "right_only": dcmp.right_only,
        "funny_files": dcmp.funny_files,
    }
    return result


def print_dir_comparison(dir1: str, dir2: str) -> None:
    """
    Print a human-readable comparison of two directories.

    Args:
        dir1 (str): Path to the first directory.
        dir2 (str): Path to the second directory.

    Example:
        >>> print_dir_comparison('dirA', 'dirB')
    """
    dcmp = filecmp.dircmp(dir1, dir2)
    dcmp.report_full_closure()  # Recursively prints comparison


if __name__ == "__main__":
    # Compare two files
    print("Are files identical?", compare_two_files("sample1.csv", "sample2.csv"))

    # Compare two directories
    comparison = compare_directories("data_dir_A", "data_dir_B")
    print("Directory comparison summary:", comparison)

    # Print full directory comparison report
    print_dir_comparison("data_dir_A", "data_dir_B")

"""
TROUBLESHOOTING TIPS:
- Ensure file paths are correct and accessible.
- Use shallow=False for strict byte-by-byte comparison.
- For large directories, consider filtering file lists to relevant files.
- Use dircmp.report() for a quick summary, or report_full_closure() for recursive details.

SCALABILITY:
- Integrate these functions into ETL/data pipeline validation scripts.
- Use in CI/CD pipelines to detect unexpected file changes.
- Automate data quality checks between staging and production datasets.
"""
