from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
import string

# In Python 2, division of integers results in integer division
# With the division import from __future__, it results in true division
print("True division (5 / 2):", 5 / 2)  # Outputs 2.5


# In Python 2, print is a statement, not a function
# With the print_function import from __future__, it behaves like a function
print("Hello, World!")  # Outputs Hello, World!

# In Python 2, string literals are ASCII by default
# With the unicode_literals import from __future__, string literals are Unicode by default
s = "Hello, Unicode!"
print("Unicode string:", s)  # Outputs Hello, Unicode!
print("Type of string:", type(s))  # Outputs <type 'unicode'>


# In Python 2, imports are relative by default
# With the absolute_import import from __future__, imports are absolute by default
# This means that 'import string' will always import the standard library string module,
# and not a local module named string.py

# Assuming there is a local module named string.py, this will still import the standard library string module
print("Standard library string module:", string.__name__)  # Outputs 'string'

# In Python 2, nested scopes are not enabled by default
# With the nested_scopes import from __future__, nested scopes are enabled


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_five = outer_function(5)
print("Nested scopes result (5 + 3):", add_five(3))  # Outputs 8
