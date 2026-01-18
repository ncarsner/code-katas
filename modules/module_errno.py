import errno
import os
import socket
from typing import Optional, Tuple

"""
Demonstration of Python's errno module for error handling.

The errno module provides standard error codes and utilities for working with
system-level errors. This is particularly useful for data engineers and BI
developers working with file I/O, database connections, and system resources.

Key errno codes relevant to data engineering:
- ENOENT (2): File/directory not found
- EACCES (13): Permission denied
- EEXIST (17): File already exists
- ENOSPC (28): No space left on device
- ETIMEDOUT (60): Connection timeout
- ECONNREFUSED (61): Connection refused
"""


def safe_file_read(filepath: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Safely read a file with detailed error handling using errno.

    Args:
        filepath: Path to the file to read

    Returns:
        Tuple of (file_content, error_message)

    Example:
        >>> content, error = safe_file_read('/data/sales_2024.csv')
        >>> if error:
        ...     print(f"Error: {error}")
    """
    try:
        with open(filepath, "r") as f:
            return f.read(), None
    except OSError as e:
        if e.errno == errno.ENOENT:
            return (
                None,
                f"File not found: {filepath}. Check path or run data pipeline first.",
            )
        elif e.errno == errno.EACCES:
            return (
                None,
                f"Permission denied: {filepath}. Check file permissions (chmod).",
            )
        elif e.errno == errno.EISDIR:
            return None, f"Expected file but got directory: {filepath}"
        else:
            # Use errorcode dict to get symbolic name
            error_name = errno.errorcode.get(e.errno or 0, "UNKNOWN")
            return None, f"OS error ({error_name}): {e.strerror}"


def safe_directory_create(
    dirpath: str, exist_ok: bool = True
) -> Tuple[bool, Optional[str]]:
    """
    Create a directory with granular error handling for ETL pipelines.

    Args:
        dirpath: Path to directory to create
        exist_ok: If True, don't raise error if directory exists

    Returns:
        Tuple of (success, error_message)

    Example:
        >>> success, error = safe_directory_create('/data/output/2024')
        >>> if not success:
        ...     log_error(error)
    """
    try:
        os.makedirs(dirpath, exist_ok=exist_ok)
        return True, None
    except OSError as e:
        if e.errno == errno.EEXIST and not exist_ok:
            return False, f"Directory already exists: {dirpath}"
        elif e.errno == errno.EACCES:
            return (
                False,
                f"Permission denied creating: {dirpath}. Run with sudo or check parent directory permissions.",
            )
        elif e.errno == errno.ENOSPC:
            return (
                False,
                f"No space left on device. Cannot create: {dirpath}. Free up disk space.",
            )
        elif e.errno == errno.EROFS:
            return False, f"Read-only file system. Cannot create: {dirpath}"
        else:
            return False, f"Failed to create directory: {e.strerror} (errno: {e.errno})"


def check_database_connection(
    host: str, port: int, timeout: int = 5
) -> Tuple[bool, Optional[str]]:
    """
    Test database/service connectivity with errno-based diagnostics.

    Useful for data pipeline health checks and connection retry logic.

    Args:
        host: Database host/IP address
        port: Database port number
        timeout: Connection timeout in seconds

    Returns:
        Tuple of (is_connected, error_message)

    Example:
        >>> is_up, error = check_database_connection('postgres-prod', 5432)
        >>> if not is_up:
        ...     send_alert(f"DB down: {error}")
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        sock.connect((host, port))
        sock.close()
        return True, None
    except OSError as e:
        sock.close()
        if e.errno == errno.ECONNREFUSED:
            return (
                False,
                f"Connection refused to {host}:{port}. Service may be down or firewall blocking.",
            )
        elif e.errno == errno.ETIMEDOUT:
            return (
                False,
                f"Connection timeout to {host}:{port}. Check network or increase timeout.",
            )
        elif e.errno == errno.ENETUNREACH:
            return False, f"Network unreachable to {host}:{port}. Check routing/VPN."
        elif e.errno == errno.EHOSTUNREACH:
            return False, f"Host unreachable: {host}. Check DNS or host is up."
        else:
            error_name = errno.errorcode.get(e.errno or 0, "UNKNOWN")
            return False, f"Connection error ({error_name}): {e.strerror}"


def safe_file_write(filepath: str, content: str) -> Tuple[bool, Optional[str]]:
    """
    Write file with comprehensive error handling for data exports.

    Args:
        filepath: Destination file path
        content: Content to write

    Returns:
        Tuple of (success, error_message)

    Example:
        >>> success, error = safe_file_write('/exports/report.csv', csv_data)
        >>> if not success:
        ...     retry_with_alternative_path()
    """
    try:
        with open(filepath, "w") as f:
            f.write(content)
        return True, None
    except OSError as e:
        if e.errno == errno.ENOSPC:
            return (
                False,
                f"Disk full. Cannot write to: {filepath}. Archive old files or expand storage.",
            )
        elif e.errno == errno.EACCES:
            return False, f"Permission denied writing: {filepath}"
        elif e.errno == errno.EDQUOT:
            return False, f"Disk quota exceeded writing: {filepath}"
        elif e.errno == errno.EROFS:
            return False, f"Read-only filesystem: {filepath}"
        else:
            return False, f"Write failed: {e.strerror} (errno: {e.errno})"


def demonstrate_errno_utilities() -> None:
    """
    Demonstrate useful errno module utilities for debugging and logging.
    """
    print("=== errno Module Utilities ===\n")

    # 1. errorcode dict: Maps errno numbers to symbolic names
    print("Common error codes:")
    for code in [errno.ENOENT, errno.EACCES, errno.ENOSPC, errno.ETIMEDOUT]:
        print(f"  {code}: {errno.errorcode[code]}")

    print("\n2. Using errno in exception handling:")
    try:
        with open("/nonexistent/file.txt") as f:
            pass
    except OSError as e:
        print(
            f"  Caught errno {e.errno}: {errno.errorcode.get(e.errno or 0, 'UNKNOWN')}"
        )
        print(f"  Strerror: {e.strerror}")
        print(f"  Can check: e.errno == errno.ENOENT -> {e.errno == errno.ENOENT}")

    print("\n3. All available error codes (sample):")
    sample_codes = list(errno.errorcode.items())[:10]
    for code, name in sample_codes:
        print(f"  {name} ({code})")


if __name__ == "__main__":
    print("Testing errno module examples...\n")

    # Test file operations
    content, error = safe_file_read("/etc/hosts")
    print(f"Read /etc/hosts: {'Success' if content else f'Failed - {error}'}")

    # Test directory creation
    success, error = safe_directory_create("/tmp/test_errno_demo")
    print(f"Create directory: {'Success' if success else f'Failed - {error}'}")

    # Test database connection (localhost example)
    is_up, error = check_database_connection("localhost", 5432, timeout=2)
    print(f"DB connection test: {'Connected' if is_up else f'Failed - {error}'}")

    print("\n" + "=" * 50 + "\n")
    demonstrate_errno_utilities()
