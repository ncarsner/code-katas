"""A list of unconventional use case or abstract concepts, according to the author."""

import random

"""
Output of the implicit empty None type object - i.e. [None, None, None] - may differ when executing in an interactive environment (Jupyter notebook, Debug console) vs. executing in a script.
"""

list_of_numbers = [random.randint(1, 20) for _ in range(random.randint(5, 10))]

# Returns iterated objects in list, AND list of None types
lambda_in_list = lambda object: [print(x) for x in object]
# Returns iterated objects in list, AND list of None types
lambda_in_list_or_none = lambda object: [print(i) for i in object] or None
# Returns only iterated objects in list
lambda_in_list_and_none = lambda object: [print(i) for i in object] and None
# Returns only iterated objects in list
lambda_list_list_explicit_empty = lambda object: (print(*object, sep="\n"))

# Returns generator object
lambda_in_tuple = lambda object: (print(x) for x in object)
# Returns generator object
lambda_in_tuple_or_none = lambda object: (print(x) for x in object) or None
# Returns nothing
lambda_in_tuple_and_none = lambda object: (print(x) for x in object) and None


lambda_in_list(list_of_numbers)
# lambda_in_list_or_none(list_of_numbers)
# lambda_in_list_and_none(list_of_numbers)
# lambda_list_list_explicit_empty(list_of_numbers)

# lambda_in_tuple(list_of_numbers)
# lambda_in_tuple_or_none(list_of_numbers)
# lambda_in_tuple_and_none(list_of_numbers)
