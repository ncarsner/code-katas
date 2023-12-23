"""
GOAL: Scramble a string, word by word, and return a single output string
in the manner in which it was ingested. 
"""

import random

my_string = "this text string was obfuscated"


def text_shuffle(text_string):
    shuffled_words = [
        "".join(random.sample(word, len(word))) for word in text_string.split()
    ]
    return " ".join(shuffled_words)


# SAMPLE OUTPUT:
print(text_shuffle(my_string))  # 'tshi xtte nitsgr was cusbteodfa'
