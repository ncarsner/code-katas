from abc import ABC, abstractmethod
from typing import List, Dict
import csv


class DataProcessor(ABC):
    """
    Abstract base class for data processing tasks.
    Business Intelligence developers can extend this class to implement
    specific data processing workflows.
    """

    @abstractmethod
    def extract_data(self, source: str) -> List[Dict]:
        """
        Extract data from a given source.
        :param source: The data source (e.g., file path, database connection string).
        :return: A list of dictionaries representing the extracted data.
        """
        pass

    @abstractmethod
    def transform_data(self, data: List[Dict]) -> List[Dict]:
        """
        Transform the extracted data into a desired format.
        :param data: The raw data to be transformed.
        :return: A list of dictionaries representing the transformed data.
        """
        pass

    @abstractmethod
    def load_data(self, data: List[Dict], destination: str) -> None:
        """
        Load the transformed data into a destination.
        :param data: The transformed data to be loaded.
        :param destination: The destination (e.g., database, file path).
        """
        pass


class CSVDataProcessor(DataProcessor):
    """
    Concrete implementation of DataProcessor for handling CSV files.
    """

    def extract_data(self, source: str) -> List[Dict]:
        data = []
        try:
            with open(source, mode="r") as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: File {source} not found.")
        return data

    def transform_data(self, data: List[Dict]) -> List[Dict]:
        # Convert all string values to uppercase
        return [
            {
                key: value.upper() if isinstance(value, str) else value
                for key, value in row.items()
            }
            for row in data
        ]

    def load_data(self, data: List[Dict], destination: str) -> None:
        try:
            with open(destination, mode="w", newline="") as file:
                if data:
                    writer = csv.DictWriter(file, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
        except Exception as e:
            print(f"Error while writing to {destination}: {e}")


if __name__ == "__main__":
    processor = CSVDataProcessor()
    source_file = "input.csv"
    destination_file = "output.csv"

    # Extract data
    raw_data = processor.extract_data(source_file)
    if not raw_data:
        print("No data extracted. Exiting.")
        exit()

    # Transform data
    transformed_data = processor.transform_data(raw_data)

    # Load data
    processor.load_data(transformed_data, destination_file)
    print(f"Data processing complete. Transformed data saved to {destination_file}.")
