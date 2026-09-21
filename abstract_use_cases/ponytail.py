"""A module of abstract one-liners written in Python"""

import random

WORDS = ["bus", "hex", "buzz", "church", "bush"]

# Pluralize a word, approximately
plural = lambda w: w + ("es" if w.endswith(("s", "x", "z", "ch", "sh")) else "s")

# Clamp between lo and hi
clamp = lambda x, lo, hi: max(lo, min(x, hi))

# Pick singular/plural
items = lambda n: f"{n} item{'s' * (n != 1)}"

# Get the sign of a number
sign = lambda x: (x > 0) - (x < 0)

# Flatten one level of nesting
flatten = lambda lst: sum(lst, [])

# Get the most common item
mode = lambda xs: max(set(xs), key=xs.count)

# Fibonacci numbers via recursion
fib = lambda n: round(((1 + 5**0.5) / 2) ** n / 5**0.5)

# Convert a number to odd or even
parity = lambda n: ("even", "odd")[n & 1]

# Convert seconds to HH:MM:SS
hms = lambda s: f"{s // 3600:02}:{(s % 3600) // 60:02}:{s % 60:02}"

# FizzBuzz
fizzbuzz = lambda n: "Fizz" * (n % 3 == 0) + "Buzz" * (n % 5 == 0) or str(n)

if __name__ == "__main__":
    word = random.choice(WORDS)
    number = random.randint(1, 15)

    print(f"Plural of {word}:", plural(word))
    print(f"Clamp {number} between 1 and 10:", clamp(number, 1, 10))
    print(f"{number} items:", items(number))

    rand_num = random.randint(-number, number)
    print(f"Sign of {rand_num}:", sign(rand_num))

    nested_list = [[1, 2], [3, 4], [5]]
    print("Flattened list:", flatten(nested_list))

    items_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
    print("Most common item:", mode(items_list))

    print(f"Fibonacci of {number}:", fib(number))

    print(f"Parity of {number}:", parity(number))

    time = random.randint(0, 86400)  # Random number of seconds in a day
    print(f"{time} seconds:", hms(time))

    print(f"FizzBuzz of {number}:", fizzbuzz(number))
