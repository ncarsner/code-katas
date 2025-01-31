title_str = " This Is A Title "
"""
Joining and Splitting Methods:
- split(sep=None): Splits the string into a list using the specified separator.
- join(iterable): Joins elements of an iterable with the string as a separator.

Line Splitting Methods:
- splitlines(keepends=False): Splits the string at line breaks.

Partitioning Methods:
- partition(sep): Splits the string at the first occurrence of the separator.
- rpartition(sep): Splits the string at the last occurrence of the separator.
"""

### Joining and splitting
print("This is a title".split())  # ['This', 'is', 'a', 'title']
print(" ".join(["This", "is", "a", "title"]))  # This is a title

### Line splitting
multiline_str = "This\nIs\nA\nTitle"
print(multiline_str.splitlines())  # ['This', 'Is', 'A', 'Title']

### Partitioning
print(title_str.partition("Is"))  # ('This ', 'Is', ' A Title')
print(title_str.rpartition("Is"))  # ('This ', 'Is', ' A Title')
