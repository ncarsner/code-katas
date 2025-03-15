import functools
import operator
import random
import json

# functools.reduce(function, iterable[, initializer])
# Applies function of two arguments cumulatively to the items of iterable,
# from left to right, so as to reduce the iterable to a single value.
""" Usage: Imagine you want to find the product of all numbers in a list.
    Instead of writing a loop, you can use reduce with a multiplication function."""


def multiply_numbers(*numbers):
    nums = [i for i in numbers]
    return functools.reduce(lambda x, y: x * y, nums)


numbers = [random.randint(1, 10) for _ in range(5)]
result = functools.reduce(operator.mul, numbers)
print(result)

print(multiply_numbers(random.randint(1, 10) for _ in range(4)))


# functools.partial(func, /, *args, **keywords)
# Returns a new function with partial application of the given arguments and keywords.
""" Usage: Let's say you have a function that calculates the commission for a sale based on a percentage
    and the sale amount. If your company uses a standard commission rate, you can create a new function
    with that rate pre-filled using partial."""


def commission(percentage, amount):
    return percentage / 100 * amount


standard_commission = functools.partial(commission, 10)
print(standard_commission(500))  # Output: 50.0


# functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
# A decorator to update a wrapper function to look more like the original wrapped function.
""" Usage: When creating decorators, wraps can be used to ensure that the metadata of the original
    function is preserved. This is useful, for instance, when generating documentation or debugging. """


def my_decorator(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        print("Before calling the function")
        result = f(*args, **kwargs)
        print("After calling the function")
        return result

    return decorated


@my_decorator
def say_hello(name):
    """Says hello to a given name."""
    print(f"Hello, {name}!")


print(say_hello.__name__)  # Output: say_hello
print(say_hello.__doc__)  # Output: Says hello to a given name.


# functools.lru_cache(maxsize=128, typed=False)
# Decorator to wrap a function with a memoizing callable that saves up to the maxsize most recent calls.
""" Usage: When you have functions that are expensive to compute and are called multiple times with the same
    arguments (e.g., recursive functions, database queries), using lru_cache can significantly speed up code
    by caching the results. """


@functools.lru_cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Output: 55


# functools.cached_property(func)
# Transform an attribute of an instance into a property whose value is computed the first time it is accessed and then cached as a regular attribute for the subsequent calls.
""" Usage: Useful for expensive computations in classes that should only be computed once.
    For instance, when fetching data for a report in a BI tool. """


class Report:
    def __init__(self, data_source):
        self.data_source = data_source

    @functools.cached_property
    def processed_data(self):
        # Expensive processing goes here
        return self.data_source


my_data = "sample data"
report = Report(my_data)
# The first time this is accessed, it's computed and then cached.
data = report.processed_data

#######################################

# functools.cmp_to_key(func)
# Converts a comparison function to a key function to be used in sorting algorithms.
""" Usage: Consider a list of strings representing integers. You want to sort them not alphabetically,
    but numerically. Traditional sorting methods might not work as expected because they sort string
    representations. cmp_to_key can be used to convert a comparison function into a key function for
    sorting. """


def compare_items(x, y):
    return int(x) - int(y)


data = ["5", "100", "15", "2"]
sorted_data = sorted(data, key=functools.cmp_to_key(compare_items))
print(sorted_data)

# functools.total_ordering
# Class decorator that fills in missing ordering methods.
""" Usage: When creating a class that represents a version, and you implement just one or two comparison methods,
    total_ordering can automatically provide the rest of them. This is particularly useful in cases where objects
    need to be sorted or compared frequently, and you want to ensure consistency across different types of comparisons. """


@functools.total_ordering
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)


v1 = Version(1, 2)
v2 = Version(2, 1)
print(v1 < v2)  # Output: True
print(v1 > v2)  # Output: False
print(v1 <= v2)  # Output: True
print(v1 >= v2)  # Output: False
print(v1 == v2)  # Output: False

# functools.singledispatch
# Transforms a function into a single-dispatch generic function.
""" Usage: In a scenario where you need to process data differently based on its type
    (e.g., rendering data to JSON in a web application), singledispatch allows you to
    create a generic function that dispatches to type-specific implementations. """


@functools.singledispatch
def to_json(val):
    raise NotImplementedError("Unsupported type")


@to_json.register
def _(val: dict):
    return json.dumps(val)


@to_json.register
def _(val: list):
    return json.dumps(val)


@to_json.register
def _(val: int):
    return str(val)


print(to_json({"name": "John", "age": 30}))
print(to_json([random.randint(1, 10) for _ in range(4)]))
print(to_json(random.randint(1, 50)))


def add_up_numbers(*numbers):
    return sum(numbers)


print(add_up_numbers(*[random.randint(1, 10) for _ in range(4)]))
