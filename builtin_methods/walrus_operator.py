import random
import re
from datetime import datetime


# Using the Walrus operator in a while loop
numbers = [*(range(5))]
while (n := len(numbers)) > 0:
    print(f"Length of list: {n}")
    numbers.pop()

# Using the Walrus operator in an if statement
text = random.choice(
    ["Hello, world!", "Can't stop the feeling", "Right here", "Good day!"]
)
if (n := len(text)) > 10:
    print(f"\nThe text is quite long: {n} characters")


# Using the Walrus operator in a list comprehension
data = [random.randint(1, 10) for _ in range(10)]
filtered_data = [x for x in data if (x_squared := x**2) > 20]
print(f"\nFiltered data: {filtered_data}\n")


# Using the Walrus operator to find the first name longer than a random length
students = ["Alex", "Blake", "Cameron", "Dillon", "Elliott", "Frederico", "Genevieve"]
length = random.randint(3, 10)

if any(len(first := i) > length for i in students):
    print(f"First name longer than {length} characters: {first}\n")
else:
    print(f"No names longer than {length} characters found.\n")


# Using the Walrus operator in a for loop
a = random.randint(3, 20)
b = random.randint(3, 20)
print(f"{a=} {b=}")
for i in range(1, 20):
    if (cube := i**3) % a == 0 and i % b != 0: # root divisibility, cubed divisibility
        print(f"The cube of {i} is {cube:,}")


# Using the Walrus operator to simplify code
pattern = re.compile(r"\d+")
current_year = datetime.today().year
years = random.sample([*(range(current_year - 30, current_year - 1))], k=2)
text = f"The year is {current_year}, not {years[0]} nor {years[1]}."

print(f"\n{text}")
if match := pattern.search(text):  # one match
    print(f"\nFound a match: {match.group(0)}")
if matches := pattern.findall(text):  # all matches
    print(f"\nFound matches: {matches}")

