import difflib
from typing import List, Tuple
import string
import random


def calculate_similarity_ratio(string1: str, string2: str) -> float:
    """
    Calculate the similarity ratio between two strings using SequenceMatcher.

    Args:
        string1 (str): The first string to compare.
        string2 (str): The second string to compare.

    Returns:
        float: A similarity ratio between 0 and 1, where 1 means identical strings.

    Example:
        ratio = calculate_similarity_ratio("report_2022", "report_2023")
        print(ratio)  # Output: 0.916...
    """
    matcher = difflib.SequenceMatcher(None, string1, string2)
    return matcher.ratio()


def find_closest_match(query: str, options: List[str]) -> str:
    """
    Find the closest match to a query string from a list of options.

    Args:
        query (str): The string to match.
        options (List[str]): A list of strings to compare against.

    Returns:
        str: The closest matching string from the options.

    Example:
        closest = find_closest_match("sales_report", ["sales_data", "sales_report_2023", "inventory_report"])
        print(closest)  # Output: "sales_report_2023"
    """
    closest_matches = difflib.get_close_matches(query, options, n=1, cutoff=0.6)
    return closest_matches[0] if closest_matches else "No close match found"


def generate_diff_report(text1: str, text2: str) -> List[str]:
    """
    Generate a human-readable diff report between two strings.

    Args:
        text1 (str): The first text to compare.
        text2 (str): The second text to compare.

    Returns:
        List[str]: A list of strings representing the differences.

    Example:
        diff = generate_diff_report("old data", "new data")
        print("\n".join(diff))
    """
    differ = difflib.Differ()
    diff = list(differ.compare(text1.splitlines(), text2.splitlines()))
    return diff


def compare_csv_rows(row1: List[str], row2: List[str]) -> List[Tuple[int, str, str]]:
    """
    Compare two rows of data (e.g., from a CSV file) and return differences.

    Args:
        row1 (List[str]): The first row of data.
        row2 (List[str]): The second row of data.

    Returns:
        List[Tuple[int, str, str]]: A list of tuples containing the index, value from row1, and value from row2.

    Example:
        differences = compare_csv_rows(["A", "B", "C"], ["A", "X", "C"])
        print(differences)  # Output: [(1, 'B', 'X')]
    """
    differences = []
    for i, (val1, val2) in enumerate(zip(row1, row2)):
        if val1 != val2:
            differences.append((i, val1, val2))
    return differences


if __name__ == "__main__":
    # Calculate similarity ratio
    print("\nSimilarity Ratio Example:")
    ratio = calculate_similarity_ratio("report_2022", "report_2023")
    print(f"Similarity Ratio: {ratio:.1%}\n")

    # Find closest match
    print("Closest Match Example:")
    closest = find_closest_match(
        "sales_report", ["sales_data", "sales_report_2023", "inventory_report"]
    )
    print(f"Closest Match: {closest}\n")

    # Generate diff report
    print("Diff Report:")
    text1 = "Line 1: Old Data\nLine 2: Unchanged\nLine 3: Removed"
    text2 = "Line 1: New Data\nLine 2: Unchanged\nLine 3: Added"
    diff = generate_diff_report(text1, text2)
    print("\n".join(diff), "\n")

    # Compare CSV rows
    print("CSV Row Comparison Example:")
    letters = list(string.ascii_uppercase)
    random.shuffle(letters)
    csv_content_a = list(letters[:5])
    random.shuffle(letters)
    csv_content_b = list(letters[:5])
    print(f"Row 1: {csv_content_a}")
    print(f"Row 2: {csv_content_b}")
    row_diff = compare_csv_rows(csv_content_a, csv_content_b)
    # row_diff = compare_csv_rows(["A", "B", "C"], ["A", "X", "C"])
    print(f"Differences: {row_diff}")
