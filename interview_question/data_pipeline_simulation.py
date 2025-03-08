import csv
import sqlite3
import sys


def read_data_from_file(file_path):
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data


def clean_data(data):
    cleaned_data = []
    for row in data:
        cleaned_row = {key: value.strip() for key, value in row.items()}
        cleaned_data.append(cleaned_row)
    return cleaned_data


def transform_data(data):
    transformed_data = []
    for row in data:
        transformed_row = {key: value.upper() for key, value in row.items()}
        transformed_data.append(transformed_row)
    return transformed_data


def load_data_into_database(data, db_path="data/processed/database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        column1 TEXT,
                        column2 TEXT,
                        column3 TEXT)"""
    )
    for row in data:
        cursor.execute(
            """INSERT INTO data (column1, column2, column3) VALUES (?, ?, ?)""",
            (row["column1"], row["column2"], row["column3"]),
        )
    conn.commit()
    conn.close()


def data_pipeline_simulation(file_path):
    data = read_data_from_file(file_path)
    cleaned_data = clean_data(data)
    transformed_data = transform_data(cleaned_data)
    load_data_into_database(transformed_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python data_pipeline_simulation.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    data_pipeline_simulation(file_path)
