import random
from typing import List, Any, Sequence


def random_choice(sequence: Sequence[Any]) -> Any:
    """Returns a random element from a non-empty sequence."""
    return random.choice(sequence)


def random_shuffle(sequence: List[Any]) -> List[Any]:
    """Shuffles the sequence in place."""
    random.shuffle(sequence)
    return sequence


def random_randint(a: int, b: int) -> int:
    """Returns a random integer N such that a <= N <= b."""
    return random.randint(a, b)


def random_sample(sequence: Sequence[Any], k: int) -> List[Any]:
    """Returns a k length list of unique elements chosen from the sequence."""
    return random.sample(sequence, k)


def random_uniform(a: float, b: float) -> float:
    """Returns a random floating point number N such that a <= N <= b."""
    return random.uniform(a, b)


def random_random() -> float:
    """Returns a random floating point number in the range [0.0, 1.0)."""
    return random.random()



if __name__ == '__main__':
    print(f"{random_choice([1, 2, 3, 4, 5])=}")
    print(f"{random_shuffle([1, 2, 3, 4, 5])=}")
    print(f"{random_randint(1, 100)=}")
    print(f"{random_sample([1, 2, 3, 4, 5], 3)=}")
    print(f"{random_uniform(1.0, 10.0)=}")
    print(f"{random_random()=}")


    students = {
        "Alex": ["Engineering", "Sociology", "Algebra", "Humanities", "Study"],
        "Blake": ["US History", "Literature", "Study", None],
        "Chris": ["Trigonometry", "Humanities", "Engineer", "Study", None],
        "Dylan": ["World Languages", "Programming", "Social Studies", "Study", None],
        "Elliott": ["Sciences", "Engineering", "World History", "Chemistry", "Study", None],
    }

    for student, classes in students.items():
        print(f"{student} is taking {random.choice(classes)}")


    teams = [
        "1 Nashville",
        "2 Murfreesboro",
        "3 Franklin",
        "4 Brentwood",
        "5 Hendersonville",
        "6 Clarksville",
        "7 Gallatin",
        "8 Lebanon",
        "9 Mt. Juliet",
        "10 Smyrna",
        "11 La Vergne",
        "12 Antioch",
        "13 Hermitage",
        "14 Madison",
        "15 Goodlettsville",
        "16 Belle Meade",
    ]

    random.shuffle(teams)

    for i in range(len(teams) // 2):
        print(f"{teams[i]} vs. {teams[len(teams)-i-1]}")
