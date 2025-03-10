import string
import random

# Generate a random string of letters
random_string = "".join(random.choices(string.ascii_letters, k=20))
print(f"Random String: {random_string}")

# Slicing examples
print(f"First 5 characters: {random_string[:5]}")
print(f"Last 5 characters: {random_string[-5:]}")
print(f"Characters from index 5 to 10: {random_string[5:10]}")
print(f"Every second character: {random_string[::2]}")
print(f"Reversed string: {random_string[::-1]}")
print(f"Characters from index 2 to 8 with step 2: {random_string[2:8:2]}")

students = ["Alex", "Blake", "Chris", "Dylan", "Elliott"]
print(f"First student: {students[0]}")
print(f"Last student: {students[-1]}")
print(f"Students from index 1 to 3: {students[1:4]}")
print(f"Every second student: {students[::2]}")
print(f"Reversed students: {students[::-1]}")
print(f"Students from index 0 to 4 with step 2: {students[0:5:2]}")
print(f"Students from index 4 to 0 with step -1: {students[4::-1]}")

first, *_, last = students
print(f"First and Last students: {first}, {last}")
