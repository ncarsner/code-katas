from collections import Counter
import random
from timeit import timeit


def is_anagram(word1: str, word2: str) -> bool:
    """Check if two words are anagrams using Counter."""
    return Counter(word1) == Counter(word2)


def is_anagram_counter(word1: str, word2: str) -> bool:
    """Check if two words are anagrams using Counter."""
    return Counter(word1.lower()) == Counter(word2.lower())


if __name__ == "__main__":
    words = ["listen", "silent", "enlist", "inlets", "tinsel"]
    words = ["stale", "steal", "teals", "tales", "least"]
    words = ["evil", "vile", "live", "lives", "veil"]
    words = ["astronomer", "moon", "starer", "angers", "anglers", "rangels"]
    words = ["conversation", "misanthrope", "agoraphone", "conservation", "conversational"]

    for word in words:
        print(f"{word} is an anagram of listen: {is_anagram('listen', word)}")
    word1 = random.choice(words)
    word2 = random.choice(words)

    # Measure the time taken by the anagram function
    time_taken = timeit(lambda: is_anagram(word1, word2), number=100000)
    print(f"Time taken for is_anagram: {time_taken:.6f} seconds")

    time_taken_counter = timeit(lambda: is_anagram_counter(word1, word2), number=100000)
    print(f"Time taken for is_anagram_counter: {time_taken_counter:.6f} seconds")
