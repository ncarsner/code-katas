import random
import string

words = ["banana", "pie", "id", "book", "mushroom", "pineapple", "moth", "Godzilla"]
numbers = [random.randint(1, 20) for _ in range(5)]
letters = random.choices(string.ascii_lowercase, k=5)


def logical_operations():
    global numbers
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
    global numbers
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
    global letters
    list1 = sorted(list(set(letters)))
    list2 = [i for i in range(len(letters))]
    print(f"\n{list(zip(list1, list2))=}")


def zip_strict_example():
    list1 = list(set(random.randint(1, 9) for _ in range(10)))
    list2 = list(set(random.choices(string.ascii_lowercase, k=10)))
    try:
        result = list(zip(list1, list2, strict=True))
        print(f"\nZip strict: {result=}")
    except ValueError as e:
        print(f"\nException: {e}")


def reverse_sequences():
    global numbers
    number_sequence = numbers
    string_sequence = "hello"
    print(f"\n{list(reversed(number_sequence))=}")
    print(f"{list(reversed(string_sequence))=}")


def sorted_operations():
    random_numbers = [random.randint(1, 9) for _ in range(6)]
    print(f"\n{random_numbers=}")
    print(f"{sorted(random_numbers)=}")


def key_keyword_usage():
    global words
    numbers = [random.randint(1, 100) for _ in range(5)]
    y = random.randint(2, 10)

    print(f"\n{numbers=}, {y=}")
    print(f"{sorted(words, key=len, reverse=True)=}")
    print(f"{sorted(numbers, key=lambda x: x % y)=}")
    print(f"{max(words, key=len)=}")
    print(f"{min(numbers, key=lambda x: x % y)=}")


def map_function_examples():
    global numbers
    squared_numbers = list(map(lambda x: f"{x**2:,}", numbers))
    print(f"\n{numbers=}")
    print(f"{squared_numbers=}")

    global words
    words = random.sample(words, 4)
    uppercased_words = list(map(str.upper, words))
    print(f"\n{words=}")
    print(f"{uppercased_words=}")

    lengths = list(map(len, words))
    print(f"{lengths=}")


if __name__ == "__main__":
    logical_operations()
    type_checking()
    object_attributes()
    sequence_operations()
    disjointed_sets()
    enumerate_operations()
    zip_lists()
    zip_strict_example()
    reverse_sequences()
    sorted_operations()
    key_keyword_usage()
    map_function_examples()
