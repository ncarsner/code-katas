import mimetypes
from typing import Tuple, List, Optional, Dict


def guess_mime_type(
    file_path: str, strict: bool = True
) -> Tuple[Optional[str], Optional[str]]:
    """
    Guess the MIME type of a file based on its filename or URL.

    :param file_path: The path to the file.
    :param strict: If True, only consider official MIME types. Defaults to True.
    :return: A tuple containing the guessed MIME type and encoding.
    """
    mime_type, encoding = mimetypes.guess_type(file_path, strict=True)
    return mime_type, encoding


def add_custom_mime_type(extension: str, mime_type: str, strict: bool = True) -> None:
    """
    Add a custom MIME type to the mimetypes module.

    :param extension: The file extension.
    :param mime_type: The MIME type to associate with the extension.
    :param strict: If True, only consider official MIME types. Defaults to True.
    """
    mimetypes.add_type(mime_type, extension, strict=True)


def init_mime_types() -> None:
    """
    Initialize the mimetypes module.
    Useful for resetting MIME types to their default values.
    """
    mimetypes.init()


def read_mime_types(file_path: str) -> None:
    """
    Read MIME types from a file and add them to the mimetypes module.

    :param file_path: The path to the file containing MIME types.
    """
    mimetypes.read_mime_types(file_path)


def list_all_mime_types(strict: bool = True) -> None:
    """
    List all known MIME types.

    :param strict: If True, only consider official MIME types. Defaults to True.
    """
    for ext, mime in mimetypes.types_map.items():
        print(f"Extension: {ext}, MIME type: {mime}")


def get_mime_type_by_extension(extension: str, strict: bool = True) -> str:
    """
    Get the MIME type for a given file extension.

    :param extension: The file extension.
    :param strict: If True, only consider official MIME types. Defaults to True.
    :return: The MIME type associated with the extension.
    """
    return mimetypes.types_map.get(extension, "Unknown MIME type")


def guess_all_extensions(mime_type: str, strict: bool = True) -> List[str]:
    """
    Guess all file extensions for a given MIME type.

    :param mime_type: The MIME type.
    :param strict: If True, only consider official MIME types. Defaults to True.
    :return: A list of file extensions associated with the MIME type.
    """
    return mimetypes.guess_all_extensions(mime_type, strict=True)


def get_inited() -> bool:
    """
    Check if the mimetypes module has been initialized.

    :return: True if initialized, False otherwise.
    """
    return mimetypes.inited


def get_knownfiles() -> List[str]:
    """
    Get the list of known files used by the mimetypes module.

    :return: A list of known files.
    """
    return mimetypes.knownfiles


def get_suffix_map() -> Dict[str, str]:
    """
    Get the suffix map used by the mimetypes module.

    :return: The suffix map.
    """
    return mimetypes.suffix_map


def get_encodings_map() -> Dict[str, str]:
    """
    Get the encodings map used by the mimetypes module.

    :return: The encodings map.
    """
    return mimetypes.encodings_map


def get_common_types() -> Dict[str, str]:
    """
    Get the common types used by the mimetypes module.

    :return: The common types.
    """
    return mimetypes.common_types


if __name__ == "__main__":
    # Sample mime.types file with content
    sample_mime_types_content = """
    # Sample MIME types
    .md text/markdown
    .json application/json
    """
    with open("mime.types", "w") as mime_file:
        mime_file.write(sample_mime_types_content)

    # Read MIME types from the created file
    read_mime_types("mime.types")

    # Guess the MIME type of a file
    file_path = "example.html"
    mime_type, encoding = guess_mime_type(file_path)
    print(f"MIME type of {file_path}: {mime_type}, Encoding: {encoding}")

    # Add a custom MIME type
    add_custom_mime_type(".md", "text/markdown")
    mime_type, encoding = guess_mime_type("example.md")
    print(f"MIME type of example.md: {mime_type}, Encoding: {encoding}")

    # Initialize the mimetypes module
    init_mime_types()

    # Guess the MIME type of a file with a custom extension from the file
    mime_type, encoding = guess_mime_type("example.json")
    print(f"MIME type, example.json: {mime_type}, Encoding: {encoding}")

    print("\nAll known MIME types:")
    list_all_mime_types()

    # Get the MIME type by extension
    extension = ".html"
    mime_type = get_mime_type_by_extension(extension)
    print(f"MIME type for {extension}: {mime_type}")

    # Guess all extensions for a given MIME type
    mime_type = "application/json"
    extensions = guess_all_extensions(mime_type)
    print(f"Extensions for {mime_type}: {extensions}")

    # Check if the mimetypes module has been initialized
    inited = get_inited()
    print(f"Mimetypes module initialized: {inited}")

    # Get the list of known files used by the mimetypes module
    known_files = get_knownfiles()
    print(f"Known files: {known_files}")

    # Get the suffix map used by the mimetypes module
    print(f"Suffix map: {get_suffix_map()=}")

    # Get the encodings map used by the mimetypes module
    print(f"{get_encodings_map()=}")

    # Get the common types used by the mimetypes module
    print(f"Common types: {get_common_types()=}")
