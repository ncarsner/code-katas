import random

"""
Conversion methods:
- abs(): Returns the absolute value of a number.
- divmod()    # Returns a tuple of quotient and remainder
- round()     # Rounds a number to a specified number of decimal places
- complex()   # Creates a complex number
- float()     # Converts a number or string to a floating point number
- int()       # Converts a number or string to an integer

Mathematical functions:
- max()       # Returns the largest of the input values
- min()       # Returns the smallest of the input values
- pow()       # Returns the value of a number raised to the power of another number
- sum()       # Sums the items of an iterable

Validation functions:
- isinstance()    # Checks if an object is an instance of a specified class
- issubclass()    # Checks if a class is a subclass of another class

Additional numerical methods:
- bin()       # Converts an integer to a binary string
- hex()       # Converts an integer to a hexadecimal string
- oct()       # Converts an integer to an octal string
"""

# Generate random values for each example
random_int = random.randint(-100, 100)
random_float = random.uniform(-100.0, 100.0)
random_complex = complex(random.uniform(-100.0, 100.0), random.uniform(-100.0, 100.0))
random_str_int = str(random.randint(-100, 100))
random_str_float = str(random.uniform(-100.0, 100.0))
random_list = [random.randint(1, 10) for _ in range(3)]
random_bool = random.choice([True, False])
random_base_int = random.randint(0, 255)

# Conversion methods with random values
print(f"{abs(random_int)=}")
print(f"{divmod(random_int, random.randint(1, 10))=}")
print(f"{round(random_float, random.randint(0, 5))=}")
print(f"{complex(random_float, random_float)=}")
print(f"{float(random_str_float)=}")
print(f"{int(random_str_int)=}")

# Mathematical functions with random values
print(f"\n{max(*random_list)=}")
print(f"{min(*random_list)=}")
print(f"{pow(random.randint(1, 10), random.randint(1, 5))=}")
print(f"{sum(random_list)=}")

# Validation functions with random values
print(f"\n{isinstance(random_int, int)=}")
print(f"{issubclass(bool, int)=}")

# Additional built-in functions for numerical operations with random values
print(f"\n{bin(random_base_int)=}")
print(f"{hex(random_base_int)=}")
print(f"{oct(random_base_int)=}")
