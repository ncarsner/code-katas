# Logical operations
def logical_operations():
    """
    Demonstrates the use of any() and all() functions.
    """
    numbers = [1, 2, 3, 4, 5]
    print(any(n > 3 for n in numbers))  # True: some numbers are greater than 3
    print(all(n > 0 for n in numbers))  # True: all numbers are greater than 0

# Type checking
def type_checking():
    """
    Demonstrates the use of isinstance() and issubclass() functions.
    """
    class Animal:
        pass

    class Dog(Animal):
        pass

    dog = Dog()
    print(isinstance(dog, Dog))         # True, because dog is an instance of Dog
    print(isinstance(dog, Animal))      # True, because dog is an instance of Animal
    print(issubclass(Dog, Animal))      # True, because Dog is a subclass of Animal

# Object attributes
def object_attributes():
    """
    Demonstrates the use of hasattr(), getattr(), setattr(), and delattr() functions.
    """
    class Person:
        def __init__(self, name):
            self.name = name

    person = Person("Alice")
    print(hasattr(person, 'name'))      # True, because person has an attribute 'name'
    print(getattr(person, 'name'))      # Alice, gets the value of 'name' attribute
    setattr(person, 'age', 30)          # Sets a new attribute 'age' to 30
    print(getattr(person, 'age'))       # 30, gets the value of 'age' attribute
    delattr(person, 'age')              # Deletes the 'age' attribute
    print(hasattr(person, 'age'))       # False, because 'age' attribute has been deleted


# Sequence operations
def sequence_operations():
    numbers = [1, 2, 3, 4, 5]
    print(len(numbers))                 # 5, length of the list
    print(sorted(numbers, reverse=True))# [5, 4, 3, 2, 1], sorted list in descending order

if __name__ == "__main__":
    logical_operations()
    type_checking()
    object_attributes()
    sequence_operations()
