import pytest
from use_cases.pytest_functions import is_palindrome, StringUtils, is_anagram, MathUtils

"""
This module contains test functions for the `is_palindrome` function, the `reverse_string` method of the `StringUtils` class, the `is_anagram` function, and the `add` and `multiply` methods of the `MathUtils` class using pytest's parameterize decorator.
Functions:
    test_is_palindrome(s: str, expected: bool) -> None:
        Tests the `is_palindrome` function with various inputs and their expected outputs.
    test_reverse_string() -> None:
        Tests the `reverse_string` method of the `StringUtils` class with various inputs using individual assertion statements.
    test_string_utils_reverse_string(string_input: str, expected: str) -> None:
        Tests the `reverse_string` method of the `StringUtils` class with various inputs and their expected outputs.
    test_is_anagram(string_a: str, string_b: str, expected: bool) -> None:
        Tests the `is_anagram` function with various pairs of inputs and their expected outputs.
    test_add(number_a: int, number_b: int, expected: int) -> None:
        Tests the `add` method of the `MathUtils` class with different pairs of inputs and their expected sums.
    test_multiply(number_a: int, number_b: int, expected: int) -> None:
        Tests the `multiply` method of the `MathUtils` class with different pairs of inputs and their expected products.

Notes:
    `@pytest.mark.parametrize` decorator allows multiple sets of inputs and expected outputs to be defined.
    Easier to test functions and methods with various inputs without writing repetitive code.
    To run these tests, navigate to the directory containing this file and run `pytest` in the terminal.
"""


# Test function for 'is_palindrome' using pytest's parameterize decorator
@pytest.mark.parametrize(
    "string_input, expected",
    [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("A man a plan a canal Panama".replace(" ", "").lower(), True),
    ],
)
def test_is_palindrome(string_input, expected):
    assert is_palindrome(string_input) == expected


# Test method for 'reverse_string' in StringUtils class using individual assertion statements
def test_reverse_string():
    string_utils = StringUtils()
    assert string_utils.reverse_string("hello") == "olleh"
    assert string_utils.reverse_string("world") == "dlrow"
    assert string_utils.reverse_string("") == ""
    assert string_utils.reverse_string("a") == "a"
    assert string_utils.reverse_string("12345") != "12345"


# Test method for 'reverse_string' in StringUtils class using pytest's parameterize decorator
@pytest.mark.parametrize(
    "string_input, expected",
    [("hello", "olleh"), ("", ""), ("Python", "nohtyP"), ("12345", "54321")],
)
def test_string_utils_reverse_string(string_input, expected):
    utils = StringUtils()
    assert utils.reverse_string(string_input) == expected


@pytest.mark.parametrize(
    "string_a, string_b, expected",
    [
        ("listen", "silent", True),
        ("triangle", "integral", True),
        ("apple", "pale", False),
        ("", "", True),
        ("a", "a", True),
        ("shelf", "flesh", True),
        ("flesh", "feels", False)
    ],
)
def test_is_anagram(string_a, string_b, expected):
    assert is_anagram(string_a, string_b) == expected


@pytest.mark.parametrize(
    "number_a, number_b, expected",
    [
        (1, 2, 3),
        (-1, 1, 0),
        (0, 0, 0),
        (100, 200, 300),
        (-5, -5, -10),
    ],
)
def test_add(number_a, number_b, expected):
    math_utils = MathUtils()
    assert math_utils.add(number_a, number_b) == expected


@pytest.mark.parametrize(
    "number_a, number_b, expected",
    [
        (1, 2, 2),
        (-1, 1, -1),
        (0, 10, 0),
        (100, 200, 20000),
        (-5, -5, 25),
    ],
)
def test_multiply(number_a, number_b, expected):
    math_utils = MathUtils()
    assert math_utils.multiply(number_a, number_b) == expected
