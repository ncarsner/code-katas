import random


def test_pass():
    list_of_nums = [random.randint(1, 100) for _ in range(10)]
    assert all(isinstance(num, int) for num in list_of_nums)
