import sys
import tracemalloc


class Person:
    __slots__ = ["name", "age", "gender"]

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, gender={self.gender})"


class PersonWithoutSlots:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


person = Person("Alice", 30, "Female")
print(person)

# Trying to add a new attribute that is not in __slots__ will raise an AttributeError
try:
    person.address = "123 Main St"
except AttributeError as e:
    print(e)

# Creating instances of both classes
person_with_slots = Person("Bob", 25, "Male")
person_without_slots = PersonWithoutSlots("Bob", 25, "Male")

# Checking memory usage
print(f"\nMemory usage with __slots__: {sys.getsizeof(person_with_slots)} bytes")
print(f"Memory usage without __slots__: {sys.getsizeof(person_without_slots)} bytes")

# Demonstrating that __slots__ restricts dynamic attribute assignment
try:
    person_with_slots.hobby = "Reading"
except AttributeError as e:
    print(f"Error: {e}")

# Demonstrating that a class without __slots__ allows dynamic attribute assignment
person_without_slots.hobby = "Reading"
print(f"\nPersonWithoutSlots hobby: {person_without_slots.hobby}")

# Start tracing memory allocations
tracemalloc.start()

# Create instances of both classes with more attributes
person_with_slots = Person("Charlie", 40, "Male")
try:
    person_with_slots.job = "Engineer"
except AttributeError as e:
    print(f"Error: {e}")

person_without_slots = PersonWithoutSlots("Charlie", 40, "Male")
person_without_slots.job = "Engineer"

# Check memory usage
snapshot1 = tracemalloc.take_snapshot()
print(f"Memory usage with __slots__: {sys.getsizeof(person_with_slots)} bytes")
print(f"Memory usage without __slots__: {sys.getsizeof(person_without_slots)} bytes")

# Add more attributes to PersonWithoutSlots
person_without_slots.address = "456 Elm St"
person_without_slots.phone = "555-1234"

# Check memory usage again
snapshot2 = tracemalloc.take_snapshot()
print(f"Memory usage with: {sys.getsizeof(person_with_slots)} bytes")
print(f"Memory usage without, adding more attrs: {sys.getsizeof(person_without_slots)} bytes")

# Display memory usage difference
stats = snapshot2.compare_to(snapshot1, "lineno")
for stat in stats[:10]:
    print(stat)
