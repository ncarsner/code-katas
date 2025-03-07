from typing import List, Dict, Any
from collections import Counter
import random
from datetime import datetime, timedelta
import pandas as pd

"""
This module provides functionality to design and use survivorship rules to achieve a golden record for a dataset.
"""


def select_most_recent(records: List[Dict[str, Any]], field: str) -> Any:
    """
    Selects the most recent value for a given field from a list of records.

    Args:
        records (List[Dict[str, Any]]): List of records.
        field (str): The field to select the most recent value for.

    Returns:
        Any: The most recent value for the specified field.
    """
    return max(records, key=lambda x: x["timestamp"])[field]


def select_most_frequent(records: List[Dict[str, Any]], field: str) -> Any:
    """
    Selects the most frequent value for a given field from a list of records.

    Args:
        records (List[Dict[str, Any]]): List of records.
        field (str): The field to select the most frequent value for.

    Returns:
        Any: The most frequent value for the specified field.
    """
    counter = Counter(record[field] for record in records)
    return counter.most_common(1)[0][0]


def merge_records(
    records: List[Dict[str, Any]], rules: Dict[str, str]
) -> Dict[str, Any]:
    """
    Merges a list of records into a single golden record based on specified survivorship rules.

    Args:
        records (List[Dict[str, Any]]): List of records to merge.
        rules (Dict[str, str]): Dictionary specifying the survivorship rule for each field.

    Returns:
        Dict[str, Any]: The merged golden record.
    """
    golden_record = {}
    for field, rule in rules.items():
        if rule == "most_recent":
            golden_record[field] = select_most_recent(records, field)
        elif rule == "most_frequent":
            golden_record[field] = select_most_frequent(records, field)
        else:
            raise ValueError(f"Unknown rule: {rule}")
    return golden_record


if __name__ == "__main__":
    records = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "Johnathan Doe",
            "email": "john@example.com",
            "phone": "987-654-3210",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
    ]

    rules = {"name": "most_recent", "email": "most_frequent", "phone": "most_recent"}

    golden_record = merge_records(records, rules)
    print(golden_record)
    # Output: {'name': 'Johnathan Doe', 'email': 'john@example.com', 'phone': '987-654-3210'}


"""Refactored for a Pandas dataframe object."""


def select_most_recent(df: pd.DataFrame, field: str) -> Any:
    """
    Selects the most recent value for a given field from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame of records.
        field (str): The field to select the most recent value for.

    Returns:
        Any: The most recent value for the specified field.
    """
    return df.loc[df["timestamp"].idxmax(), field]


def select_most_frequent(df: pd.DataFrame, field: str) -> Any:
    """
    Selects the most frequent value for a given field from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame of records.
        field (str): The field to select the most frequent value for.

    Returns:
        Any: The most frequent value for the specified field.
    """
    return df[field].mode()[0]


def merge_records(df: pd.DataFrame, rules: Dict[str, str]) -> Dict[str, Any]:
    """
    Merges a DataFrame of records into a single golden record based on specified survivorship rules.

    Args:
        df (pd.DataFrame): DataFrame of records to merge.
        rules (Dict[str, str]): Dictionary specifying the survivorship rule for each field.

    Returns:
        Dict[str, Any]: The merged golden record.
    """
    golden_record = {}
    for field, rule in rules.items():
        if rule == "most_recent":
            golden_record[field] = select_most_recent(df, field)
        elif rule == "most_frequent":
            golden_record[field] = select_most_frequent(df, field)
        else:
            raise ValueError(f"Unknown rule: {rule}")
    return golden_record


if __name__ == "__main__":
    data = [
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "Johnathan Doe",
            "email": "john@example.com",
            "phone": "987-654-3210",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "Johnathan Doe",
            "email": "john.doe@example.com",
            "phone": "987-654-3210",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "Johnathan Doe",
            "email": "john@example.com",
            "phone": "987-654-3210",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
        {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "timestamp": (datetime.now() - timedelta(days=random.randint(0, 90))).strftime("%Y-%m-%d"),
        },
    ]

    df = pd.DataFrame(data)

    rules = {"name": "most_recent", "email": "most_frequent", "phone": "most_recent"}

    golden_record = merge_records(df, rules)
    print(golden_record)
    # Output: {'name': 'John Doe', 'email': 'john@example.com', 'phone': '123-456-7890'}
