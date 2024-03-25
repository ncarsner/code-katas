from fractions import Fraction


def fraction_to_decimal(fraction):
    numerator, denominator = fraction.numerator, fraction.denominator
    if numerator == 0:
        return "0"

    result = ""
    if (numerator < 0) ^ (denominator < 0):
        result += "-"
    numerator, denominator = abs(numerator), abs(denominator)

    quotient, remainder = divmod(numerator, denominator)
    result += str(quotient)
    if remainder == 0:
        return result

    result += "."

    # Use a dictionary to keep track of the remainder and its index
    remainders = {}
    while remainder != 0:
        if remainder in remainders:
            index = remainders[remainder]
            result = result[:index] + "(" + result[index:] + ")"
            break
        remainders[remainder] = len(result)
        quotient, remainder = divmod(remainder * 10, denominator)
        result += str(quotient)

    return result


# Example usage:
# fraction = Fraction(1, 3)
fractions = [
    Fraction(1, 3),
    Fraction(1, 5),
    Fraction(1, 8),
    Fraction(1, 7),
    Fraction(4, 9),
    Fraction(4, 11),
]


for fraction in fractions:
    decimal_representation = fraction_to_decimal(fraction)
    print(decimal_representation)
