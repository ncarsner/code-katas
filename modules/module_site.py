import site
from typing import List
import sys

"""
Configure the Python runtime environment, including managing site-specific paths and user site directories. Useful for managing custom libraries or ensure proper environment setup for their scripts.
"""


def list_site_packages() -> List[str]:
    """
    Lists all directories where Python looks for site-packages.
    This includes both global and user-specific directories.
    Useful for understanding where Python is loading libraries from.
    May not work in virtual environments.

    Returns:
        List[str]: A list of paths to site-packages directories.
    """
    try:
        site_packages = site.getsitepackages()
        print("Global site-packages directories:")
        for path in site_packages:
            print(f"  - {path}")
        return site_packages
    except AttributeError:
        print("getsitepackages() is not available in this environment.")
        return []


def list_user_site_packages() -> str:
    """
    Returns the path to the user-specific site-packages directory.

    Returns:
        str: The path to the user site-packages directory.
    """
    user_site = site.getusersitepackages()
    print(f"User site-packages directory: {user_site}")
    return user_site


def add_custom_path(path: str) -> None:
    """
    Adds a custom directory to Python's module search path (sys.path).
    Useful for dynamically adding custom library paths.

    Args:
        path (str): The custom directory to add to sys.path.
    """
    site.addsitedir(path)
    print(f"Added {path} to Python's module search path.")


def troubleshoot_imports() -> None:
    """
    Prints the current Python module search paths for troubleshooting import issues.
    """
    print("Current Python module search paths:")
    for path in sys.path:
        print(f"  - {path}")


if __name__ == "__main__":
    # List global site-packages directories
    list_site_packages()

    # List user-specific site-packages directory
    list_user_site_packages()

    # Add a custom path
    custom_path = "/path/to/custom/libs"  # replace with an actual path
    add_custom_path(custom_path)

    # Troubleshoot import issues by printing sys.path
    troubleshoot_imports()
