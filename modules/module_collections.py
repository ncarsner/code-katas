import collections

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

fruits = ["apple", "banana", "apple", "orange", "banana", "apple", "grapefruit", "cherries", "apple"]
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
