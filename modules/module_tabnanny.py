import os
# import sys
import tabnanny
from typing import List, Optional

"""
Detect ambiguous indentation in Python source files. Useful when working with scripts shared across teams. Ensuring consistent indentation prevents hard-to-debug errors.

This script provides:
- A function to check a single file for indentation issues.
- A function to recursively check all `.py` files in a directory.
- Example usage and troubleshooting tips.
"""


def check_file_for_indentation_issues(filepath: str) -> Optional[str]:
    """
    Checks a single Python file for indentation issues using tabnanny.

    Args:
        filepath (str): Path to the Python file.

    Returns:
        Optional[str]: Returns None if no issues, or an error message if issues are found.
    """
    try:
        tabnanny.check(open(filepath, "r"), filepath)
        return None
    except tabnanny.NannyNag as e:
        return f"Indentation issue in {filepath}: {e}"


def check_directory_for_indentation_issues(directory: str) -> List[str]:
    """
    Recursively checks all Python files in a directory for indentation issues.

    Args:
        directory (str): Path to the directory.

    Returns:
        List[str]: List of error messages for files with indentation issues.
    """
    issues = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                result = check_file_for_indentation_issues(filepath)
                if result:
                    issues.append(result)
    return issues


if __name__ == "__main__":
    # To check a single file:
    file_to_check = "example_script.py"
    issue = check_file_for_indentation_issues(file_to_check)
    if issue:
        print(issue)
    else:
        print(f"No indentation issues found in {file_to_check}.")

    # To check all Python files in a directory (e.g. BI scripts folder):
    directory_to_check = "./"
    issues = check_directory_for_indentation_issues(directory_to_check)
    if issues:
        print("Indentation issues found:")
        for msg in issues:
            print(msg)
    else:
        print("No indentation issues found in any Python files.")

"""
Troubleshooting & Efficiency Tips:
- If you encounter a NannyNag error, open the file and check for mixed tabs and spaces.
- Configure your editor to use spaces only (PEP8 recommends 4 spaces per indent).
- Integrate this script into your CI/CD pipeline to automatically check for indentation issues.
- For large codebases, run this script regularly to maintain code quality.
"""
