from typing import Any, Dict, List

"""
This script demonstrates the use of Python's `match-case` statement (introduced in Python 3.10)
to handle business intelligence use cases. The example focuses on processing different types
of data transformation tasks based on user input or system configuration.

The `match-case` construct is Python's built-in way to implement switch-case functionality.
"""


def process_data(task_type: str, data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Processes data based on the specified task type using a match-case statement.

    Args:
        task_type (str): The type of task to perform. Options include:
                         - "filter"
                         - "aggregate"
                         - "transform"
        data (List[Dict[str, Any]]): A list of dictionaries representing the data to process.

    Returns:
        List[Dict[str, Any]]: The processed data.

    Raises:
        ValueError: If the task_type is not recognized.
    """
    match task_type:
        case "filter":
            # Filter out records where the "status" field is "inactive"
            return [record for record in data if record.get("status") != "inactive"]

        case "aggregate":
            # Aggregate data by summing up the "sales" field
            total_sales = sum(record.get("sales", 0) for record in data)
            return [{"total_sales": total_sales}]

        case "transform":
            # Transform data by adding a new field "processed" with a value of True
            return [{**record, "processed": True} for record in data]

        case _:
            # Handle unknown task types
            raise ValueError(f"Unknown task type: {task_type}")


if __name__ == "__main__":
    sample_data = [
        {"id": 1, "status": "active", "sales": 100},
        {"id": 2, "status": "inactive", "sales": 200},
        {"id": 3, "status": "active", "sales": 150},
        {"id": 4, "status": "active", "sales": 300},
        # {"id": 5, "status": "inactive", "sales": 50},
        # {"id": 6, "status": "active", "sales": 400},
        # {"id": 7, "status": "inactive", "sales": 0},
        # {"id": 8, "status": "active", "sales": 250},
        # {"id": 9, "status": "inactive", "sales": 100},
        # {"id": 10, "status": "active", "sales": 500},
    ]

    # Task: Filter
    filtered_data = process_data("filter", sample_data)
    print("Filtered Data:", filtered_data)

    # Task: Aggregate
    aggregated_data = process_data("aggregate", sample_data)
    print("Aggregated Data:", aggregated_data)

    # Task: Transform
    transformed_data = process_data("transform", sample_data)
    print("Transformed Data:", transformed_data)

    # Task: Invalid
    try:
        invalid_data = process_data("invalid_task", sample_data)
    except ValueError as e:
        print("Error:", e)
