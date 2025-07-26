import random
import re

# Using the Walrus operator in a while loop
numbers = [1, 2, 3, 4, 5]
i = 0
while (n := len(numbers)) > 0:
    print(f"Length of list: {n}")
    numbers.pop()
    i += 1

# Using the Walrus operator in an if statement
text = "Hello, world!"
if (n := len(text)) > 10:
    print(f"\nThe text is quite long: {n} characters")


# Using the Walrus operator in a list comprehension
data = [random.randint(1, 10) for _ in range(10)]
filtered_data = [x for x in data if (x_squared := x**2) > 20]
print(f"\nFiltered data: {filtered_data}\n")

students = ["Alex", "Blake", "Chris", "Dillon", "Elliott", "Flynn", "Genevieve"]
length = random.randint(4, 10)

# Using the Walrus operator to find the first name longer than a random length
if any(len(first := i) > length for i in students):
    print(f"First name with more than {length} characters: {first}\n")
else:
    print(f"No names longer than {length} characters found.\n")


# Using the Walrus operator in a for loop
for i in range(10):
    if (square := i**2) % 2 == 0:
        print(f"The square of {i} is even: {square}")


# Using the Walrus operator to simplify code
pattern = re.compile(r"\d+")
text = "The year is 2024, not 2023 or 1999."
if match := pattern.search(text):  # find one match
    print(f"\nFound a match: {match.group(0)}\n")
if matches := pattern.findall(text):  # find all matches
    for match in matches:
        print(f"Found a match: {match}")
