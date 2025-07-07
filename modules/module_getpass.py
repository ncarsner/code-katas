import getpass
from typing import Optional

"""
Python's built-in getpass module is useful for connecting to databases or APIs without exposing sensitive information.
"""


def prompt_for_password(prompt: str = "Enter your password: ") -> str:
    """
    Securely prompts the user for a password without echoing input.

    Args:
        prompt (str): The prompt message displayed to the user.

    Returns:
        str: The password entered by the user.

    Example:
        password = prompt_for_password("Database password: ")
    """
    try:
        return getpass.getpass(prompt)
    except Exception as e:
        print(f"Error reading password: {e}")
        return ""


def prompt_for_username(prompt: str = "Enter your username: ") -> str:
    """
    Prompts the user for a username (input is visible).

    Args:
        prompt (str): The prompt message displayed to the user.

    Returns:
        str: The username entered by the user.

    Example:
        username = prompt_for_username("Database username: ")
    """
    return input(prompt)


def authenticate_user() -> Optional[tuple[str, str]]:
    """
    Example function to prompt for username and password,
    simulating a login process for a BI tool or database.

    Returns:
        Optional[tuple[str, str]]: (username, password) if both are provided, else None.

    Example:
        creds = authenticate_user()
        if creds:
            username, password = creds
            # Use credentials to connect to a database
    """
    username = prompt_for_username()
    password = prompt_for_password()
    if username and password:
        return username, password
    print("Username or password not provided.")
    return None


def getpass_troubleshooting():
    """
    Notes on troubleshooting getpass usage:
    - On some IDEs (e.g., IDLE, Jupyter), getpass may not work as expected.
    - Use a terminal/command prompt for best results.
    - If getpass fails, it may fall back to visible input with a warning.
    """
    print(getpass.__doc__)


if __name__ == "__main__":
    # Prompt for credentials and print (never print passwords in production!)
    creds = authenticate_user()
    if creds:
        username, password = creds
        print(f"Username entered: {username}")
        print("Password received (not displayed for security).")
    else:
        print("Authentication failed.")

    # Show getpass module documentation for troubleshooting
    # getpass_troubleshooting()
