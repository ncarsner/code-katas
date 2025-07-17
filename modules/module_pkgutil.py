import pkgutil
import importlib
from typing import List, Optional

"""
Practical uses of the built-in `pkgutil` module:
- Discover available modules in a package (useful for plugin systems or dynamic imports)
- Read data files bundled within packages (e.g., configuration, templates)
- Iterate over submodules for automation or reporting
"""


def list_submodules(package_name: str) -> List[str]:
    """
    List all submodules and subpackages in a given package.

    Args:
        package_name (str): The name of the package to inspect.

    Returns:
        List[str]: List of submodule/subpackage names.

    Example:
        >>> list_submodules('pandas')
        ['pandas._libs', 'pandas.api', ...]
    """
    package = importlib.import_module(package_name)
    return [
        name
        for _, name, _ in pkgutil.iter_modules(package.__path__, package.__name__ + ".")
    ]


def load_module(module_name: str):
    """
    Dynamically import a module by name.

    Args:
        module_name (str): The full name of the module.

    Returns:
        module: The imported module object.

    Example:
        >>> mod = load_module('pandas.api')
        >>> print(mod.__name__)
        pandas.api
    """
    return importlib.import_module(module_name)


def read_package_data(package: str, resource: str) -> Optional[bytes]:
    """
    Read a data file bundled within a package.

    Args:
        package (str): The package name.
        resource (str): The relative path to the resource file.

    Returns:
        Optional[bytes]: The file contents as bytes, or None if not found.

    Example:
        >>> read_package_data('my_pkg', 'data/config.yaml')
    """
    try:
        return pkgutil.get_data(package, resource)
    except Exception as e:
        print(f"Error reading resource '{resource}' from package '{package}': {e}")
        return None


def discover_plugins(package_name: str) -> List[str]:
    """
    Discover all plugin modules in a given package (e.g., for ETL steps, report generators).

    Args:
        package_name (str): The package containing plugins.

    Returns:
        List[str]: List of plugin module names.

    Example:
        >>> discover_plugins('mycompany.plugins')
    """
    return list_submodules(package_name)


if __name__ == "__main__":
    # List all submodules in the 'pkgutil' package itself
    print("Submodules in 'pkgutil':", list_submodules("pkgutil"))

    # Read a data file from a package (if exists)
    data = read_package_data("pkgutil", "__init__.py")
    if data:
        print("First 100 bytes of pkgutil/__init__.py:", data[:100])

    # Discover plugins in a hypothetical 'mycompany.plugins' package
    # print("Plugins:", discover_plugins('mycompany.plugins'))
    # (Uncomment and replace with your actual package)
