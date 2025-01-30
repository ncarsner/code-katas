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