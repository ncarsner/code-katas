import string
from typing import List, Dict
import random


def clean_column_names(columns: List[str]) -> List[str]:
    """
    Cleans a list of column names by removing punctuation and converting to lowercase.
    Useful for standardizing dataframes in BI workflows.

    Args:
        columns (List[str]): List of column names.

    Returns:
        List[str]: Cleaned column names.
    """
    table = str.maketrans("", "", string.punctuation)
    return [col.translate(table).replace(" ", "_").lower() for col in columns]


def is_valid_identifier(name: str) -> bool:
    """
    Checks if a string is a valid Python identifier (e.g., for use as a variable or column name).

    Args:
        name (str): The string to check.

    Returns:
        bool: True if valid, False otherwise.
    """
    allowed = string.ascii_letters + string.digits + "_"
    return all(c in allowed for c in name) and name[0] in string.ascii_letters + "_"


def mask_sensitive_data(text: str, mask_char: str = "*") -> str:
    """
    Masks all digits in a string (e.g., for hiding sensitive numbers in reports).

    Args:
        text (str): The input string.
        mask_char (str): The character to use for masking.

    Returns:
        str: The masked string.
    """
    return "".join(mask_char if c in string.digits else c for c in text)


def count_word_frequencies(text: str, threshold: int = 1) -> Dict[str, int]:
    """
    Counts the frequency of each word in a string, ignoring punctuation and case.
    Optionally filters to only include words appearing at least 'threshold' times.

    Args:
        text (str): The input text.
        threshold (int): Minimum number of occurrences for a word to be included.

    Returns:
        Dict[str, int]: Dictionary of word frequencies.
    """
    table = str.maketrans("", "", string.punctuation)
    words = text.translate(table).lower().split()
    freq: Dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return {word: count for word, count in freq.items() if count >= threshold}


def generate_random_password(length: int = 12) -> str:
    """
    Generates a random password using letters, digits, and punctuation.

    Args:
        length (int): Length of the password.

    Returns:
        str: The generated password.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    # Clean column names
    cols = ["First Name", "E-mail!", "Salary($)", "Hire Date"]
    print("Cleaned columns:", clean_column_names(cols))

    # Validate identifier
    identifier_a = "employee_id"
    identifier_b = "123name"
    print(f"{identifier_a} valid: {is_valid_identifier(identifier_a)}")
    print(f"{identifier_b} valid: {is_valid_identifier(identifier_b)}")

    # Mask sensitive data
    ssn = (
        f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"
    )
    print("Original SSN:", ssn)
    print(f"Masked SSN: {mask_sensitive_data(ssn)}")
    # print("Masked SSN:", mask_sensitive_data("SSN: 123-45-6789"))

    # Count word frequencies
    sample_text = (
        "Revenue, revenue, and more revenue! Growth is key. Growth is the answer."
    )
    print("Word frequencies:", count_word_frequencies(sample_text, threshold=2))

    # Generate random password
    print("Random password:", generate_random_password(16))
