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

# Generate values
random_int = random.randint(-10, 10)
random_float = random.uniform(-10.0, 10.0)
random_complex = complex(random.uniform(-10.0, 10.0), random.uniform(-10.0, 10.0))
random_str_int = str(random.randint(-10, 10))
random_str_float = str(random.uniform(-10.0, 10.0))
random_list = [random.randint(1, 10) for _ in range(3)]
random_bool = random.choice([True, False])
random_base_int = random.randint(0, 255)

# Conversion methods
print(f"\n{abs(random_int)=}")
print(f"{divmod(random_int, random.randint(1, 10))=}")
print(f"{round(random_float, random.randint(0, 5))=}")
print(f"{complex(random_float, random_float)=}")
print(f"{float(random_str_float)=}")
print(f"{int(random_str_int)=}")

# Mathematical functions
print(f"\n{random_list=}, {max(*random_list)=}")
print(f"{random_list=}, {min(*random_list)=}")
a, b = random.randint(1, 10), random.randint(1, 5)
print(f"{a=}^{b=}, {pow(a, b)=:,}")
print(f"{sum(random_list)=:,}")

# Validation functions
print(f"\n{isinstance(random_int, int)=}")
print(f"{issubclass(bool, int)=}")

# Additional numerical operations
print(f"\n{random_base_int=}")
print(f"{bin(random_base_int)=}")
print(f"{hex(random_base_int)=}")
print(f"{oct(random_base_int)=}")

"""
Class methods for numeric data types:
- int.bit_length()    # Returns the number of bits required to represent an integer in binary
- int.to_bytes()      # Returns an array of bytes representing an integer
- int.from_bytes()    # Returns an integer from an array of bytes
- float.is_integer()  # Returns True if the float is an integer
- float.hex()         # Returns a hexadecimal string representing a float
- float.fromhex()     # Creates a float from a hexadecimal string
- complex.conjugate() # Returns the complex conjugate of a complex number
"""

print(f"\n{random_int=}")
print(f"{random_int.bit_length()=}")

byte_length = (random_int.bit_length() + 7) // 8  # bytes needed
random_int_bytes = random_int.to_bytes(byte_length, byteorder="big", signed=True)

print(f"{random_int_bytes=}")
print(f"{int.from_bytes(random_int_bytes, byteorder='big', signed=True)=}")

print(f"{random_float.is_integer()=}")

random_float_hex = random_float.hex()
print(f"\n{random_float_hex=}")
print(f"{float.fromhex(random_float_hex)=}")

print(f"{random_complex.conjugate()=}")
