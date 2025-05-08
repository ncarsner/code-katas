from string import ascii_lowercase as lets
from typing import Tuple

phrases = [
    "The quick brown fox jumps over the lazy dog",
    "A journey of a thousand miles begins with a single step",
    "Pack my box with five dozen liquor jugs",
    "The future belongs to those who believe in the beauty of their dreams",
    "Sphinx of black quartz, judge my vow",
    "It does not matter how slowly you go as long as you do not stop",
    "The five boxing wizards jump quickly",
    "The best way to predict the future is to create it",
    "Jinxed wizards pluck ivy from the big quilt",
]


def is_it_a_pangram(phrase: str) -> Tuple[str, bool]:
    """
    Check if a phrase is a pangram (contains every letter of the alphabet at least once).

    Args:
        phrase (str): The input phrase to check.

    Returns:
        Tuple[str, bool]: A tuple containing the original phrase and a boolean indicating if it's a pangram.
    """
    # Normalize the phrase to lowercase and remove spaces
    normalized_phrase = "".join(filter(str.isalpha, phrase.lower()))

    # Check if all letters are present
    is_pangram = set(lets).issubset(set(normalized_phrase))

    return phrase, is_pangram


if __name__ == "__main__":
    for phrase in phrases:
        original_phrase, is_pangram = is_it_a_pangram(phrase)
        print(f"{is_pangram} - Phrase: {original_phrase}")
        print("-" * 40)
