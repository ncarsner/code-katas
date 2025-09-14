import random
import string

students = [
    "Alex", "Anthony", "Brian", "Blake", "Cameron", "Chris", "Daphnie", "Dillon", "Elliott",
    "Finley", "Frank", "Gabriel", "Gray", "Harper", "Hayden", "Ira", "Jaime", "Jordan",
    "Kendall", "Ky", "Logan", "Lorraine", "McKenzie", "Morgan", "Parker", "Quinn", "Riley",
    "Sean", "Sawyer", "Taylor", "Tristan", "Tyler", "Vivian", "Val", "Winter", "Zion",
]


def is_long_name(names: list, length: int = 4) -> list:
    """Return names longer than N characters using filter."""
    return list(filter(lambda name: len(name) > length, names))


def name_starts_with(names: list, letter: str) -> list:
    """Filter names that start with a specific letter."""
    return list(filter(lambda name: name.startswith(letter), names))


def names_contain(names: list, substring: str) -> list:
    """Filter names that contain a specific substring."""
    return list(filter(lambda name: substring.lower() in name.lower(), names))


if __name__ == "__main__":
    random_length = random.randint(3, 7)
    print(f"Names longer than {random_length} characters:")
    print(is_long_name(students, random_length))

    random_letter = random.choice(string.ascii_uppercase)
    print(f"\nNames starting with '{random_letter}':")
    print(name_starts_with(students, random_letter))

    random_substring = random.choice(string.ascii_lowercase)
    print(f"\nNames containing '{random_substring}':")
    print(names_contain(students, random_substring))
