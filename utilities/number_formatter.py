import random


def format_number(num, decimal_places=1):
    """
    Format a number into a human-readable string with appropriate truncation and rounding.

    Args:
    num (float): The number to format.
    decimal_places (int): The number of decimal places to round to.

    Returns:
    str: The formatted number as a string.
    """

    def format_with_optional_decimal(value, decimal_places):
        if isinstance(value, int) or value.is_integer():
            return f"{int(value)}"
        else:
            return f"{value:.{decimal_places}f}"

    if num >= 1_000_000_000:
        return format_with_optional_decimal(num / 1_000_000_000, decimal_places) + "B"
    elif num >= 1_000_000:
        return format_with_optional_decimal(num / 1_000_000, decimal_places) + "M"
    elif num >= 1_000:
        return format_with_optional_decimal(num / 1_000, decimal_places) + "k"
    else:
        return format_with_optional_decimal(num, decimal_places)


if __name__ == "__main__":
    # for i in range(2,12,3):
        # print(format_number(random.randint(10**i, 10**(i+1)-1)))
        # print(format_number(random.randint(10**i, 10**(i+1)-1), 2))

        # print(format_number(random.randint(10**3, 10**4-1)))
        # print(format_number(random.randint(1_000_000, 9_999_999)))
        # print(format_number(random.randint(1_000_000_000, 9_999_999_999)))
        # print(format_number(random.randint(1_000_000_000, 9_999_999_999), 2))
        # print(format_number(random.randint(1_000_000, 9_999_999), 2))
        # print(format_number(random.randint(1_000, 9_999), 2))
        # print(format_number(random.randint(100, 999), 2))

    print(format_number(random.randint(10**2, 10**3-1)))
    print(format_number(random.randint(1_000, 9_999)))
    print(format_number(random.randint(1_000_000, 9_999_999)))
    print(format_number(random.randint(1_000_000_000, 9_999_999_999)))
    print(format_number(random.randint(1_000_000_000, 9_999_999_999), 2))
    print(format_number(random.randint(1_000_000, 9_999_999), 2))
    print(format_number(random.randint(1_000, 9_999), 2))
    print(format_number(random.randint(100, 999), 2))
