import platform
from typing import Dict

"""
The built-in `platform` module includes functions to retrieve system information; useful for logging, troubleshooting, and ensuring compatibility.
"""


def get_system_info() -> Dict[str, str]:
    """
    Retrieves basic system information.

    Returns:
        dict: A dictionary containing system, node, release, version, machine, and processor info.

    Example:
        >>> info = get_system_info()
        >>> print(info['system'])
        'Windows'
    """
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


def get_python_info() -> Dict[str, str]:
    """
    Retrieves Python interpreter information.

    Returns:
        dict: A dictionary with Python version and implementation details.

    Example:
        >>> get_python_info()
        {'python_version': '3.11.4', 'implementation': 'CPython'}
    """
    return {
        "python_version": platform.python_version(),
        "implementation": platform.python_implementation(),
    }


def is_64bit_architecture() -> bool:
    """
    Checks if the current machine is 64-bit.

    Returns:
        bool: True if 64-bit, False otherwise.

    Example:
        >>> is_64bit_architecture()
        True
    """
    return platform.machine().endswith("64")


def get_platform_summary() -> str:
    """
    Returns a one-line summary of the platform.

    Returns:
        str: A summary string (e.g., 'Windows-10-10.0.19041-SP0').

    Example:
        >>> get_platform_summary()
        'Windows-10-10.0.19041-SP0'
    """
    return platform.platform()


def print_detailed_info() -> None:
    """
    Prints detailed platform information for troubleshooting.

    Example:
        >>> print_detailed_info()
        System: Windows
        Node: DESKTOP-1234
        ...
    """
    info = get_system_info()
    py_info = get_python_info()
    print("System:", info["system"])
    print("Node:", info["node"])
    print("Release:", info["release"])
    print("Version:", info["version"])
    print("Machine:", info["machine"])
    print("Processor:", info["processor"])
    print("Python Version:", py_info["python_version"])
    print("Python Implementation:", py_info["implementation"])
    print("Platform Summary:", get_platform_summary())
    print("Is 64-bit:", is_64bit_architecture())


if __name__ == "__main__":
    # Example usage for BI developers/analysts:
    # - Log system info before running heavy ETL jobs
    # - Troubleshoot environment-specific issues
    # - Ensure compatibility for deployment scripts

    print_detailed_info()
