from random import choice


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "makes the sound"


class Dog(Animal):
    def __init__(self, name, breed):
        # Call the __init__ method of the parent class
        super().__init__(name, species="Dog")
        self.breed = breed

    def make_sound(self):
        # Call the make_sound method of the parent class
        sound = super().make_sound()
        return f"{sound} Woof."


class Cat(Animal):
    def __init__(self, name, breed):
        # Call the __init__ method of the parent class
        super().__init__(name, species="Cat")
        self.breed = breed

    def make_sound(self):
        # Call the make_sound method of the parent class
        sound = super().make_sound()
        return f"{sound} Meow."


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        return "works on tasks"


class Manager(Employee):
    def __init__(self, name, department):
        super().__init__(name, position="Manager")
        self.department = department

    def work(self):
        task = super().work()
        return f"{task} and manages the {self.department} department"


class Developer(Employee):
    def __init__(self, name, programming_language):
        super().__init__(name, position="Developer")
        self.programming_language = programming_language

    def work(self):
        task = super().work()
        return f"{task} and writes code in {self.programming_language}"


def main(animal_example=True, employee_example=True):
    if animal_example:
        dog = Dog(name="Buddy", breed="Golden Retriever")
        cat = Cat(name="Whiskers", breed="Siamese")

        print(f"\n{dog.name} is a {dog.breed} and {dog.make_sound()}")
        print(f"{cat.name} is a {cat.breed} and {cat.make_sound()}")

    if employee_example:
        personnel = ["Alex", "Blake", "Chris", "Dylan", "Elliott"]
        departments = ["Sales", "Marketing", "Engineering", "HR", "Operations"]
        languages = ["Python", "Java", "C++", "C#", ".NET"]
        manager = Manager(name=choice(personnel), department=choice(departments))
        developer = Developer(name=choice(personnel), programming_language=choice(languages))

        print(f"\n{manager.name} is a {manager.position} and {manager.work()}")
        print(f"{developer.name} is a {developer.position} and {developer.work()}")


if __name__ == "__main__":
    main(
        animal_example=False,
        employee_example=True,
        )
