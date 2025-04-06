from typing import List, Dict
from itertools import cycle
import random
import string
import sqlite3
import subprocess
import os


def manual_iteration(data: List[int]) -> List[int]:
    """
    Manually iterate over a list using an iterator object.

    Args:
        data (List[int]): A list of integers.

    Returns:
        List[int]: A new list with each element incremented by 1.
    """
    result = []
    iterator = iter(data)

    while True:
        try:
            item = next(iterator)
            result.append(item + 1)
        except StopIteration:
            break

    return result


def iterate_with_sentinel(file_path: str) -> List[str]:
    """
    Read lines from a file until an empty string is encountered using iter with a sentinel.

    Args:
        file_path (str): Path to the file.

    Returns:
        List[str]: A list of lines read from the file.
    """
    lines = []
    with open(file_path, "r") as file:
        for line in iter(file.readline, ""):
            lines.append(line.strip())

    return lines


def cycle_through_elements(data: List[str], n: int) -> List[str]:
    """
    Cycle through elements of a list n times using an iterator.

    Args:
        data (List[str]): A list of strings.
        n (int): Number of times to cycle through the list.

    Returns:
        List[str]: A new list with elements cycled n times.
    """
    result = []
    iterator = cycle(data)

    for _ in range(n * len(data)):
        result.append(next(iterator))

    return result


def read_log_file(file_name):
    """Automate process with iter and sentinel value"""
    with open(file_name, "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line.strip()


def get_random_number():
    """using iter with a callable and sentinel"""
    return random.randint(1, 10)


def get_git_log():
    """Simulate running a git log command and iterating through the results"""
    result = subprocess.run(["git", "log", "--oneline"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").split("\n")


def process_etl_data(etl_data: List[Dict[str, int | str]]) -> None:
    """
    Process ETL data iteratively.

    Args:
        etl_data (List[Dict[str, int | str]]): A list of dictionaries containing ETL data.

    Returns:
        None
    """
    # Get a (lazy evaluation) iterator from the data
    etl_iter = iter(etl_data)

    for record in etl_iter:
        print(f"Processing: {record['id']=}, {record['name']=}, {record['price']=}")


def iterate_database_results(db_path: str) -> None:
    """
    Iterate through database query results and print them.

    Args:
        db_path (str): Path to the SQLite database file.

    Returns:
        None
    """
    # Connect to a database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create a table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS sales_data (date text, sales integer)"""
    )

    # Insert data
    cursor.execute("INSERT INTO sales_data VALUES ('2025-04-01', 1000)")
    cursor.execute("INSERT INTO sales_data VALUES ('2025-04-02', 1500)")
    conn.commit()

    # Query the database
    cursor.execute("SELECT * FROM sales_data")
    rows = cursor.fetchall()

    # Get an iterator from the query results
    rows_iter = iter(rows)

    # Iterate through the results
    for row in rows_iter:
        print(f"Date: {row[0]}, Sales: {row[1]}")

    conn.close()


if __name__ == "__main__":
    # Manual iteration
    data = [random.randint(1, 10) for _ in range(5)]
    print(manual_iteration(data))

    # Iteration with sentinel
    file_path = "example_lorem.txt"
    print(iterate_with_sentinel(file_path))

    # Cycle through elements
    data = [random.choices(string.ascii_lowercase, k=random.randint(3, 6))]
    print(cycle_through_elements(data, random.choice([2, 3])))

    # Automate reading a log file until a specific end-of-file marker is found
    log_iter = iter(read_log_file("process.log"))

    for log_entry in log_iter:
        if log_entry == "EOF":
            break
        print(f"Log Entry: {log_entry}")

    # Using iter() with a callable and sentinel
    random_iter = iter(get_random_number, 5)

    # Process random numbers until the sentinel value (5) is encountered
    for number in random_iter:
        print(f"Random Number: {number}")

    # Get an iterator from the git log output
    git_log_iter = iter(get_git_log())

    # Process the git log entries
    for log_entry in git_log_iter:
        if log_entry:
            print(f"Git Log Entry: {log_entry}")

    # Traverse the list lazily with iter instead of loading all items into memory at once.
    etl_data = [
        {"id": 1, "name": "Shoes", "price": 100},
        {"id": 2, "name": "Jacket", "price": 150},
        {"id": 3, "name": "Shirt", "price": 200},
    ]
    process_etl_data(etl_data)

    # Iterate through database results
    db_path = "example.db"
    if os.path.exists(db_path):
        iterate_database_results(db_path)
    else:
        print(f"Error: Database file '{db_path}' does not exist.")
