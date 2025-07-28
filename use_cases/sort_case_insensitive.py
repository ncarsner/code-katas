import random
import string
from timeit import timeit


def generate_random_string(length=10):
    """Generate a random string of fixed length."""
    letters = string.ascii_letters  # Includes both uppercase and lowercase letters
    return "".join(random.choice(letters) for _ in range(length))


random_strings = [generate_random_string(random.randint(10, 20)) for _ in range(10_000)]


# Sort using str.lower for case-insensitive sorting
def sort_using_str_lower():
    """Sort a list of strings in a case-insensitive manner."""
    return sorted(random_strings, key=str.lower)


# Sort using a lambda function for case-insensitive sorting
def sort_using_lambda():
    """Sort a list of strings in a case-insensitive manner using a lambda function."""
    return sorted(random_strings, key=lambda s: s.lower())


# Sort using the built-in sorted function with str.casefold for case-insensitive sorting
def sort_using_casefold():
    """Sort a list of strings in a case-insensitive manner using str.casefold."""
    return sorted(random_strings, key=str.casefold)


if __name__ == "__main__":
    # Call each sorting function
    sorted_strings_lower = sort_using_str_lower()
    sorted_strings_casefold = sort_using_casefold()
    sorted_strings_lambda = sort_using_lambda()

    # Print the first n sorted strings for verification
    first_n_string = 5
    print("Sorted using str.lower:", sorted_strings_lower[:first_n_string])
    print("Sorted using str.casefold:", sorted_strings_casefold[:first_n_string])
    print("Sorted using lambda:", sorted_strings_lambda[:first_n_string])

    # Measure the time taken for each sorting method
    n = 1_000
    time_str_lower = timeit(sort_using_str_lower, number=n)
    time_casefold = timeit(sort_using_casefold, number=n)
    time_lambda = timeit(sort_using_lambda, number=n)

    # Print the time taken for each method
    print(f"Time taken using str.lower: {time_str_lower:.4f} seconds")
    print(f"Time taken using str.casefold: {time_casefold:.4f} seconds")
    print(f"Time taken using lambda: {time_lambda:.4f} seconds")
