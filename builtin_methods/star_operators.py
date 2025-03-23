from typing import Any
import random


def sum_all(*args: int) -> int:
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))


def print_person_details(**kwargs: Any) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_person_details(name="John", age=30, city="New York")

person_details = {"name": "John", "age": 30, "city": "New York"}
print_person_details(**person_details)


def multiply(*args: int) -> int:
    result = 1
    for num in args:
        result *= num
    return result


print(multiply(1, 2, 3, 4))


def create_greeting(greeting: str, **kwargs: Any) -> str:
    return f"{greeting}, {kwargs.get('name', 'Guest')}!"


print(create_greeting("Hello", name="Alex"))
print(create_greeting("Welcome"))


def combined_example(*args: Any, **kwargs: Any) -> None:
    print("Args:", args)
    print("Kwargs:", kwargs)


combined_example(1, 2, 3, name="John", age=30)

# Using *args in a lambda function
sum_lambda = lambda *args: sum(args)
print(f"{sum_lambda(1, 2, 3, 4, 5)=}")

# Using **kwargs in a lambda function
greet_lambda = lambda **kwargs: f"Hello, {kwargs.get('name', 'Guest')}!"
print(greet_lambda(name="Alex"))
print(greet_lambda())

# Packing and unpacking in one-liners
numbers = [1, 2, 3, 4, 5]
print(sum([*(numbers)]))
print(sum([*(range(101))]))  # * unpacks range into a list


def display_info(name: str, age: int, city: str) -> str:
    return f"{name} is {age} years old and lives in {city}."


info_dict = {"name": "Alex", "age": 28, "city": "Wonderland"}
print(display_info(**info_dict))  # ** unpacks dictionary into a function call


# Merging objects using * operator
tuple1 = tuple([random.randint(1, 10) for _ in range(3)])
tuple2 = tuple([random.randint(1, 10) for _ in range(3)])
merged_tuple = (*tuple1, *tuple2)
print(f"{merged_tuple=}")

list1 = [random.randint(1, 10) for _ in range(3)]
list2 = [random.randint(1, 10) for _ in range(3)]
merged_list = [*list1, *list2]
print(f"{merged_list=}")

set1 = set(random.randint(1, 10) for _ in range(3))
set2 = set(random.randint(1, 10) for _ in range(3))
merged_set = {*set1, *set2}
print(f"{merged_set=}")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(f"{merged_dict=}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"{flattened=}")

# Unpacking a list into individual variables
numbers = [1, 2, 3]
a, b, c = numbers
print(f"{a=}, {b=}, {c=}")


# Unpacking a list into individual variables with a star operator
first, *rest = [1, 2, 3, 4, 5]
print(f"{first=}, {rest=}")

*start, last = [1, 2, 3, 4, 5]
print(f"{start=}, {last=}")


employees = ["Alex", "Blake", "Chris", "Dylan", "Elliott"]
nums = [random.randint(1, 20) for _ in range(5)]

print(*employees)
print(*sorted(nums))


def first_and_last(items: list) -> tuple:
    first, *_, last = items
    return first, last


items = [1, 2, 3, 4, 5]
print(first_and_last(items))

items = random.sample(range(1, 100), 10)
print(f"{items=}")
print(first_and_last(items))
print(first_and_last(sorted(items)))
