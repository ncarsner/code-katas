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


def strip_non_printable_and_whitespace(text: str) -> str:
    """
    Remove non-printable characters and whitespace from a string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with non-printable characters and whitespace removed.

    Example:
        >>> strip_non_printable_and_whitespace("Hello \u200bWorld")
        'HelloWorld'
    """
    return "".join(c for c in text if unicodedata.category(c)[0] != "C" and not c.isspace())


def display_unicode_categories(text: str) -> None:
    """
    Display the unicode categories of characters in a string.

    Args:
        text (str): The input string.
    """
    for char in text:
        print(f"Character: {char!r}, Category: {unicodedata.category(char)}")


def display_hex_and_name(text: str) -> None:
    """
    Display the hexadecimal code and unicode name for each character in a string.

    Args:
        text (str): The input string.
    """
    for char in text:
        hex_code = f"U+{ord(char):04X}"
        name = get_char_name(char)
        print(f"{char}, {ord(char)}, {hex_code}, {name}")


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
    print("Without non-printable and whitespace:", strip_non_printable_and_whitespace(sample))

    # print("\nUnicode categories:")
    # display_unicode_categories(sample)

    # print("\nHexadecimal codes and names:")
    # display_hex_and_name(sample)

    greeting_text = "¡Hola, ¿cómo estás? München"
    print("\nCombined greeting:", greeting_text)
    print("Normalized (NFKC):", normalize_text(greeting_text))
    print("Without accents:", remove_accents(greeting_text))

    # List of emojis comprised of multiple ordinal characters (grapheme clusters)
    multi_char_emojis = [
        "👨‍👩‍👧‍👦",  # family: man, woman, girl, boy
        "🧑‍🎓", # student (person + graduation cap)
        "👩‍🚀",   # woman astronaut
        "👨‍🦽",   # man in manual wheelchair
        "👩‍🦳",   # woman: white hair
        "👨‍🦲",   # man: bald
        "🏳️‍🌈",    # rainbow flag
        "😶‍🌫️", # face in clouds
        "💩",   # pile of poo
    ]

    emoji = random.choice(multi_char_emojis)
    print(f"\nSelected emoji: {emoji}  (length: {len(emoji)})")
    for char in emoji:
        # print(f"{char!r}: {[ord(c) for c in char]} (length: {len(char)})")
        print(f"{char!r:<8} {ord(char):<8} {hex(ord(char)):<10} U+{ord(char):04X}   {get_char_name(char):<40}")
