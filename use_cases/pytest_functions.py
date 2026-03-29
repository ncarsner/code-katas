import random


def is_palindrome(string_input):
    return string_input == string_input[::-1]


class StringUtils:
    def reverse_string(self, string_input):
        return string_input[::-1]


def is_anagram(string_a, string_b):
    return sorted(string_a) == sorted(string_b)


class MathUtils:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


if __name__ == "__main__":
    words = ["racecar", "hello", "level", "world", "madam", "python", "listen", "silent"]
    print(f"{is_palindrome("racecar")=}")  # True
    print(f"{is_palindrome("hello")=}")  # False

    string_utils = StringUtils()
    print(f"{string_utils.reverse_string("hello")=}")  # "olleh"

    words = [random.choice(words) for _ in range(2)]
    print(f"{words[0]} = {words[1]}: {is_anagram(words[0], words[1])}")  # True
    words = [random.choice(words) for _ in range(2)]
    print(f"{is_anagram(words[0], words[1])=}")  # True


    math_utils = MathUtils()
    nums = [random.randint(1, 10) for _ in range(2)]
    print(f"{math_utils.add(nums[0], nums[1])=}")  # Random sum
    nums = [random.randint(1, 10) for _ in range(2)]
    print(f"{math_utils.multiply(nums[0], nums[1])=}")  # Random product
