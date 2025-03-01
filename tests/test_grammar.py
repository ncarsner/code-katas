from collections import defaultdict
from utilities.grammar_reviewer import GrammarReviewer


def test_no_duplicate_words():
    reviewer = GrammarReviewer()
    word_occurrences = defaultdict(int)

    # Count occurrences for each word from keys and their replacement lists.
    for key, values in reviewer.replacements.items():
        word_occurrences[key] += 1
        for value in values:
            word_occurrences[value] += 1

    # Filter words that appear more than once.
    duplicates = {word: count for word, count in word_occurrences.items() if count > 1}

    assert not duplicates, f"Duplicate words found: {duplicates}"


def test_replacement_words_not_empty():
    reviewer = GrammarReviewer()
    for key, values in reviewer.replacements.items():
        assert values, f"Replacement words for '{key}' should not be empty"


def test_replacement_words_are_strings():
    reviewer = GrammarReviewer()
    for key, values in reviewer.replacements.items():
        for value in values:
            assert isinstance(
                value, str
            ), f"Replacement word '{value}' for '{key}' is not a string"


def test_replacement_keys_are_strings():
    reviewer = GrammarReviewer()
    for key in reviewer.replacements.keys():
        assert isinstance(key, str), f"Replacement key '{key}' is not a string"


def test_replacement_values_are_lists():
    reviewer = GrammarReviewer()
    for values in reviewer.replacements.values():
        assert isinstance(values, list), f"Replacement values '{values}' are not a list"


def test_review_text_with_key():
    reviewer = GrammarReviewer()
    text = "Please access the system."
    suggestions = reviewer.review_text(text)
    # 'access' should be replaced with its options (excluding 'access' itself)
    assert "access" in suggestions
    assert suggestions["access"] == [
        v for v in reviewer.replacements["access"] if v != "access"
    ]


def test_review_text_with_value():
    reviewer = GrammarReviewer()
    text = "Please entry the system."
    suggestions = reviewer.review_text(text)
    # When a word from a replacement list is found, suggestions should include the key followed by the other options.
    # 'entry' appears in the list for 'access'
    expected = ["access"] + [v for v in reviewer.replacements["access"] if v != "entry"]
    assert "entry" in suggestions
    assert suggestions["entry"] == expected
