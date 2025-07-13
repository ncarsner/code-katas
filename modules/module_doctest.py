from typing import List, Dict, Any
import doctest

"""
Practical usage of Python's built-in doctest module includes data cleaning, aggregation, and transformation functions.

To run doctests:
    python -m doctest -v module_doctest.py

For more info: https://docs.python.org/3/library/doctest.html
"""


def clean_currency(value: str) -> float:
    """
    Cleans a currency string and converts it to a float.

    Args:
        value (str): Currency string, e.g. "$1,234.56"

    Returns:
        float: Numeric value

    Example:
        >>> clean_currency("$1,234.56")
        1234.56
        >>> clean_currency("€2.500,00".replace('.', '').replace(',', '.'))
        2500.0
        >>> clean_currency("1000")
        1000.0
        >>> clean_currency("$-500.75")
        -500.75
    """
    cleaned = value.replace("$", "").replace(",", "").replace("€", "")
    return float(cleaned)


def aggregate_sales(sales: List[Dict[str, Any]], key: str = "amount") -> float:
    """
    Aggregates sales amounts from a list of sales records.

    Args:
        sales (List[Dict[str, Any]]): List of sales records.
        key (str): The key in the dict to sum.

    Returns:
        float: Total sales amount.

    Example:
        >>> sales = [{'amount': 100.0}, {'amount': 250.5}, {'amount': 149.5}]
        >>> aggregate_sales(sales)
        500.0
        >>> aggregate_sales([], key="amount")
        0.0
    """
    return sum(float(sale.get(key, 0)) for sale in sales)


def normalize_names(names: List[str]) -> List[str]:
    """
    Normalizes a list of names to title case and strips whitespace.

    Args:
        names (List[str]): List of names.

    Returns:
        List[str]: Normalized names.

    Example:
        >>> normalize_names([' alice ', 'BOB', 'eVa'])
        ['Alice', 'Bob', 'Eva']
        >>> normalize_names([])
        []
    """
    return [name.strip().title() for name in names]


if __name__ == "__main__":
    # Run all doctests in this module
    doctest.testmod()
    print("Doctests completed. If no output above, all tests passed.")

"""
TROUBLESHOOTING DOCTESTS:
- Ensure your docstring examples are correct and match actual output.
- Use 'python -m doctest -v module_doctest.py' for verbose output.
- If a test fails, doctest will show the expected and actual output.
- For complex outputs, use '...'(ellipsis) to match partial output.
- For more advanced usage, see the doctest documentation.
"""
