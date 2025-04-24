import tempfile
import os
from typing import List
import shutil

"""
This script demonstrates practical examples of using the `tempfile` module in Python.
The `tempfile` module is useful for creating temporary files and directories, which are
automatically cleaned up after use. These examples are tailored for business intelligence
developers/analysts who may need temporary storage for intermediate data processing tasks.
"""


def create_temp_file_with_data(data: str) -> str:
    """
    Creates a temporary file, writes data to it, and returns the file path.

    Args:
        data (str): The data to write into the temporary file.

    Returns:
        str: The path to the temporary file.

    Example:
        temp_file_path = create_temp_file_with_data("Sample data")
        print(f"Temporary file created at: {temp_file_path}")
    """
    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", suffix=".txt"
    ) as temp_file:
        temp_file.write(data)
        temp_file_path = temp_file.name
    return temp_file_path


def create_temp_directory_with_files(file_data: List[str]) -> str:
    """
    Creates a temporary directory and populates it with files containing the provided data.

    Args:
        file_data (List[str]): A list of strings, where each string is written to a separate file.

    Returns:
        str: The path to the temporary directory.

    Example:
        temp_dir_path = create_temp_directory_with_files(["File 1 data", "File 2 data"])
        print(f"Temporary directory created at: {temp_dir_path}")
    """
    temp_dir = tempfile.TemporaryDirectory()
    for i, data in enumerate(file_data):
        file_path = os.path.join(temp_dir.name, f"file_{i + 1}.txt")
        with open(file_path, "w") as temp_file:
            temp_file.write(data)
    return temp_dir.name


def use_temp_file_for_large_data_processing(data: List[str]) -> None:
    """
    Demonstrates using a temporary file for processing large datasets.

    Args:
        data (List[str]): A list of strings representing large data to process.

    Example:
        use_temp_file_for_large_data_processing(["Row 1", "Row 2", "Row 3"])
    """
    with tempfile.TemporaryFile(mode="w+t") as temp_file:
        # Write data to the temporary file
        for row in data:
            temp_file.write(row + "\n")

        # Reset file pointer to the beginning for reading
        temp_file.seek(0)

        # Process the data
        print("Processing data from temporary file:")
        for line in temp_file:
            print(line.strip())


if __name__ == "__main__":
    # Create a temporary file with data
    temp_file_path = create_temp_file_with_data("This is a sample temporary file.")
    print(f"Temporary file created at: {temp_file_path}")
    # Clean up the file manually
    os.remove(temp_file_path)

    # Create a temporary directory with multiple files
    temp_dir_path = create_temp_directory_with_files(
        ["Data for file 1", "Data for file 2"]
    )
    print(f"Temporary directory created at: {temp_dir_path}")
    # List files in the directory
    print("Files in temporary directory:", os.listdir(temp_dir_path))
    # Clean up the directory manually
    shutil.rmtree(temp_dir_path)

    # Use a temporary file for large data processing
    use_temp_file_for_large_data_processing(["Row 1", "Row 2", "Row 3"])
