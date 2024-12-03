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


teams = [
    '1 Nashville',
    '2 Murfreesboro',
    '3 Franklin',
    '4 Brentwood',
    '5 Hendersonville',
    '6 Clarksville',
    '7 Gallatin',
    '8 Lebanon',
    '9 Mt. Juliet',
    '10 Smyrna',
    '11 La Vergne',
    '12 Antioch',
    '13 Hermitage',
    '14 Madison',
    '15 Goodlettsville',
    '16 Belle Meade',
]

random.shuffle(teams)

for i in range(len(teams) // 2):
    print(f"{teams[i]} vs. {teams[len(teams)-i-1]}")