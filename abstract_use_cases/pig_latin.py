# Pig Latin Translator
# This script translates English sentences into Pig Latin.

VOWELS = "aeiouAEIOU"


def translate_to_pig_latin(sentence: str) -> str:
    """
    Translate a sentence into Pig Latin.

    Args:
        sentence (str): The input sentence to translate.

    Returns:
        str: The translated Pig Latin sentence.
    """
    if not isinstance(sentence, str):
        raise ValueError("Input must be a string.")

    if not sentence.strip():
        return ""  # Return empty string for empty input

    words = split_into_words(sentence)
    return process_words(words)


def split_into_words(sentence: str) -> list:
    """
    Split a sentence into words.

    Args:
        sentence (str): The input sentence to split.

    Returns:
        list: A list of words from the sentence.
    """
    return [word.strip() for word in sentence.split() if word.strip()]


def translate_word(word: str) -> str:
    """
    Translate a single word into Pig Latin.

    Args:
        word (str): The input word to translate.

    Returns:
        str: The translated Pig Latin word.
    """
    if not word.isalpha():
        return word  # Return non-alphabetic words unchanged

    if word[0] in VOWELS:
        return word + "yay"

    # Handle consonant-starting words
    first_vowel_index = next(
        (i for i, char in enumerate(word) if char in VOWELS), len(word)
    )
    return word[first_vowel_index:] + word[:first_vowel_index] + "ay"


def process_words(words: list) -> str:
    """
    Process a list of words and translate them into Pig Latin.

    Args:
        words (list): The list of words to process.

    Returns:
        str: The translated Pig Latin sentence.
    """
    return " ".join(translate_word(word) for word in words)


def handle_errors(func):
    """
    Decorator to handle errors in the translation process.

    Args:
        func (callable): The function to wrap with error handling.

    Returns:
        callable: The wrapped function with error handling.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f"Error: {e}")
            return ""

    return wrapper


@handle_errors
def test_translate_to_pig_latin():
    assert translate_to_pig_latin("hello world") == "ellohay orldway"
    assert translate_to_pig_latin("This is a test") == "isThay isyay ayay esttay"
    assert translate_to_pig_latin("Python is fun!") == "ythonPay isyay unfay!"
    assert translate_to_pig_latin("I love programming") == "Iyay ovelay ogrammingpray"
    assert (
        translate_to_pig_latin("123 numbers are not words")
        == "123 umbersnay areyay otnay ordsway"
    )
    assert translate_to_pig_latin("") == ""  # Test empty string
    assert translate_to_pig_latin("hello") == "ellohay"  # Test single word


if __name__ == "__main__":
    # Test cases for Pig Latin Translator
    test_sentences = [
        "hello world",
        "This is a test",
        "Python is fun!",
        "I love programming",
        "123 numbers are not words",
        "",
    ]

    for sentence in test_sentences:
        print(f"Original: {sentence}")
        print(f"Pig Latin: {translate_to_pig_latin(sentence)}")
        print("-" * 30)
