import math
import random


def area_of_circle(radius):
    """Area of a circle"""
    return math.pi * (radius**2)


def factorial_of_number(n):
    """Factorial of a number"""
    return math.factorial(n)


def gcd_of_numbers(a, b):
    """Greatest common divisor of two numbers"""
    return math.gcd(a, b)


def square_root(number):
    """Square root of a number"""
    return math.sqrt(number)


def sine_of_angle(angle_radians):
    """Sine of an angle in radians"""
    return math.sin(angle_radians)


def cosine_of_angle(angle_radians):
    """Cosine of an angle in radians"""
    return math.cos(angle_radians)


def tangent_of_angle(angle_radians):
    """Tangent of an angle in radians"""
    return math.tan(angle_radians)


def degrees_to_radians(degrees):
    """Convert degrees to radians"""
    return math.radians(degrees)


def radians_to_degrees(radians):
    """Convert radians to degrees"""
    return math.degrees(radians)


def natural_logarithm(number):
    """Natural logarithm of a number"""
    return math.log(number)


def base10_logarithm(number):
    """Base-10 logarithm of a number"""
    return math.log10(number)


def exponential(number):
    """Exponential of a number"""
    return math.exp(number)


def power(base, exponent):
    """Power of a number"""
    return math.pow(base, exponent)


def hypotenuse(a, b):
    """Hypotenuse of a right-angled triangle"""
    return math.hypot(a, b)


def ceiling(number):
    """Ceiling of a number"""
    return math.ceil(number)


def floor(number):
    """Floor of a number"""
    return math.floor(number)


def absolute_value(number):
    """Absolute value of a number"""
    return math.fabs(number)


def remainder(a, b):
    """Remainder of a division"""
    return math.fmod(a, b)


precision_digits = 4
max_num = 20

random_radius = random.uniform(1, max_num)
random_number = random.randint(1, max_num)
random_angle = random.uniform(0, math.pi)
random_base = random.uniform(1, max_num)
random_exponent = random.uniform(1, max_num)
random_a = random.randint(1, max_num)
random_b = random.randint(1, max_num)

# Dictionary of functions
functions_dict = {
    1: ("\nArea of Circle", area_of_circle, [random_radius]),
    2: ("Factorial of Number", factorial_of_number, [random_number]),
    3: ("GCD of Numbers", gcd_of_numbers, [random_a, random_b]),
    4: ("Square Root", square_root, [random_number]),
    5: ("Sine of Angle", sine_of_angle, [random_angle]),
    6: ("Cosine of Angle", cosine_of_angle, [random_angle]),
    7: ("Tangent of Angle", tangent_of_angle, [random_angle]),
    8: ("Degrees to Radians", degrees_to_radians, [random_number]),
    9: ("Radians to Degrees", radians_to_degrees, [random_angle]),
    10: ("Natural Logarithm", natural_logarithm, [random_number]),
    11: ("Base-10 Logarithm", base10_logarithm, [random_number]),
    12: ("Exponential", exponential, [random_number]),
    13: ("Power", power, [random_base, random_exponent]),
    14: ("Hypotenuse", hypotenuse, [random_a, random_b]),
    15: ("Ceiling", ceiling, [random_number]),
    16: ("Floor", floor, [random_number]),
    17: ("Absolute Value", absolute_value, [random_number]),
    18: ("Remainder", remainder, [random_a, random_b]),
}

if __name__ == "__main__":
    for key, (description, func, args) in functions_dict.items():
        result = func(*args)
        if isinstance(result, float):
            result = round(result, precision_digits)
        args_str = ", ".join(f"{arg:.{precision_digits}f}" if isinstance(arg, float) else str(arg) for arg in args)
        print(f"{description} (args: {args_str}): {result}")
