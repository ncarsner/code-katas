import tomllib
from typing import Any, Dict, Optional

"""
The `tomllib` module in Python 3.11+ can read and parse TOML (Tom's Obvious, Minimal Language) configuration files; commonly used for project settings, data pipelines, and environment configs.
"""


def load_toml_file(file_path: str) -> Dict[str, Any]:
    """
    Loads and parses a TOML file.

    Args:
        file_path (str): Path to the TOML file.

    Returns:
        Dict[str, Any]: Parsed TOML data as a nested dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        tomllib.TOMLDecodeError: If the file is not valid TOML.

    Example:
        config = load_toml_file("config.toml")
        print(config["database"]["host"])
    """
    with open(file_path, "rb") as f:
        data = tomllib.load(f)
    return data


def get_config_value(config: Dict[str, Any], key_path: str, default: Optional[Any] = None) -> Any:
    """
    Retrieves a nested value from a TOML config dictionary using dot notation.

    Args:
        config (Dict[str, Any]): The parsed TOML config.
        key_path (str): Dot-separated path to the value (e.g., "database.host").
        default (Optional[Any]): Value to return if key is not found.

    Returns:
        Any: The value at the specified key path, or default if not found.

    Example:
        host = get_config_value(config, "database.host", default="localhost")
    """
    keys = key_path.split(".")
    value = config
    try:
        for key in keys:
            value = value[key]
        return value
    except (KeyError, TypeError):
        return default


def print_config_summary(config: Dict[str, Any]) -> None:
    """
    Prints a summary of the top-level keys in the TOML config.

    Args:
        config (Dict[str, Any]): The parsed TOML config.

    Example:
        print_config_summary(config)
    """
    print("TOML Config Summary:")
    for section in config:
        print(f"  - {section}: {type(config[section]).__name__}")


if __name__ == "__main__":
    # Example TOML file for demonstration (save as 'example_config.toml'):
    # [database]
    # host = "localhost"
    # port = 5432
    # user = "bi_user"
    # password = "secret"
    #
    # [pipeline]
    # name = "daily_etl"
    # schedule = "0 2 * * *"

    try:
        config = load_toml_file("example_config.toml")
        print_config_summary(config)
        db_host = get_config_value(config, "database.host")
        pipeline_name = get_config_value(config, "pipeline.name")
        print(f"Database Host: {db_host}")
        print(f"Pipeline Name: {pipeline_name}")
    except FileNotFoundError:
        print("TOML file not found. Please check the file path.")
    except tomllib.TOMLDecodeError as e:
        print(f"Error parsing TOML file: {e}")

"""
TROUBLESHOOTING TIPS:
- Ensure your TOML file is valid and follows TOML syntax (see https://toml.io).
- Use 'tomllib.TOMLDecodeError' to catch parsing errors.
- Always open TOML files in binary mode ('rb') as required by tomllib.
- Use clear key paths for nested values (e.g., "section.subsection.key").
"""
