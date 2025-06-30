import keyword
from typing import List, Dict

"""
Useful for validating dynamically generated variable names, column names, or identifiers to avoid conflicts with Python keywords, this module provides functions to check if a name is a valid Python identifier, filter out keywords, suggest alternate names for keywords, and retrieve all Python keywords.
"""


def is_valid_identifier(name: str) -> bool:
    """
    Checks if a given string is a valid Python identifier and not a keyword.

    Args:
        name (str): The string to check.

    Returns:
        bool: True if valid identifier and not a keyword, False otherwise.

    Example:
        >>> is_valid_identifier('class')
        False
        >>> is_valid_identifier('sales_total')
        True
    """
    return name.isidentifier() and not keyword.iskeyword(name)


def filter_keywords(names: List[str]) -> List[str]:
    """
    Filters out Python keywords from a list of strings.

    Args:
        names (List[str]): List of strings to check.

    Returns:
        List[str]: List with keywords removed.

    Example:
        >>> filter_keywords(['for', 'sales', 'if', 'profit'])
        ['sales', 'profit']
    """
    return [name for name in names if not keyword.iskeyword(name)]


def suggest_alternate_names(names: List[str]) -> Dict[str, str]:
    """
    Suggests alternate names for any Python keywords in the input list.

    Args:
        names (List[str]): List of names to check.

    Returns:
        Dict[str, str]: Mapping from keyword to suggested alternate name.

    Example:
        >>> suggest_alternate_names(['class', 'def', 'total'])
        {'class': 'class_', 'def': 'def_'}
    """
    return {name: f"{name}_" for name in names if keyword.iskeyword(name)}


def get_all_keywords() -> List[str]:
    """
    Returns the list of all Python keywords for the current interpreter.

    Returns:
        List[str]: List of Python keywords.

    Example:
        >>> 'lambda' in get_all_keywords()
        True
    """
    return list(keyword.kwlist)


if __name__ == "__main__":
    # Column names from a data source
    column_names = ["class", "sales", "def", "profit", "lambda"]

    # Filter out keywords
    safe_columns = filter_keywords(column_names)
    print("Safe columns:", safe_columns)

    # Suggest alternates for keywords
    alternates = suggest_alternate_names(column_names)
    print("Suggested alternates:", alternates)

    # Validate identifiers
    for name in column_names:
        print(f"Is '{name}' a valid identifier? {is_valid_identifier(name)}")

    # List all Python keywords
    print("Python keywords:", get_all_keywords())
