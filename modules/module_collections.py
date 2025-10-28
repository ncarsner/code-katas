import collections
import random
from datetime import datetime, timedelta
from pprint import pp

# namedtuple
Point = collections.namedtuple("Point", ["x", "y"])
p = Point(11, y=22)
print(p.x, p.y)

# deque
d = collections.deque(["task1", "task2", "task3"])
d.append("task4")
print("Deque after append:", d)
d.appendleft("task0")
print("Deque after appendleft:", d)
d.pop()
print("Deque after pop:", d)
d.popleft()
print("Deque after popleft:", d)

# Counter
counter = collections.Counter(["apple", "banana", "apple", "orange", "banana", "apple"])
print("Counter:", counter)
print("Most common:", counter.most_common(2))

fruits = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "grapefruit",
    "cherries",
    "apple",
]
counted_fruits = collections.Counter(fruits)
print(counted_fruits)

# defaultdict
dd = collections.defaultdict(int)
dd["apple"] += 1
dd["banana"] += 2
print("Defaultdict:", dd)

# OrderedDict
od = collections.OrderedDict()
od["apple"] = 1
od["banana"] = 2
od["orange"] = 3
print("OrderedDict:", od)

# ChainMap
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
chain = collections.ChainMap(dict1, dict2)
print("ChainMap:", chain)
print("Value for 'b':", chain["b"])


# UserDict
class MyDict(collections.UserDict):
    def __setitem__(self, key, value):
        if isinstance(key, str):
            super().__setitem__(key, value)
        else:
            raise TypeError("Keys must be strings")


my_dict = MyDict()
my_dict["key"] = "value"
print("UserDict:", my_dict)


# UserList
class MyList(collections.UserList):
    def append(self, item):
        if isinstance(item, int):
            super().append(item)
        else:
            raise TypeError("Items must be integers")


my_list = MyList([1, 2, 3])
my_list.append(4)
print("UserList:", my_list)


# UserString
class MyString(collections.UserString):
    def append(self, s):
        self.data += s


my_string = MyString("Hello")
my_string.append(" World")
print("UserString:", my_string)


"""Inheritance:

dict Inheritance: Inheriting from dict directly extends the built-in dictionary type, resulting in a class that behaves like a dictionary with any additional methods or overrides provided.

UserDict Inheritance: collections.UserDict is a wrapper around a standard dictionary that allows for easier subclassing. It is designed to be easier to extend and customize. It provides a dictionary-like interface but stores the actual data in a separate internal dictionary (self.data).

Both classes override the __setitem__ method to print a message when adding a new item to the dictionary.
The output will be the same for both classes, but the UserDict implementation is more flexible and easier to extend.

Courtesy of Bob Belderbos, a la Trey Hunner's article:
    https://treyhunner.com/2019/04/why-you-shouldnt-inherit-from-list-and-dict-in-python/
"""


class BirthdayDict(dict):
    def __setitem__(self, name, birthday):
        print(f"Adding {name}")
        super().__setitem__(name, birthday)


def random_birthday(min_age=18, max_age=55):
    """
    Generate a random birthday within a specified age range.

    This function calculates a random date between the current date minus the maximum age
    and the current date minus the minimum age. The resulting date is formatted as a string
    in the "YYYY-MM-DD" format.

    Args:
        min_age (int): The minimum age for the random birthday. Default is 18.
        max_age (int): The maximum age for the random birthday. Default is 55.

    Returns:
        str: A string representing the random birthday in "YYYY-MM-DD" format.
    """
    start_date = datetime.now() - timedelta(days=max_age * 365)
    end_date = datetime.now() - timedelta(days=min_age * 365)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%Y-%m-%d")


students = ["Alex", "Blake", "Chris", "Dylan", "Elliot"]

bd = BirthdayDict()
bd["Alex"] = random_birthday()

for student in students[1:]:
    bd.update({student: random_birthday()})  # dict method does not call __setitem__
    print(bd)


class BirthdayUserDict(collections.UserDict):
    def __setitem__(self, name, birthday):
        print(f"Adding {name}")
        super().__setitem__(name, birthday)


bd = BirthdayUserDict()
bd["Alex"] = random_birthday()

for student in students[1:]:
    bd.update({student: random_birthday()})  # UserDict method calls __setitem__
    print(bd)


# Grouping cities by state using defaultdict
city_state_list = [
    ("New York", "NY"),
    ("Los Angeles", "CA"),
    ("San Francisco", "CA"),
    ("Houston", "TX"),
    ("Dallas", "TX"),
    ("Buffalo", "NY"),
    ("Nashville", "TN"),
    ("Memphis", "TN"),
    ("Austin", "TX"),
]

results = collections.defaultdict(list)
for city, state in city_state_list:
    results[state].append(city)

print("Cities grouped by state (from list):")
pp(results)

# Grouping cities by state using a dictionary
city_state_dict = {
    "New York": "NY",
    "Los Angeles": "CA",
    "San Francisco": "CA",
    "Houston": "TX",
    "Dallas": "TX",
    "Buffalo": "NY",
    "Nashville": "TN",
}

results = collections.defaultdict(list)
for city, state in city_state_dict.items():
    results[state].append(city)

print("Cities grouped by state (from dict):")
pp(results)