import random


def logical_operations():
    numbers = [1, 2, 3, 4, 5]
    print(f"\n{any([0, 0, 1, 0])=}")
    print(f"{any([0, 0, 0, 0])=}")
    print(f"{any({'a': 0, 'b': 0, 'c': 1}.values())=}")
    print(f"{any(n > 3 for n in numbers)=}")
    print(f"\n{all([1, 1, 1, 1])=}")
    print(f"{all([1, 0, 1, 1])=}")
    print(f"{all({'a': 1, 'b': 1, 'c': 1}.values())=}")
    print(f"{all(n > 0 for n in numbers)=}")


def type_checking():
    class Animal:
        pass

    class Dog(Animal):
        pass

    dog = Dog()
    print(f"\n{isinstance(dog, Dog)=}")
    print(f"{isinstance(dog, Animal)=}")
    print(f"{issubclass(Dog, Animal)=}")
    print(f"{issubclass(Animal, Dog)=}")


def object_attributes():
    class Person:
        def __init__(self, name):
            self.name = name

    person = Person("Alice")
    print(f"\n{hasattr(person, 'name')=}")
    print(f"{getattr(person, 'name')=}")
    setattr(person, "age", 30)
    print(f"{getattr(person, 'age')=}")
    delattr(person, "age")
    print(f"{hasattr(person, 'age')=}")


def sequence_operations():
    numbers = [1, 2, 3, 4, 5]
    print(f"\n{len(numbers)=}")
    print(f"{sorted(numbers, reverse=True)=}")


def disjointed_sets():
    set_a = set(random.randint(1, 9) for _ in range(3))
    set_b = set(random.randint(1, 9) for _ in range(3))
    set_c = set(random.randint(1, 9) for _ in range(3))

    print(f"\n{set_a=}")
    print(f"{set_b=}")
    print(f"{set_c=}")
    print(f"\n{set_a.isdisjoint(set_b)=}")
    print(f"{set_a.isdisjoint(set_c)=}")
    print(f"{set_b.isdisjoint(set_c)=}")


def enumerate_operations():
    employees = ["Alex", "Blake", "Chris", "Dylan"]
    random.shuffle(employees)
    print(f"\n{employees=}")
    print([f"{index=}, {item=}" for index, item in enumerate(employees)])


def zip_lists():
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    print(f"\n{list(zip(list1, list2))=}")


def reverse_sequences():
    number_sequence = [1, 2, 3, 4]
    string_sequence = "hello"
    print(f"\n{list(reversed(number_sequence))=}")
    print(f"{list(reversed(string_sequence))=}")


def sorted_operations():
    random_numbers = [random.randint(1, 9) for _ in range(6)]
    print(f"\n{random_numbers=}")
    print(f"{sorted(random_numbers)=}")


if __name__ == "__main__":
    logical_operations()
    type_checking()
    object_attributes()
    sequence_operations()
    disjointed_sets()
    enumerate_operations()
    zip_lists()
    reverse_sequences()
    sorted_operations()
