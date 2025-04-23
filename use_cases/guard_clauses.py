from typing import List, Dict, Optional
import random

"""
Guard clauses are used to handle edge cases  or invalid inputs early in a function, improving readability and reducing nested code. These examples 
are tailored for business intelligence developers/analysts working with data processing tasks.
"""


def calculate_average_sales(sales_data: List[float]) -> Optional[float]:
    """
    Calculate the average sales from a list of sales data.

    Guard clauses are used to handle edge cases such as empty lists or invalid data.

    Args:
        sales_data (List[float]): A list of sales figures.

    Returns:
        Optional[float]: The average sales value, or None if the input is invalid.
    """
    # Guard clause: Check if the input list is empty
    if not sales_data:
        print("Error: Sales data is empty.")
        return None

    # Guard clause: Check if all elements in the list are non-negative numbers
    if not all(isinstance(sale, (int, float)) and sale >= 0 for sale in sales_data):
        print("Error: Sales data contains invalid or negative values.")
        return None

    return sum(sales_data) / len(sales_data)


def filter_valid_records(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Filter out invalid records from a list of dictionaries based on required fields.

    Args:
        records (List[Dict[str, str]]): A list of dictionaries representing data records.

    Returns:
        List[Dict[str, str]]: A list of valid records.
    """
    required_fields = {"id", "name", "email"}

    def is_valid(record: Dict[str, str]) -> bool:
        # Guard clause: Check if all required fields are present
        if not required_fields.issubset(record.keys()):
            return False
        # Guard clause: Check if email contains '@'
        if "@" not in record.get("email", ""):
            return False
        return True

    # Filter records using the guard clause logic
    return [record for record in records if is_valid(record)]


def generate_report(data: List[Dict[str, float]]) -> None:
    """
    Generate a report from a list of data dictionaries.

    Args:
        data (List[Dict[str, float]]): A list of dictionaries containing report data.

    Returns:
        None
    """
    # Guard clause: Check if data is empty
    if not data:
        print("Error: No data available to generate the report.")
        return

    # Guard clause: Check if all dictionaries have the same keys
    keys = data[0].keys()
    if not all(d.keys() == keys for d in data):
        print("Error: Inconsistent data structure.")
        return

    # Main logic
    print("\nReport:")
    for record in data:
        print(record)


if __name__ == "__main__":
    # Calculate average sales
    sales = [random.uniform(100, 500) for _ in range(5)]
    print("\nAverage Sales:", round(calculate_average_sales(sales), 2))

    # Filter valid records
    records = [
        {"id": "1", "name": "Alex", "email": "alex@example.com"},
        {"id": "2", "name": "Blake", "email": "blakeexample.com"},  # Invalid
        {"id": "3", "name": "Chris"},  # Missing
    ]
    print("\nValid Records:", filter_valid_records(records))

    # Generate a report
    report_data = [
        {"product": "A", "sales": round(random.uniform(100, 500), 2)},
        {"product": "B", "sales": round(random.uniform(100, 500), 2)},
    ]
    generate_report(report_data)
