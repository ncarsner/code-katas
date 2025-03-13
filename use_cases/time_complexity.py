import collections
import time
from functools import wraps
import pandas as pd


def time_complexity(func):
    """Measures execution time, not time complexity in Big O time."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result

    return wrapper


def calculate_word_frequency_pure_python(text: str) -> dict[str, int]:
    word_freq = {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq


@time_complexity
def count_word_frequency_pure_python(text: str) -> dict[str, int]:
    word_freq = calculate_word_frequency_pure_python(text)
    return dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True)[:10])


@time_complexity
def count_word_frequency_builtin(text: str) -> dict[str, int]:
    words = text.lower().split()
    return dict(collections.Counter(words).most_common(10))


@time_complexity
def count_word_frequency_pandas(text: str) -> dict[str, int]:
    words = pd.Series(text.lower().split())
    word_freq = words.value_counts()
    return word_freq.head(10).to_dict()


if __name__ == "__main__":
    with open("example_lorem.txt", "r") as file:
        text = file.read()
    if text is None:
        text = "This is a sample text with several words. This text is just a sample."
    print(count_word_frequency_pure_python(text))
    print(count_word_frequency_builtin(text))
    print(count_word_frequency_pandas(text))
