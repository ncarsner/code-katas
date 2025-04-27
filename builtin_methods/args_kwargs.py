import argparse
from typing import Any, Dict, List
import random

"""Additional examples in /modules/module_argparse.py"""


def process_data(*args: str, **kwargs: Any) -> None:
    """
    Processes data based on positional and keyword arguments.

    Args:
        *args: Positional arguments representing data sources (e.g., file paths).
        **kwargs: Keyword arguments for additional options (e.g., filters, output format).

    Example:
        process_data("data1.csv", "data2.csv", filter="status:active", output="json")
    """
    print("Positional arguments (data sources):", args)
    print("Keyword arguments (options):", kwargs)

    # Example: Simulate processing data
    for source in args:
        print(f"Processing data from {source}...")

    if "filter" in kwargs:
        print(f"Applying filter: {kwargs['filter']}")

    if "output" in kwargs:
        print(f"Output format set to: {kwargs['output']}")


def example_with_dict(data: Dict[str, Any]) -> None:
    """
    Example function that demonstrates usage of a dictionary.

    Args:
        data: A dictionary containing key-value pairs to process.

    Example:
        example_with_dict({"name": "Alex", "age": 28, "active": True})
    """
    print("Processing dictionary data:")
    for key, value in data.items():
        print(f"{key}: {value}")


def example_with_list(items: List[Any]) -> None:
    """
    Example function that demonstrates usage of a list.

    Args:
        items: A list of items to process.

    Example:
        example_with_list(["apple", "banana", "cherry"])
    """
    print("Processing list data:")
    for item in items:
        print(f"Item: {item}")


def main():
    """
    Main function to parse command-line arguments and call process_data.
    """
    parser = argparse.ArgumentParser(
        description="A command-line tool for processing data with flexible options."
    )

    # Positional arguments for data sources
    parser.add_argument(
        "sources",
        metavar="SOURCE",
        type=str,
        nargs="+",
        help="One or more data sources (e.g., file paths).",
    )

    # Optional keyword arguments
    parser.add_argument(
        "--filter",
        type=str,
        help="Filter to apply to the data (e.g., 'status:active').",
    )
    parser.add_argument(
        "--output",
        type=str,
        choices=["json", "csv", "xml"],
        default="json",
        help="Output format for the processed data (default: json).",
    )

    args = parser.parse_args()

    # Pass parsed arguments to process_data
    process_data(*args.sources, filter=args.filter, output=args.output)

    # Usage of example_with_dict
    example_dict = {
        "report_name": "Monthly Sales",
        "created_by": "Analyst1",
        "status": "Completed",
        "rows_processed": random.randint(1, 100) * 1000,
    }
    example_with_dict(example_dict)

    # Usage of example_with_list
    example_list = ["sales_data.csv", "customer_data.csv", "inventory_data.csv"]
    example_with_list(example_list)


if __name__ == "__main__":
    main()
