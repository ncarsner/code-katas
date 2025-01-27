import subprocess
from typing import List, Tuple


def run_command(command: List[str]) -> Tuple[int, str, str]:
    """
    Run a command using subprocess and return the exit code, stdout, and stderr.

    Args:
        command (List[str]): The command to run as a list of strings.

    Returns:
        Tuple[int, str, str]: A tuple containing the exit code, stdout, and stderr.
    """
    result = subprocess.run(command, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def check_ping(host: str) -> bool:
    """
    Check if a host is reachable by pinging it.

    Args:
        host (str): The host to ping.

    Returns:
        bool: True if the host is reachable, False otherwise.
    """
    command = ["ping", "-n", "1", host]
    returncode, _, _ = run_command(command)
    return returncode == 0


def list_directory(path: str) -> List[str]:
    """
    List the contents of a directory using the 'ls' command.

    Args:
        path (str): The path of the directory to list.

    Returns:
        List[str]: A list of filenames in the directory.
    """
    command = ["cmd", "/c", "dir", path]
    _, stdout, _ = run_command(command)
    return stdout.splitlines()


def get_system_info() -> str:
    """
    Get system information using the 'uname' command.

    Returns:
        str: The system information.
    """
    command = ["cmd", "/c", "systeminfo"]
    _, stdout, _ = run_command(command)
    return stdout.strip()


if __name__ == "__main__":
    # Example usage
    print("Pinging google.com:", check_ping("google.com"))
    print("Listing current directory:", list_directory("."))
    print("System information:", get_system_info())
