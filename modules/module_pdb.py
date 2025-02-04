import pdb
import random


def add(a, b):
    pdb.set_trace()
    return a + b


def subtract(a, b):
    pdb.set_trace()
    return a - b


def multiply(a, b):
    pdb.set_trace()
    return a * b


def divide(a, b):
    pdb.set_trace()
    if not b:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def main():
    x = random.randint(1, 100)
    y = random.randint(1, 100)

    result_add = add(x, y)
    print(f"Add: {x} + {y} = {result_add}")

    result_subtract = subtract(x, y)
    print(f"Subtract: {x} - {y} = {result_subtract}")

    result_multiply = multiply(x, y)
    print(f"Multiply: {x} * {y} = {result_multiply}")

    result_divide = divide(x, y)
    print(f"Divide: {x} / {y} = {result_divide}")


if __name__ == "__main__":
    main()
