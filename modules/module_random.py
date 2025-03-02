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


def get_random_weighted(low=None, high=None, weights=None, num_samples=1):
    """Returns a random floating-point number using weighted probabilities.

    - If `low` and `high` are not provided, they default to a random range.
    - If `weights` is not provided, it defaults to an increasing likelihood from `low` to `high`.

    Parameters:
        low (int): Lower bound of the range (inclusive).
        high (int): Upper bound of the range (inclusive).
        weights (list): List of weights corresponding to each value in the range.
        num_samples (int): Number of values to return.

    Returns:
        float or list: A single random number if `num_samples == 1`, otherwise a list.
    """
    if low is None:
        low = random.randint(1, 10)
    if high is None:
        high = low + random.randint(1, 10)

    # Generate a range of values
    values = list(range(low, high + 1))

    # Default weights: Increase likelihood towards higher values
    if weights is None:
        weights = [i - low + 1 for i in values]  # Example: 1, 2, 3, ... progressively increasing

    # Select a weighted random choice
    selected_values = random.choices(values, weights=weights, k=num_samples)

    return selected_values[0] if num_samples == 1 else selected_values



def random_triangular(
    low: float = None, high: float = None, mode: float = None) -> float:
    """Returns a random floating point number N such that low <= N <= high and with the specified mode between those bounds."""
    if low is None:
        low = random.randint(1, 10)
    if high is None:
        high = low + random.randint(1, 10)
    if mode is None:
        mode = random.uniform(low, high)
        # mode = (low + high) / 2 if mode < low or mode > high else mode
    return random.triangular(low, high, mode)


if __name__ == "__main__":
    a = random.randint(1, 10)
    b = a + random.randint(1, 10)
    c = random.randint(1, 10)

    print(f"{random_choice([1, 2, 3, 4, 5])=}")
    print(f"{random_shuffle([1, 2, 3, 4, 5])=}")
    print(f"{random_randint(1, 100)=}")
    print(f"{random_sample([1, 2, 3, 4, 5], 3)=}")
    print(f"Random uniform({a=},{b=}): {random_uniform(a, b)}")
    print(f"{random_random()=}")
    print(f"{random_triangular()=}")

    print(f"Triangular({a=},{b=}): {random_triangular(a, b)}")
    print(f"Triangular default: {random_triangular()}")
    print(f"Triangular skewed({a=},{b=},{c=}): {random_triangular(a, b, c)}")

    print(f"Weighted: {get_random_weighted()}")
    print(f"Weighted (increasingly high between {a} and {b}): {get_random_weighted(a, b)}")
    print(f"Weighted (decreasingly low): {get_random_weighted(1, 10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])}")

    students = {
        "Alex": ["Engineering", "Sociology", "Algebra", "Humanities", "Study"],
        "Blake": ["US History", "Literature", "Study", None],
        "Chris": ["Trigonometry", "Humanities", "Engineer", "Study", None],
        "Dylan": ["World Languages", "Programming", "Social Studies", "Study", None],
        "Elliott": ["Sciences", "Engineering", "World History", "Chemistry", "Study", None],
    }

    for student, classes in students.items():
        # print(f"{student} is taking {random.choice(classes)}")
        ...

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
        # print(f"{teams[i]} vs. {teams[len(teams)-i-1]}")
        ...
