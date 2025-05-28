import unicodedata
from typing import Dict
import random

"""
Useful for normalization, character categorization, and name lookup, for data cleaning, validation, and reporting.
"""


def normalize_text(text: str, form: str = "NFKC") -> str:
    """
    Normalize unicode text to a standard form.

    Args:
        text (str): The input string to normalize.
        form (str): The normalization form ('NFC', 'NFKC', 'NFD', 'NFKD').

    Returns:
        str: The normalized string.

    Example:
        >>> normalize_text("Café")
        'Café'
    """
    return unicodedata.normalize(form, text)


def remove_accents(text: str) -> str:
    """
    Remove accents from a string using unicode normalization.

    Args:
        text (str): The input string.

    Returns:
        str: The string with accents removed.

    Example:
        >>> remove_accents("Café")
        'Cafe'
    """
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def get_unicode_category_summary(text: str) -> Dict[str, int]:
    """
    Summarize the unicode categories present in a string.

    Args:
        text (str): The input string.

    Returns:
        Dict[str, int]: A dictionary mapping unicode categories to their counts.

    Example:
        >>> get_unicode_category_summary("A1!é")
        {'Lu': 1, 'Nd': 1, 'Po': 1, 'Ll': 1, 'Mn': 1}
    """
    summary: Dict[str, int] = {}
    for char in text:
        cat = unicodedata.category(char)
        summary[cat] = summary.get(cat, 0) + 1
    return summary


def get_char_name(char: str) -> str:
    """
    Get the official unicode name for a character.

    Args:
        char (str): A single character.

    Returns:
        str: The unicode name, or a placeholder if not found.

    Example:
        >>> get_char_name("é")
        'LATIN SMALL LETTER E WITH ACUTE'
    """
    try:
        return unicodedata.name(char)
    except ValueError:
        return "<no name found>"


def lookup_char_by_name(name: str) -> str:
    """
    Lookup a character by its unicode name.

    Args:
        name (str): The unicode name.

    Returns:
        str: The corresponding character.

    Example:
        >>> lookup_char_by_name("LATIN CAPITAL LETTER A")
        'A'
    """
    try:
        return unicodedata.lookup(name)
    except KeyError:
        return "<no character found>"


def strip_non_printable(text: str) -> str:
    """
    Remove non-printable characters from a string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with non-printable characters removed.

    Example:
        >>> strip_non_printable("Hello\u200bWorld")
        'HelloWorld'
    """
    return "".join(c for c in text if unicodedata.category(c)[0] != "C")


if __name__ == "__main__":
    sample = "Café, résumé, coöperate, naïve, 𝟘𝟙𝟚, Hello\u200bWorld, \u200e, Benny & the Jets"
    print("\nOriginal:", sample)
    print("Normalized (NFKC):", normalize_text(sample))
    print("Without accents:", remove_accents(sample))
    print("Unicode category summary:", get_unicode_category_summary(sample))
    vowel_scalars = [
        "á", "à", "ä", "â", "ã", "å", "ā",  # a variants
        "é", "è", "ë", "ê", "ē",            # e variants
        "í", "ì", "ï", "î", "ī",            # i variants
        "ó", "ò", "ö", "ô", "õ", "ō",       # o variants
        "ú", "ù", "ü", "û", "ū",            # u variants
        "ý", "ÿ",                           # y variants
        "Á", "À", "Ä", "Â", "Ã", "Å", "Ā",  # A variants
        "É", "È", "Ë", "Ê", "Ē",            # E variants
        "Í", "Ì", "Ï", "Î", "Ī",            # I variants
        "Ó", "Ò", "Ö", "Ô", "Õ", "Ō",       # O variants
        "Ú", "Ù", "Ü", "Û", "Ū",            # U variants
        "Ý", "Ÿ"                            # Y variants
    ]
    random_vowel = random.choice(vowel_scalars)
    random_name = get_char_name(random.choice(vowel_scalars))
    print(f"\nUnicode name for '{random_vowel}': {get_char_name(random_vowel)}")
    print(f"Character for {random_name}: {lookup_char_by_name(random_name)}")
    print("Without non-printable:", strip_non_printable(sample))
