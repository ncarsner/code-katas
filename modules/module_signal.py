import signal
import time
from typing import Any, Optional

"""
Useful for handle asynchronous events, such as interrupt signals from the operating system.

Practical Example:
This script simulates a long-running data processing task that can be gracefully interrupted by the user (e.g., pressing Ctrl+C). This is useful for business intelligence developers/analysts who may need to stop a process without corrupting data or leaving resources open.

Key Features:
1. Graceful handling of SIGINT (Ctrl+C).
2. Timeout handling for long-running tasks using SIGALRM.
"""


def handle_sigint(signum: int, frame: Optional[Any]) -> None:
    """
    Signal handler for SIGINT (Ctrl+C).
    This function is called when the user interrupts the program.

    Args:
        signum (int): The signal number.
        frame (Optional[Any]): The current stack frame (not used here).
    """
    print("\nSIGINT received. Gracefully shutting down...")
    exit(0)


def handle_sigalrm(signum: int, frame: Optional[Any]) -> None:
    """
    Signal handler for SIGALRM.
    This function is called when a timeout occurs.

    Args:
        signum (int): The signal number.
        frame (Optional[Any]): The current stack frame (not used here).
    """
    print("\nTimeout occurred! Task took too long.")
    raise TimeoutError("The operation timed out.")


def long_running_task(duration: int) -> None:
    """
    Simulates a long-running task.

    Args:
        duration (int): The duration (in seconds) for the task to run.
    """
    print(f"Starting a long-running task for {duration} seconds...")
    for i in range(duration):
        print(f"Processing... {i + 1}/{duration}")
        time.sleep(1)  # Simulate work


def main() -> None:
    # Register handlers
    signal.signal(signal.SIGINT, handle_sigint)  # Handle Ctrl+C
    signal.signal(signal.SIGALRM, handle_sigalrm)  # Handle timeout

    try:
        # Set an alarm for 10 seconds (timeout)
        signal.alarm(10)

        # Simulate a long-running task
        long_running_task(15)

        # Cancel the alarm if the task completes in time
        signal.alarm(0)
        print("Task completed successfully!")

    except TimeoutError as e:
        print(f"Error: {e}")

    finally:
        print("Cleaning up resources...")


if __name__ == "__main__":
    main()
