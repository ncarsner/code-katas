from pprint import pprint, pformat, PrettyPrinter
from typing import Any, Dict

"""
Includes examples for pretty-printing nested data, controlling output width, and formatting dictionaries for reporting.
"""


def print_nested_data(data: Any) -> None:
    """
    Pretty-prints deeply nested data structures (e.g., dicts, lists).
    Useful for inspecting complex JSON responses or ETL pipeline outputs.

    Args:
        data: The data structure to print.
    """
    print("Pretty-printed nested data:")
    pprint(data, indent=2, width=80, depth=None, compact=False)


def format_for_report(data: Dict[str, Any]) -> str:
    """
    Returns a formatted string of a dictionary for inclusion in reports or logs.

    Args:
        data: The dictionary to format.

    Returns:
        str: The pretty-formatted string.
    """
    return pformat(data, indent=4, width=60, compact=True)


def custom_pretty_printer(data: Any, width: int = 60, depth: int = 2) -> None:
    """
    Uses PrettyPrinter class for advanced formatting control.
    Useful for large datasets where you want to limit output depth or width.

    Args:
        data: The data structure to print.
        width: Max characters per line.
        depth: Levels of nesting to print (None for unlimited).
    """
    printer = PrettyPrinter(indent=2, width=width, depth=depth, compact=True)
    printer.pprint(data)


if __name__ == "__main__":
    # Pretty-printing a nested dictionary (e.g., BI dashboard config)
    dashboard_config = {
        "dashboard": "Sales Overview",
        "widgets": [
            {
                "type": "bar_chart",
                "metrics": ["revenue", "profit"],
                "filters": {"region": "EMEA"},
            },
            {
                "type": "table",
                "columns": ["date", "customer", "sales"],
                "sort": ["date", "desc"],
            },
        ],
        "refresh_interval": 15,
        "theme": {"color": "blue", "font": "Arial"},
    }
    print_nested_data(dashboard_config)

    # Formatting for reports/logs
    report_str = format_for_report(dashboard_config)
    print("\nFormatted for report/log:\n", report_str)

    # Limiting output depth for large/nested data
    deeply_nested = {"level1": {"level2": {"level3": {"level4": "too deep"}}}}
    print("\nCustom PrettyPrinter (depth=2):")
    custom_pretty_printer(deeply_nested, width=50, depth=2)

    # Troubleshooting tip:
    # If pprint output is truncated, increase the 'width' or set 'depth=None'.
    # For very large data, use 'compact=True' to save space.
