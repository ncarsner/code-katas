from typing import FrozenSet
import random


def create_frozen_set(elements: list) -> FrozenSet:
    """
    Create a frozen set from a list of elements.

    Args:
        elements (list): A list of elements to be converted into a frozen set.

    Returns:
        FrozenSet: A frozen set containing the elements from the list.
    """
    return frozenset(elements)


def check_membership(fset: FrozenSet, element) -> bool:
    """
    Check if an element is a member of the frozen set.

    Args:
        fset (FrozenSet): The frozen set to check membership in.
        element: The element to check for membership.

    Returns:
        bool: True if the element is in the frozen set, False otherwise.
    """
    return element in fset


def union_frozen_sets(fset1: FrozenSet, fset2: FrozenSet) -> FrozenSet:
    """
    Perform a union operation on two frozen sets.

    Args:
        fset1 (FrozenSet): The first frozen set.
        fset2 (FrozenSet): The second frozen set.

    Returns:
        FrozenSet: A new frozen set that is the union of the two frozen sets.
    """
    return fset1 | fset2


def intersection_frozen_sets(fset1: FrozenSet, fset2: FrozenSet) -> FrozenSet:
    """
    Perform an intersection operation on two frozen sets.

    Args:
        fset1 (FrozenSet): The first frozen set.
        fset2 (FrozenSet): The second frozen set.

    Returns:
        FrozenSet: A new frozen set that is the intersection of the two frozen sets.
    """
    return fset1 & fset2


def difference_frozen_sets(fset1: FrozenSet, fset2: FrozenSet) -> FrozenSet:
    """
    Perform a difference operation on two frozen sets.

    Args:
        fset1 (FrozenSet): The first frozen set.
        fset2 (FrozenSet): The second frozen set.

    Returns:
        FrozenSet: A new frozen set that is the difference of the two frozen sets.
    """
    return fset1 - fset2


if __name__ == "__main__":
    elements1 = [random.randint(1, 10) for _ in range(4)]
    elements2 = [random.randint(1, 10) for _ in range(4)]

    fset1 = create_frozen_set(elements1)
    fset2 = create_frozen_set(elements2)

    print(f"Frozen Set 1: {fset1}")
    print(f"Frozen Set 2: {fset2}")

    print(f"Is 3 in Frozen Set 1? {check_membership(fset1, 3)}")
    print(f"Union: {union_frozen_sets(fset1, fset2)}")
    print(f"Intersection: {intersection_frozen_sets(fset1, fset2)}")
    print(f"Difference (fset1 - fset2): {difference_frozen_sets(fset1, fset2)}")
