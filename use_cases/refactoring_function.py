"""
Create a function that returns how many ascii letters are in a given string.
A letter is defined as a character [A-Z] or [a-z]
"""

from string import ascii_letters as lets
from string import printable as chars
import random

from decorators import timer


@timer
def count_ascii_letters(text: str):
    # return sum(i for i in text if i.isalpha())
    return "".join([i for i in text if i in lets])


@timer
def count_ascii_lets(text: str) -> int:
    return sum(letter in lets for letter in text)
    # return "".join([letter for letter in text if letter in lets])


sample = "".join([random.choice(chars) for _ in range(100_000)])

# print(f"Sample: {sample}")
print(f"Length sample: {len(sample):,}\n")

# print(f"func1 value: {count_ascii_letters(sample)}")
print(f"Length func1: {len(count_ascii_letters(sample)):,}\n")


# print(f"func2 value: {count_ascii_lets(sample)}")
print(f"Length func2: {count_ascii_lets(sample):,}\n")
