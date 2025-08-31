import tokenize
from typing import List, IO
import io

"""
The `tokenize` module is useful for analyzing and processing Python source code, which can be helpful for business intelligence developers/analysts who need to parse or analyze Python scripts, such as:

1. Tokenizing a Python script to extract function definitions.
2. Identifying and counting comments in a Python script.
3. Extracting string literals for further analysis (e.g., SQL queries in BI scripts).
"""



def extract_function_definitions(file: IO[bytes]) -> List[str]:
    """
    Extracts all function definitions from a Python script.

    Args:
        file (IO[bytes]): A file-like object containing the Python script.

    Returns:
        List[str]: A list of function names defined in the script.
    """
    function_names = []
    tokens = tokenize.tokenize(file.readline)
    for token in tokens:
        if token.type == tokenize.NAME and token.string == "def":
            # The next token after "def" is the function name
            next_token = next(tokens)
            if next_token.type == tokenize.NAME:
                function_names.append(next_token.string)
    return function_names


def count_comments(file: IO[bytes]) -> int:
    """
    Counts the number of comments in a Python script.

    Args:
        file (IO[bytes]): A file-like object containing the Python script.

    Returns:
        int: The number of comments in the script.
    """
    comment_count = 0
    tokens = tokenize.tokenize(file.readline)
    for token in tokens:
        if token.type == tokenize.COMMENT:
            comment_count += 1
    return comment_count


def extract_string_literals(file: IO[bytes]) -> List[str]:
    """
    Extracts all string literals from a Python script.

    Args:
        file (IO[bytes]): A file-like object containing the Python script.

    Returns:
        List[str]: A list of string literals found in the script.
    """
    string_literals = []
    tokens = tokenize.tokenize(file.readline)
    for token in tokens:
        if token.type == tokenize.STRING:
            string_literals.append(token.string)
    return string_literals


if __name__ == "__main__":
    sample_script = b"""
    # This is a sample Python script
    def calculate_sum(a, b):
        \"\"\"Calculate the sum of two numbers.\"\"\"
        return a + b

    def greet_user(name):
        \"\"\"Greet the user by name.\"\"\"
        print(f"Hello, {name}!")

    # End of script
    """

    # Wrap the script in a BytesIO object to simulate a file
    script_file = io.BytesIO(sample_script)

    # Extract function definitions
    script_file.seek(0)
    functions = extract_function_definitions(script_file)
    print("Function Definitions:", functions)

    # Count comments
    script_file.seek(0)
    comments = count_comments(script_file)
    print("Number of Comments:", comments)

    # Extract string literals
    script_file.seek(0)
    strings = extract_string_literals(script_file)
    print("String Literals:", strings)
