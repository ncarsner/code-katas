import random
from typing import List
from collections import Counter


def remove_dupes_no_modules(lst: List[int]) -> List[int]:
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


def remove_dupes_with_collections(lst: List[int]) -> List[int]:
    return list(Counter(lst).keys())


if __name__ == "__main__":
    nums = random.choices(range(10), k=10)

    print(f"\n{nums=}")

    print(f"\n{remove_dupes_no_modules(nums)=}")
    print(f"{remove_dupes_with_collections(nums)=}")
    print(f"{remove_dupes_no_modules(nums) == remove_dupes_with_collections(nums)=}")
