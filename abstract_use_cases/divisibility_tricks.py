from string import digits
import random

"""
Inspired by Numberphile's video on divisibility tricks - https://www.youtube.com/watch?v=yi-s-TTpLxY
"""


def create_random_number(length=4):
    characters = digits
    result = "".join(random.choice(characters) for _ in range(length))
    return result


def is_divisible_by_3(num_str):
    # A number is divisible by 3 if the sum of its digits is divisible by 3
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum % 3 == 0


def is_divisible_by_9(num_str):
    # A number is divisible by 9 if the sum of its digits is divisible by 9
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum % 9 == 0


def is_divisible_by_11(num_str):
    # A number is divisible by 11 if the difference between the sum of its odd-positioned digits and even-positioned digits is either 0 or divisible by 11
    odd_sum = sum(int(num_str[i]) for i in range(0, len(num_str), 2))
    even_sum = sum(int(num_str[i]) for i in range(1, len(num_str), 2))
    return abs(odd_sum - even_sum) % 11 == 0


def is_divisible_by_6(num_str):
    # A number is divisible by 6 if it is divisible by both 2 and 3
    return int(num_str[-1]) % 2 == 0 and is_divisible_by_3(num_str)


def is_divisible_by_4(num_str):
    # A number is divisible by 4 if the last two digits form a number that is divisible by 4
    last_two_digits = int(num_str[-2:]) if len(num_str) >= 2 else int(num_str)
    return last_two_digits % 4 == 0


def is_divisible_by_8(num_str):
    # A number is divisible by 8 if the last three digits form a number that is divisible by 8
    last_three_digits = int(num_str[-3:]) if len(num_str) >= 3 else int(num_str)
    return last_three_digits % 8 == 0


def main():
    random_number_str = create_random_number()
    print(f"Random Number: {int(random_number_str):,}")
    print(f"Divisible by 3: {is_divisible_by_3(random_number_str)}")
    print(f"Divisible by 9: {is_divisible_by_9(random_number_str)}")
    print(f"Divisible by 11: {is_divisible_by_11(random_number_str)}")
    print(f"Divisible by 6: {is_divisible_by_6(random_number_str)}")
    print(f"Divisible by 4: {is_divisible_by_4(random_number_str)}")
    print(f"Divisible by 8: {is_divisible_by_8(random_number_str)}")


if __name__ == "__main__":
    main()
