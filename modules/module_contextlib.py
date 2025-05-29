from contextlib import contextmanager, closing, suppress, ExitStack
from typing import Iterator, Any, IO
import sqlite3
import csv
import os

"""
The contextlib module provides utilities for working with context managers, useful for resource management, error handling, and cleaner code.
"""


# Using @contextmanager to manage a database connection
@contextmanager
def db_connection(db_path: str) -> Iterator[sqlite3.Connection]:
    """
    Context manager for SQLite database connections.

    Args:
        db_path: Path to the SQLite database file.

    Yields:
        sqlite3.Connection object.

    Usage:
        with db_connection('mydb.sqlite') as conn:
            # use conn here
    """
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()


# Using closing() to ensure file-like objects are closed
def read_csv(file_path: str) -> list[dict[str, Any]]:
    """
    Reads a CSV file and returns a list of dictionaries.

    Args:
        file_path: Path to the CSV file.

    Returns:
        List of rows as dictionaries.
    """
    with closing(open(file_path, newline="", encoding="utf-8")) as f:
        reader = csv.DictReader(f)
        return list(reader)


# Using suppress() to ignore specific exceptions
def safe_remove(file_path: str) -> None:
    """
    Removes a file if it exists, suppressing FileNotFoundError.

    Args:
        file_path: Path to the file to remove.
    """
    with suppress(FileNotFoundError):
        os.remove(file_path)


# Using ExitStack for dynamic context management
def process_multiple_files(file_paths: list[str]) -> list[str]:
    """
    Reads the first line from multiple files using ExitStack.

    Args:
        file_paths: List of file paths.

    Returns:
        List of first lines from each file.
    """
    lines = []
    with ExitStack() as stack:
        files: list[IO[str]] = [
            stack.enter_context(open(fp, encoding="utf-8")) for fp in file_paths
        ]
        for f in files:
            lines.append(f.readline().strip())
    return lines


# Using nested context managers for BI ETL tasks
def etl_csv_to_db(csv_path: str, db_path: str, table: str) -> None:
    """
    Loads data from a CSV file into a SQLite database table.

    Args:
        csv_path: Path to the CSV file.
        db_path: Path to the SQLite database.
        table: Name of the target table.
    """
    with db_connection(db_path) as conn, closing(
        open(csv_path, newline="", encoding="utf-8")
    ) as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames
        if not columns:
            raise ValueError("CSV file has no columns")
        placeholders = ",".join("?" for _ in columns)
        insert_sql = (
            f"INSERT INTO {table} ({','.join(columns)}) VALUES ({placeholders})"
        )
        conn.executemany(
            insert_sql, (tuple(row[col] for col in columns) for row in reader)
        )
        conn.commit()


# Troubleshooting tips:
# - Check that resources (files, DB connections) are properly closed.
# - Use suppress() judiciously; don't hide unexpected errors.
# - Use ExitStack when the number of context managers is dynamic.
# - Use type hints and docstrings for clarity and maintainability.

if __name__ == "__main__":
    # print(read_csv('data.csv'))
    # safe_remove('old_report.csv')
    # print(process_multiple_files(['file1.txt', 'file2.txt']))
    pass
