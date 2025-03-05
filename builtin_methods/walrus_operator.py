import re

# Example 1: Using the Walrus operator in a while loop
numbers = [1, 2, 3, 4, 5]
i = 0
while (n := len(numbers)) > 0:
    print(f"Length of list: {n}")
    numbers.pop()
    i += 1


# Example 2: Using the Walrus operator in an if statement
text = "Hello, world!"
if (n := len(text)) > 10:
    print(f"The text is quite long: {n} characters")


# Example 3: Using the Walrus operator in a list comprehension
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data = [x for x in data if (x_squared := x**2) > 20]
print(f"Filtered data: {filtered_data}")


# Example 4: Using the Walrus operator in a for loop
for i in range(10):
    if (square := i**2) % 2 == 0:
        print(f"The square of {i} is even: {square}")


# Example 5: Using the Walrus operator to simplify code
pattern = re.compile(r"\d+")
text = "The year is 2024, not 2023 or 1999."
if match := pattern.search(text):  # find one match
    print(f"Found a match: {match.group(0)}")
if matches := pattern.findall(text):  # find all matches
    for match in matches:
        print(f"Found a match: {match}")
