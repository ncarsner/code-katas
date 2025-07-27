import sys
from typing import List, Any


def print_python_version() -> None:
    """
    Prints the current Python version.
    Useful for ensuring compatibility in BI scripts.
    """
    print(f"Python version: {sys.version}")


def add_custom_module_path(path: str) -> None:
    """
    Adds a custom path to sys.path for module imports.
    Useful when BI scripts rely on shared code in non-standard locations.

    Args:
        path (str): The directory path to add.
    """
    if path not in sys.path:
        sys.path.append(path)
        print(f"Added '{path}' to sys.path.")
    else:
        print(f"'{path}' already in sys.path.")


def get_command_line_args() -> List[str]:
    """
    Returns the list of command-line arguments passed to the script.
    Useful for parameterizing BI scripts.

    Returns:
        List[str]: List of arguments.
    """
    return sys.argv[1:]  # Exclude the script name


def handle_large_output(data: Any) -> None:
    """
    Prints large data to stdout, ensuring encoding is handled.
    Useful for exporting BI results to other systems.

    Args:
        data (Any): Data to print.
    """
    # sys.stdout is a file-like object; can be redirected or replaced
    print(str(data), file=sys.stdout, flush=True)


def exit_with_status(status: int = 0) -> None:
    """
    Exits the script with a given status code.
    Useful for signaling success/failure in automated BI pipelines.

    Args:
        status (int): Exit status code (0=success, non-zero=failure).
    """
    sys.exit(status)


if __name__ == "__main__":
    print_python_version()

    ints = [-10, -7, -6, -5, -3, -2, -1, 0, 1, 5, 10, 255, 256, 257, 1000, 1001]
    for int in ints:
        print(f"Reference count for {int}: {sys.getrefcount(int)}")

    # add_custom_module_path("C:/Users/MyUser/Documents/shared_bi_code")
    args = get_command_line_args()
    print(f"Command-line arguments: {args}")

    # Simulate handling large output
    handle_large_output({"report": "sales", "total": 12345})

    # Exit with success
    exit_with_status(0)
