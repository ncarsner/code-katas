import faulthandler
import threading
import time
from typing import Optional, IO

"""
Python's built-in `faulthandler` module for helps diagnose crashes, deadlocks, and hangs by printing tracebacks on faults/signals.

Typical use cases:
- Debugging segmentation faults in data processing scripts.
- Diagnosing deadlocks in multi-threaded ETL jobs.
- Logging tracebacks for troubleshooting production issues.
"""


def enable_fault_handler(log_file: Optional[IO] = None) -> None:
    """
    Enables faulthandler to dump tracebacks on faults/signals.
    Args:
        log_file: Optional file-like object to write tracebacks to (default: sys.stderr).
    """
    if log_file is not None:
        faulthandler.enable(file=log_file.fileno())
    else:
        faulthandler.enable()
    print("faulthandler enabled.")


def disable_fault_handler() -> None:
    """
    Disables faulthandler.
    """
    faulthandler.disable()
    print("faulthandler disabled.")


def dump_traceback(log_file: Optional[IO] = None) -> None:
    """
    Manually dumps the current traceback to the given file.
    Useful for debugging long-running data jobs.
    Args:
        log_file: Optional file-like object to write tracebacks to (default: sys.stderr).
    """
    if log_file is not None:
        faulthandler.dump_traceback(file=log_file.fileno())
    else:
        faulthandler.dump_traceback()
    print("Current traceback dumped.")


def simulate_deadlock() -> None:
    """
    Simulates a deadlock in a multi-threaded environment.
    Use faulthandler.dump_traceback_later() to help diagnose.
    """
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    def thread1():
        with lock1:
            time.sleep(1)
            with lock2:
                pass

    def thread2():
        with lock2:
            time.sleep(1)
            with lock1:
                pass

    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def schedule_traceback_dump(
    timeout: float = 5.0, repeat: bool = False, log_file: Optional[IO] = None) -> None:
    """
    Schedules a traceback dump after a timeout (in seconds).
    Useful for diagnosing hangs in ETL/data jobs.
    Args:
        timeout: Seconds before dumping traceback.
        repeat: If True, repeat dump every timeout seconds.
        log_file: Optional file-like object to write tracebacks to.
    """
    if log_file is not None:
        faulthandler.dump_traceback_later(
            timeout, repeat=repeat, file=log_file.fileno()
        )
    else:
        faulthandler.dump_traceback_later(timeout, repeat=repeat)
    print(f"Scheduled traceback dump in {timeout} seconds (repeat={repeat}).")


def cancel_scheduled_traceback_dump() -> None:
    """
    Cancels a scheduled traceback dump.
    """
    faulthandler.cancel_dump_traceback_later()
    print("Scheduled traceback dump cancelled.")


if __name__ == "__main__":
    # Enable faulthandler for all faults/signals
    enable_fault_handler()

    # Schedule a traceback dump in 3 seconds (for debugging hangs)
    schedule_traceback_dump(timeout=3.0)

    # Simulate a deadlock (traceback will be dumped after timeout)
    print("Simulating deadlock...")
    simulate_deadlock()

    # Cancel scheduled dump (if needed)
    cancel_scheduled_traceback_dump()

    # Manually dump traceback
    dump_traceback()

    # Disable faulthandler when done
    disable_fault_handler()
