import random


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: Invalid input type. {e}")
        return None
    else:
        return result


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = file.read()
            return data
    except FileNotFoundError as e:
        print(f"Error: File not found. {e}")
        return None
    except IOError as e:
        print(f"Error: IO error occurred. {e}")
        return None


def convert_to_int(value):
    try:
        return int(value)
    except ValueError as e:
        print(f"Error: Cannot convert to integer. {e}")
        return None


def perform_custom_function(func, *args, **kwargs):
    try:
        result = func(*args, **kwargs)
        return result
    except Exception as e:
        print(f"Error: occurred while performing the custom function. {e}")
        return None


a = random.randint(1, 10)
b = random.randint(1, 10)

print(divide_numbers(a, b))
print(divide_numbers(random.choice([a, b]), 0))  # handles division by zero
print(divide_numbers(random.choice([a, b]), "a"))  # handles type error

file_path = "example.txt"
file_content = read_file(file_path)  # handles file not found
if file_content:
    print(file_content)

print(convert_to_int("123"))  # prints: 123
print(convert_to_int("abc"))  # handles value error

custom_function = lambda x, y: x + y
print(perform_custom_function(custom_function, a, b))


# Custom function with error
def faulty_function(x):
    return x / 0


print(perform_custom_function(faulty_function, 5))  # handles the division by zero error
