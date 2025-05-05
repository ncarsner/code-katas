import shelve
from typing import Any, Dict

"""
This script demonstrates the use of Python's built-in `shelve` module for persistent storage.
The `shelve` module is a simple key-value store that can be used to store Python objects persistently.
This example is tailored for business intelligence developers/analysts who may need to store and retrieve
data such as reports, configurations, or intermediate results.

Key Features:
- Storing and retrieving data
- Updating existing records
- Deleting records
- Handling errors gracefully
"""


def store_data(file_name: str, key: str, value: Any) -> None:
    """
    Stores a key-value pair in the shelve database.

    Args:
        file_name (str): The name of the shelve database file.
        key (str): The key under which the value will be stored.
        value (Any): The value to store.

    Example:
        store_data('business_data', 'report_2023', {'sales': 1000, 'profit': 200})
    """
    with shelve.open(file_name) as db:
        db[key] = value
        print(f"Data stored under key '{key}'.")


def retrieve_data(file_name: str, key: str) -> Any:
    """
    Retrieves a value from the shelve database by its key.

    Args:
        file_name (str): The name of the shelve database file.
        key (str): The key to retrieve the value for.

    Returns:
        Any: The value associated with the key, or None if the key does not exist.

    Example:
        data = retrieve_data('business_data', 'report_2023')
    """
    with shelve.open(file_name) as db:
        if key in db:
            print(f"Data retrieved for key '{key}': {db[key]}")
            return db[key]
        else:
            print(f"Key '{key}' not found.")
            return None


def update_data(file_name: str, key: str, value: Any) -> None:
    """
    Updates an existing key-value pair in the shelve database.

    Args:
        file_name (str): The name of the shelve database file.
        key (str): The key to update the value for.
        value (Any): The new value to store.

    Example:
        update_data('business_data', 'report_2023', {'sales': 1200, 'profit': 300})
    """
    with shelve.open(file_name) as db:
        if key in db:
            db[key] = value
            print(f"Data updated for key '{key}'.")
        else:
            print(f"Key '{key}' not found. Use store_data to add it.")


def delete_data(file_name: str, key: str) -> None:
    """
    Deletes a key-value pair from the shelve database.

    Args:
        file_name (str): The name of the shelve database file.
        key (str): The key to delete.

    Example:
        delete_data('business_data', 'report_2023')
    """
    with shelve.open(file_name) as db:
        if key in db:
            del db[key]
            print(f"Key '{key}' deleted.")
        else:
            print(f"Key '{key}' not found.")


def list_keys(file_name: str) -> Dict[str, Any]:
    """
    Lists all keys in the shelve database.

    Args:
        file_name (str): The name of the shelve database file.

    Returns:
        Dict[str, Any]: A dictionary of all key-value pairs in the database.

    Example:
        keys = list_keys('business_data')
    """
    with shelve.open(file_name) as db:
        keys = list(db.keys())
        print(f"Keys in the database: {keys}")
        return keys


if __name__ == "__main__":
    db_name = "business_data"

    # Storing data
    store_data(db_name, "report_2023", {"sales": 1000, "profit": 200})
    store_data(db_name, "config", {"theme": "dark", "language": "en"})

    # Retrieving data
    retrieve_data(db_name, "report_2023")

    # Updating data
    update_data(db_name, "report_2023", {"sales": 1200, "profit": 300})

    # Listing keys
    list_keys(db_name)

    # Deleting data
    delete_data(db_name, "config")

    # Listing keys after deletion
    list_keys(db_name)
