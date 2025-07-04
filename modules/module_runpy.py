import runpy
from typing import Any, Dict, Optional

"""
`runpy` allows you to locate and run Python modules and scripts as if they were run from the command line.

Common use cases:
- Dynamically executing ETL scripts or BI modules.
- Running reporting scripts in isolated namespaces.
- Integrating Python modules into workflow automation.
"""


def run_module_as_script(module_name: str, run_name: str = "__main__") -> Dict[str, Any]:
    """
    Runs a module as if it were a script (like `python -m module_name`).

    Args:
        module_name (str): The name of the module to run (e.g., 'my_etl_script').
        run_name (str): The value of __name__ in the executed module. Default is '__main__'.

    Returns:
        Dict[str, Any]: The globals dictionary from the executed module.

    Example:
        # Run a BI ETL module as a script
        result = run_module_as_script('etl.load_data')
        print(result['main'])  # Access variables/functions defined in the module
    """
    try:
        return runpy.run_module(module_name, run_name=run_name)
    except ImportError as e:
        print(f"Module '{module_name}' not found: {e}")
        return {}
    except Exception as e:
        print(f"Error running module '{module_name}': {e}")
        return {}


def run_python_script(script_path: str) -> Dict[str, Any]:
    """
    Runs a Python script file and returns its global namespace.

    Args:
        script_path (str): Path to the Python script (e.g., '/path/to/report.py').

    Returns:
        Dict[str, Any]: The globals dictionary from the executed script.

    Example:
        # Run a reporting script and access its results
        result = run_python_script('scripts/generate_report.py')
        print(result.get('report_data'))
    """
    try:
        return runpy.run_path(script_path)
    except FileNotFoundError as e:
        print(f"Script file '{script_path}' not found: {e}")
        return {}
    except Exception as e:
        print(f"Error running script '{script_path}': {e}")
        return {}


def run_module_in_namespace(module_name: str, custom_globals: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Runs a module in a custom global namespace, useful for testing or sandboxing.

    Args:
        module_name (str): The name of the module to run.
        custom_globals (Optional[Dict[str, Any]]): Custom globals to use.

    Returns:
        Dict[str, Any]: The updated globals dictionary.

    Example:
        # Run a BI module with custom globals
        custom_env = {'DATA_SOURCE': 'test_db'}
        result = run_module_in_namespace('etl.load_data', custom_env)
    """
    try:
        return runpy.run_module(module_name, init_globals=custom_globals)
    except Exception as e:
        print(f"Error running module '{module_name}' in custom namespace: {e}")
        return {}


if __name__ == "__main__":
    # Run a module as a script (simulate `python -m my_bi_module`)
    print("Running 'my_bi_module' as a script:")
    result1 = run_module_as_script('my_bi_module')
    print(result1.keys())

    # Run a Python script file (simulate `python my_report.py`)
    print("\nRunning 'scripts/my_report.py':")
    result2 = run_python_script('scripts/my_report.py')
    print(result2.keys())

    # Run a module with custom globals (for testing)
    print("\nRunning 'my_bi_module' with custom globals:")
    custom_env = {'DATA_SOURCE': 'test_db'}
    result3 = run_module_in_namespace('my_bi_module', custom_env)
    print(result3.keys())

"""
Troubleshooting Tips:
- Ensure the module/script paths are correct and accessible.
- Handle ImportError/FileNotFoundError for missing modules/scripts.
- Use the returned globals dict to access variables/functions defined in the executed code.

Efficiency Tips:
- Use runpy for dynamic execution in workflow automation.
- Use custom globals for testing modules in isolation.
- Avoid using runpy for performance-critical code; it's best for orchestration and automation.
"""
