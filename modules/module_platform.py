import platform
from typing import Dict, Any

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


def identify_operating_system() -> Dict[str, Any]:
    """
    Identifies the operating system and provides detailed platform information.
    
    Returns:
        dict: A dictionary containing OS type, is_windows, is_macos, is_linux flags,
              and additional platform details.
    
    Example:
        >>> os_info = identify_operating_system()
        >>> print(os_info['os_type'])
        'macOS'
        >>> print(os_info['is_macos'])
        True
    """
    system = platform.system()
    
    result = {
        "os_type": system,
        "is_windows": system == "Windows",
        "is_macos": system == "Darwin",
        "is_linux": system == "Linux",
        "is_unix": system in ("Darwin", "Linux", "Unix"),
        "platform_name": platform.platform(),
        "release": platform.release(),
    }
    
    # Add OS-specific details
    if result["is_macos"]:
        result["macos_version"] = platform.mac_ver()[0]
    elif result["is_windows"]:
        result["windows_version"] = platform.win32_ver()[0]
        result["windows_edition"] = platform.win32_edition()
    elif result["is_linux"]:
        # Get Linux distribution info if available
        try:
            import distro
            result["linux_distro"] = distro.name()
            result["linux_version"] = distro.version()
        except ImportError:
            result["linux_distro"] = "Unknown (install 'distro' package for details)"
    
    return result


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

    print("=" * 60)
    print("OPERATING SYSTEM IDENTIFICATION")
    print("=" * 60)
    os_info = identify_operating_system()
    print(f"OS Type: {os_info['os_type']}")
    print(f"Is Windows: {os_info['is_windows']}")
    print(f"Is macOS: {os_info['is_macos']}")
    print(f"Is Linux: {os_info['is_linux']}")
    print(f"Platform Name: {os_info['platform_name']}")
    
    # Print OS-specific info
    if os_info['is_macos']:
        print(f"macOS Version: {os_info.get('macos_version', 'N/A')}")
    elif os_info['is_windows']:
        print(f"Windows Version: {os_info.get('windows_version', 'N/A')}")
        print(f"Windows Edition: {os_info.get('windows_edition', 'N/A')}")
    elif os_info['is_linux']:
        print(f"Linux Distro: {os_info.get('linux_distro', 'N/A')}")
    
    print("\n" + "=" * 60)
    print("DETAILED PLATFORM INFORMATION")
    print("=" * 60)
    print_detailed_info()
