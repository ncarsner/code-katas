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
