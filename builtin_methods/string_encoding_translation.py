import string

title_str = " This Is A Title "
"""
Encoding and Decoding Methods:
- encode(encoding='utf-8', errors='strict'): Encodes the string using the specified encoding.

Translation Methods:
- translate(table): Translates the string using a translation table.
- maketrans(x, y=None, z=None): Creates a translation table for use with translate().
"""

### Encoding and decoding
encoded_str = title_str.encode("utf-16")
print(encoded_str)
print(title_str.encode())  # b'This Is A Title' -- default is UTF-8
print(encoded_str.decode("utf-16"))  # This Is A Title

### Translation
trans_table = str.maketrans("Title", "12345")
print(trans_table)
print(title_str.translate(trans_table))
trans_table = str.maketrans("title", "12345")
print(title_str.translate(trans_table))


# Removing punctuation from a string
sample_str = "Hello, World! This is an example."
remove_punct_table = str.maketrans("", "", string.punctuation)
clean_str = sample_str.translate(remove_punct_table)
print(clean_str)  # Hello World This is an example
