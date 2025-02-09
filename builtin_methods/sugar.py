"""
Syntactic sugar refers to syntax within a programming language
that is designed to make things easier to read or to express.
It makes the code "sweeter" for human use.

Common examples of syntactic sugar in Python include:
1. List Comprehensions
2. Dictionary Comprehensions
3. Lambda Functions
4. Decorators
5. Context Managers
6. Unpacking Iterables
7. Attribute Calls
8. Method Calls
9. Assertions
10. f-string Literals
11. Chained Conditions
12. The yield from Construct
13. Ternary Operators
"""

import random
import string

chars = string.ascii_letters + string.digits
random_string = "".join(random.choices(chars, k=random.randint(5, 15)))

# 1. List Comprehensions
squares_sugar = [x**2 for x in range(10)]
print(f"{squares_sugar=}")

# 2. Dictionary Comprehensions
squares_dict_sugar = {x: x**2 for x in range(10)}
print(f"{squares_dict_sugar=}")

# 3. Lambda Functions
add_sugar = lambda x, y: x + y
x, y = random.randint(1, 10), random.randint(1, 10)
print(f"{add_sugar(x, y)=}")


# 4. Decorators
def make_pretty(func):
    def inner():
        print("I got decorated.")
        func()

    return inner


@make_pretty
def ordinary_sugar():
    print("I am from the function.")


ordinary_sugar()


# 5. Context Managers
with open("example.txt", "a") as file:
    line_break = "-" * 20
    file.write(f"\n{line_break}\n{random_string}")


# 6. Unpacking Iterables
my_list = [random.randint(1, 10) for _ in range(3)]
a, b, c = my_list
print(f"{a=}, {b=}, {c=}")


# 7. Attribute Calls
class MyClass:
    def __init__(self, value):
        self.value = value


obj = MyClass(10)
value_sugar = obj.value


# 8. Method Calls
class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


obj2 = MyClass(20)
value_sugar = obj2.get_value()


# 9. Assertions
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

test_sum()


# 10. f-string Literals
name = random.choice(["Alex", "Blake", "Chris", "Dylan", "Elliott"])
print(f"Hello, {name}")


# 11. Chained Conditions
x = random.randint(0, 20)
print("x is between 5 and 15") if 5 < x < 15 else print("x is outside range")


# 12. The yield from Construct
def generator():
    for i in range(5):
        yield i


def another_generator():
    yield from generator()


# Using the generator
for value in another_generator():
    print(value)


# 13. Ternary Operators
is_even = random.choice([True, False])
result_sugar = "Even" if is_even else "Odd"
print(f"{result_sugar=}")
