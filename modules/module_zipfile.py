import zipfile
import os


def create_zipfile(zip_name, files):
    """Create a zip file containing the specified files.

    :param zip_name: Name of the zip file to create.
    :param files: List of file paths to include in the zip file."""
    with zipfile.ZipFile(zip_name, "w") as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    print(f"{zip_name} created successfully.")


def extract_zipfile(zip_name, extract_to):
    """Extract all contents of a zip file to the specified directory.

    :param zip_name: Name of the zip file to extract.
    :param extract_to: Directory to extract the contents to."""
    with zipfile.ZipFile(zip_name, "r") as zipf:
        zipf.extractall(extract_to)
    print(f"{zip_name} extracted to {extract_to}.")


def list_zipfile_contents(zip_name):
    """List the contents of a zip file.

    :param zip_name: Name of the zip file to list contents of."""
    with zipfile.ZipFile(zip_name, "r") as zipf:
        print(f"Contents of {zip_name}:")
        zipf.printdir()


def add_to_zipfile(zip_name, file_to_add):
    """Add a file to an existing zip file.

    :param zip_name: Name of the zip file to add a file to.
    :param file_to_add: Path of the file to add to the zip file."""
    with zipfile.ZipFile(zip_name, "a") as zipf:
        zipf.write(file_to_add, os.path.basename(file_to_add))
    print(f"{file_to_add} added to {zip_name}.")


def read_zipfile(zip_name, file_to_read):
    """Read a specific file from a zip file.

    :param zip_name: Name of the zip file to read from.
    :param file_to_read: Name of the file within the zip file to read."""
    with zipfile.ZipFile(zip_name, "r") as zipf:
        with zipf.open(file_to_read) as file:
            print(file.read().decode())


if __name__ == "__main__":
    files_to_zip = ["file1.txt", "file2.txt"]
    create_zipfile("example.zip", files_to_zip)
    list_zipfile_contents("example.zip")
    extract_zipfile("example.zip", "extracted_files")
    add_to_zipfile("example.zip", "file3.txt")
    read_zipfile("example.zip", "file1.txt")
