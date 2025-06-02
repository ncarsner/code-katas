import contextvars
import asyncio
from typing import Any, Optional
import random

"""
Context variables are useful for managing context-local state, such as user/session info, in concurrent or asynchronous code (e.g., web requests, ETL pipelines).

Example usage:
- Setting and getting context variables
- Using context variables in async code
- Resetting context variables
"""

# Define a context variable for storing the current user/session
current_user: contextvars.ContextVar[Optional[str]] = contextvars.ContextVar('current_user', default=None)


def set_current_user(user_id: str) -> None:
    """
    Set the current user in the context variable.

    Args:
        user_id (str): The user identifier to set.
    """
    current_user.set(user_id)


def get_current_user() -> Optional[str]:
    """
    Get the current user from the context variable.

    Returns:
        Optional[str]: The current user identifier, or None if not set.
    """
    return current_user.get()


def reset_current_user(token: contextvars.Token) -> None:
    """
    Reset the current user context variable to a previous state.

    Args:
        token (contextvars.Token): The token returned by set().
    """
    current_user.reset(token)


async def process_data_for_user(user_id: str, data: Any) -> None:
    """
    Simulate processing data for a specific user in an async context.

    Args:
        user_id (str): The user identifier.
        data (Any): The data to process.
    """
    # Set the user in the context for this task
    token = current_user.set(user_id)
    try:
        # Simulate async processing
        await asyncio.sleep(0.1)
        print(f"[{get_current_user()}] Processing data: {data}")
    finally:
        # Always reset context to avoid leaking state
        current_user.reset(token)


async def main_async_example() -> None:
    """
    Demonstrate contextvars in concurrent async tasks.
    """
    users = ["Alex", "Blake", "Chris", "Dylan", "Elliott"]
    data = [random.choice(range(100, 10000, 100)) for _ in range(len(users))]
    await asyncio.gather(*(process_data_for_user(u, d) for u, d in zip(users, data)))


def sync_example() -> None:
    """
    Demonstrate contextvars in synchronous code.
    """
    print("=== Synchronous Example ===")
    # set_current_user('dave')
    set_current_user(random.choice(["Alex", "Blake", "Chris", "Dylan", "Elliott"]))
    print(f"Current user: {get_current_user()}")

    # Save the token to reset later
    # token = current_user.set('eve')
    token = current_user.set(random.choice(["Alex", "Blake", "Chris", "Dylan", "Elliott"]))
    print(f"Current user after set: {get_current_user()}")
    reset_current_user(token)
    print(f"Current user after reset: {get_current_user()}")


if __name__ == "__main__":
    print("\n=== Synchronous Example ===")
    sync_example()

    print("\n=== Asynchronous Example ===")
    asyncio.run(main_async_example())

"""
Troubleshooting & Efficiency Tips:
- Reset context variables after temporary changes (use try/finally).
- Use contextvars for per-request/session state in async/concurrent code (e.g., ETL jobs, web APIs).
- Avoid using global variables for context-specific data in concurrent code.
"""
