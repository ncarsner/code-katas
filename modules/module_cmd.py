import cmd
import pandas as pd
from typing import Optional

"""
Demonstrates the use of Python's built-in `cmd` module for command-line interface (CLI) applications, such as to load, view, and summarize CSV data files interactively.

Includes type hints, docstrings, and comments for clarity and maintainability.
"""


class BICmd(cmd.Cmd):
    """
    A simple command-line interface for business intelligence tasks.
    Allows loading, viewing, and summarizing CSV data interactively.
    """

    intro = "Welcome to the BI CLI. Type help or ? to list commands.\n"
    prompt = "(bi) "
    file = None

    def __init__(self):
        super().__init__()
        self.data: Optional[pd.DataFrame] = None

    def do_load(self, arg: str) -> None:
        """
        Load a CSV file into memory.
        Usage: load <filepath>
        Example: load data/sales.csv
        """
        try:
            self.data = pd.read_csv(arg)
            print(
                f"Loaded data from {arg} ({len(self.data)} rows, {len(self.data.columns)} columns)."
            )
        except Exception as e:
            print(f"Error loading file: {e}")

    def do_head(self, arg: str) -> None:
        """
        Display the first N rows of the loaded data.
        Usage: head [n]
        Example: head 10
        """
        if self.data is None:
            print("No data loaded. Use 'load <filepath>' first.")
            return
        try:
            n = int(arg) if arg else 5
            print(self.data.head(n))
        except Exception as e:
            print(f"Error displaying head: {e}")

    def do_summary(self, arg: str) -> None:
        """
        Show summary statistics of the loaded data.
        Usage: summary
        """
        if self.data is None:
            print("No data loaded. Use 'load <filepath>' first.")
            return
        print(self.data.describe(include="all"))

    def do_columns(self, arg: str) -> None:
        """
        List all columns in the loaded data.
        Usage: columns
        """
        if self.data is None:
            print("No data loaded. Use 'load <filepath>' first.")
            return
        print("Columns:", ", ".join(self.data.columns))

    def do_exit(self, arg: str) -> bool:
        """
        Exit the CLI.
        Usage: exit
        """
        print("Exiting BI CLI.")
        return True

    def do_EOF(self, arg: str) -> bool:
        """
        Handle EOF (Ctrl+D/Ctrl+Z) to exit.
        """
        print("Exiting BI CLI.")
        return True

    def default(self, line: str) -> None:
        """
        Handle unrecognized commands.
        """
        print(f"Unknown command: {line}. Type 'help' or '?' for a list of commands.")


if __name__ == "__main__":
    """
    To run the CLI:
    $ python module_cmd.py

    Example session:
    (bi) load data.csv
    (bi) columns
    (bi) head 10
    (bi) summary
    (bi) exit
    """
    BICmd().cmdloop()
