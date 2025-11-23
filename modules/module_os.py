import os
import time
from pathlib import Path


def list_files_in_directory(directory):
    """List all files in the given directory.

    Args:
        directory (str): The directory path.

    Returns:
        list: List of file names in the directory.
    """
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")
        return []


def create_directory(directory):
    """Create a new directory if it does not exist.

    Args:
        directory (str): The directory path to create.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created.")
    else:
        print(f"Directory {directory} already exists.")


def move_file(source, destination):
    """Move a file from source to destination.

    Args:
        source (str): Source file path.
        destination (str): Destination file path.
    """
    if os.path.exists(source):
        os.rename(source, destination)
        print(f"Moved file from {source} to {destination}.")
    else:
        print(f"Source file {source} does not exist.")


def delete_file(file_path):
    """
    Args:
        file_path (str): The file path to delete.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file {file_path}.")
    else:
        print(f"File {file_path} does not exist.")


def find_new_or_modified_files(directory, last_checked_time):
    """Find new or modified files in a directory since the last checked time.

    Args:
        directory (str): The directory path to check.
        last_checked_time (float): The last checked time in seconds since the epoch.

    Returns:
        list: List of new or modified file names.
    """
    new_or_modified_files = []
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_mod_time = os.path.getmtime(file_path)
            if file_mod_time > last_checked_time:
                new_or_modified_files.append(file_name)
    return new_or_modified_files


def normalize_path(path):
    """Normalize a path-like object to a string using os.fspath().

    This demonstrates os.fspath() which accepts path-like objects
    (str, bytes, or objects implementing __fspath__) and returns
    a string representation of the file system path.

    Args:
        path: A path-like object (str, bytes, or pathlib.Path).

    Returns:
        str: The normalized string path.
    """
    try:
        normalized = os.fspath(path)
        print(f"Normalized path: {normalized}")
        return normalized
    except TypeError as e:
        print(f"Error: {e}. The object is not a valid path-like object.")
        return None


def demonstrate_fspath():
    """Demonstrate various uses of os.fspath()."""

    # String path
    str_path = "/home/user/documents/file.txt"
    print(f"String path: {os.fspath(str_path)}")

    # pathlib.Path object
    pathlib_path = Path("/home/user/documents/file.txt")
    print(f"Pathlib path: {os.fspath(pathlib_path)}")

    # Bytes path
    bytes_path = b"/home/user/documents/file.txt"
    print(f"Bytes path: {os.fspath(bytes_path)}")

    # Using normalize_path helper
    normalize_path(Path("./relative/path/file.txt"))


if __name__ == "__main__":
    directory = "./test_directory"
    create_directory(directory)

    files = list_files_in_directory(directory)
    print("Files in directory:", files)

    move_file("./test.txt", f"{directory}/test.txt")

    delete_file(f"{directory}/test.txt")

    hours_ago = 1
    last_checked_time = time.time() - 3600 * hours_ago
    new_files = find_new_or_modified_files(directory, last_checked_time)
    print("New or modified files:", new_files)
