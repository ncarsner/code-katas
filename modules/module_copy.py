import copy
from typing import List, Dict, Any

"""
Demonstrates shallow vs. deep copy, and provides examples relevant to data manipulation and reporting tasks.
"""


def shallow_copy(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Returns a shallow copy of a list of dictionaries.
    Useful when you want to duplicate the outer list, but not the inner dictionaries.
    Changes to inner dictionaries will affect both lists.

    Args:
        data: List of dictionaries (e.g., rows from a data extract).

    Returns:
        Shallow copy of the input list.
    """
    return copy.copy(data)


def deep_copy(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Returns a deep copy of a list of dictionaries.
    Useful when you want to duplicate both the list and all nested objects.
    Changes to the copy will not affect the original.

    Args:
        data: List of dictionaries (e.g., rows from a data extract).

    Returns:
        Deep copy of the input list.
    """
    return copy.deepcopy(data)


def demonstrate_copy():
    """
    Demonstrates the difference between shallow and deep copy in a BI context.
    """
    # List of sales records (each record is a dictionary)
    sales_data = [
        {"region": "North", "sales": 1000, "products": ["A", "B"]},
        {"region": "South", "sales": 1500, "products": ["C"]},
    ]

    # Shallow copy
    sales_shallow = shallow_copy(sales_data)
    sales_shallow[0]["sales"] = 2000  # Only changes the copy
    sales_shallow[0]["products"].append("D")  # Changes both (shared reference)

    # Deep copy
    sales_deep = deep_copy(sales_data)
    sales_deep[1]["sales"] = 3000  # Only changes the deep copy
    sales_deep[1]["products"].append("E")  # Only changes the deep copy

    print("Original sales_data:", sales_data)
    print("Shallow copy:", sales_shallow)
    print("Deep copy:", sales_deep)


if __name__ == "__main__":
    demonstrate_copy()

"""
TROUBLESHOOTING & EFFICIENCY TIPS:
- Use shallow copy (`copy.copy`) when you only need to duplicate the outer container.
- Use deep copy (`copy.deepcopy`) when nested objects must be fully independent.
- Deep copies can be expensive for large or complex data structures; use only when necessary.
- For pandas DataFrames, use `df.copy()` instead of the copy module.
"""
