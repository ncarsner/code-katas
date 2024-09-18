import random

students = {
    "Alex": ['Engineering', 'Sociology', 'Algebra', 'Humanities', 'Study'],
    "Blake": ['US History', 'Literature', 'Study', None],
    "Chris": ['Trigonometry', 'Humanities', 'Engineer', 'Study', None],
    "Dylan": ['World Languages', 'Programming', 'Social Studies', 'Study', None],
    "Elliott": ['Sciences', 'Engineering', 'World History', 'Chemistry', 'Study', None],
}

for student, classes in students.items():
    print(f"{student} is taking {random.choice(classes)}")