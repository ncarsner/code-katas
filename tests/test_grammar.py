from collections import defaultdict
from utilities.grammar_reviewer import GrammarReviewer


def test_no_duplicate_replacement_words():
    reviewer = GrammarReviewer()
    duplicates = defaultdict(list)
    for key, values in reviewer.replacements.items():
        seen = set()
        for value in values:
            if value in seen:
                duplicates[key].append(value)
            else:
                seen.add(value)

    assert not duplicates, f"Duplicate replacement words found: {dict(duplicates)}"


def test_replacement_words_not_empty():
    reviewer = GrammarReviewer()
    for key, values in reviewer.replacements.items():
        assert values, f"Replacement words for '{key}' should not be empty"


def test_replacement_words_are_strings():
    reviewer = GrammarReviewer()
    for key, values in reviewer.replacements.items():
        for value in values:
            assert isinstance(value, str), f"Replacement word '{value}' for '{key}' is not a string"


def test_replacement_keys_are_strings():
    reviewer = GrammarReviewer()
    for key in reviewer.replacements.keys():
        assert isinstance(key, str), f"Replacement key '{key}' is not a string"


def test_replacement_values_are_lists():
    reviewer = GrammarReviewer()
    for values in reviewer.replacements.values():
        assert isinstance(values, list), f"Replacement values '{values}' are not a list"
