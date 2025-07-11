import re
from difflib import SequenceMatcher
import json
import random

# Quantify: Find all words with 3 to 5 letters
text = "This is a simple text with some short and long words."
words = re.findall(r'\b\w{3,5}\b', text)
print("Words with 3 to 5 letters:", words)

# Extrapolate: Extract all email addresses from a text
text_with_emails = "Contact us at support@example.com or sales@example.org for more info."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text_with_emails)
print("Extracted emails:", emails)

# Replacing: Replace all occurrences of 'foo' with 'bar'
text_to_replace = "foo is a placeholder, foo should be replaced."
replaced_text = re.sub(r'\bfoo\b', 'bar', text_to_replace)
print("Replaced text:", replaced_text)


# Fuzzy matching logic: Find close matches to a word
def fuzzy_match(word, possibilities, threshold=0.6):
    matches = []
    for possibility in possibilities:
        ratio = SequenceMatcher(None, word, possibility).ratio()
        if ratio >= threshold:
            matches.append((possibility, ratio))
    return matches


if __name__ == "__main__":
    # Fuzzy match a word against a list of possibilities
    possibilities = [
        "samples", "examine", "exemplar", "simple", "examples", "example",
        "sampler", "simply", "sampled", "temple", "simile", "exampel",
        "expel", "exemplary", "exemplify", "dimple", "temple", "simpler"
    ]
    word_to_match = random.choice(possibilities)
    matches = fuzzy_match(word_to_match, possibilities, 0.7)
    print(f"Fuzzy matches for '{word_to_match}':")
    formatted_matches = [{"word": match[0], "percentage": f"{match[1] * 100:.1f}%"} for match in matches]
    print(json.dumps(formatted_matches, indent=4))