import random


title_str = " This Is A Title "
"""
Padding and Alignment Methods:
- zfill(width): Pads the string with zeros on the left to fill the specified width.
- ljust(width, fillchar=' '): Left-justifies the string in a field of the specified width.
- rjust(width, fillchar=' '): Right-justifies the string in a field of the specified width.
- center(width, fillchar=' '): Centers the string in a field of the specified width.

Whitespace Methods:
- strip(): Removes leading and trailing whitespace.

Tab Expansion Methods:
- expandtabs(tabsize=8): Expands tabs in the string to spaces.

Formatting Methods:
- format(*args, **kwargs): Formats the string using the specified arguments.
- format_map(mapping): Formats the string using a mapping.
"""

### Padding and alignment
print(title_str.zfill(20))  # 000000This Is A Title
print(title_str.ljust(20, "-"))  # This Is A Title-----
print(title_str.rjust(20, "-"))  # -----This Is A Title
print(title_str.center(20, "-"))  # --This Is A Title--

### Whitespace methods
print(title_str.strip())  # This Is A Title

### Tab expansion
tab_str = "This\tis\ta\ttitle"
print(tab_str.expandtabs(4))  # This    is    a    title

### Formatting (legacy)
print("Format {}".format("this"))  # Format this
print("Format {key}".format_map({"key": "value", "foo": "bar"}))  # Format value


# Built-in format methods
number = random.uniform(1000, 2000)
print(f"\nDefault: {number}")
print(f"Fixed-point: {number:.2f}")
print(f"Scientific: {number:.2e}")
print(f"With commas: {number:,.2f}")
print(f"Hexadecimal: {int(number):x}")

random_float = random.uniform(0, 1)
print(f"\nRounded float: {random_float:.2f}")
print(f"Padded number: {number:010.2f}")  # Padded number: 0001234.57

random_int = random.randint(1, 100)
print(f"\nDecimal: {random_int:d}")
print(f"Character: {random_int:c}")
print(f"Floating-point: {random_int:f}")
print(f"Binary: {random_int:b}")
print(f"Octal: {random_int:o}")
print(f"Hex: {random_int:x}")
print(f"Percentage: {random_int/100:.1%}")