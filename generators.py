import sys
from typing import Generator
import random
from string import digits

        
def fibonacci_generator() -> Generator[int, None, None]:
    """
    A generator function that yields Fibonacci numbers indefinitely.

    Yields:
        int: The next Fibonacci number in the sequence, formatted with commas.
    """
    a, b = 0, 1
    while True:
        yield f"{a:,}"
        a, b = b, (a + b)

        
def prime_generator() -> Generator[int, None, None]:
    """
    A generator function that yields prime numbers indefinitely.

    Yields:
        int: The next prime number in the sequence, formatted with commas.
    """
    num = 2
    while True:
        if not any(num % y == 0 for y in range(2, int(num / 2) + 1)):
            yield f"{num:,}"
        num += 1


def otp_generator() -> Generator[str, None, str]:
    """
    A generator function that yields a random 6-digit OTP (One-Time Password) indefinitely.

    Yields:
        str: A random 6-digit OTP.
    """
    while True:
        yield ''.join([random.choice(digits) for _ in range(6)])


def read(path: str) -> Generator[str, None, str]:
    """
    A generator function that reads a file line by line.

    Args:
        path (str): The path to the file to read.

    Yields:
        str: The next line in the file, stripped of leading and trailing whitespace.

    Returns:
        str: "end of file" when the file has been completely read.
    """
    with open(path, "r") as file:
        for line in file:
            yield line.strip()

        return "end of file"


def main() -> None:  # 1 usage
    selection = ["fibonacci", "prime", "otp", "reader"]
    selection = selection[2]

    fibonacci: Generator[int, None, None] = fibonacci_generator()
    primes: Generator[int, None, None] = prime_generator()
    reader: Generator[str, None, str] = read(r"moon.txt")
    otp: Generator[str, None, str] = otp_generator()

    n: int = 10
    line_break: str = "-" * 20

    if selection == "otp":
        while True:
            input(f"Press ENTER for the next {n} {selection} numbers")

            print(line_break)

            for i in range(n):
                print(f"{next(otp)}")

            print(line_break)

    elif selection == "reader":
        while True:
            try:
                print(next(reader))
            except StopIteration as e:
                print(line_break, e.value)
                sys.exit()

            input()

    else:
        while True:
            input(f"Press ENTER for the next {n} {selection} numbers")

            print(line_break)

            for i in range(n):
                if selection == "prime":
                    print(f"{next(primes)}")
                elif selection == "fibonacci":
                    print(f"{next(fibonacci)}")

            print(line_break)


if __name__ == "__main__":
    main()
