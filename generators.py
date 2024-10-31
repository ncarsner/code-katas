import sys
from typing import Generator


def fibonacci_generator() -> (Generator[int, None, None]):  # 3 types [yield, input, return]
    a, b = 0, 1
    while True:
        yield f"{a:,}"
        a, b = b, (a + b)


def prime_generator() -> Generator[int, None, None]:
    num = 2
    while True:
        if not any(num % y == 0 for y in range(2, int(num / 2) + 1)):
            yield f"{num:,}"
        num += 1

def read(path: str) -> Generator[str, None, str]: # reads a string, None as input, outputs a string
    with open(path, 'r') as file:
        for line in file:
            yield line.strip()

        return 'end of file'


def main() -> None:  # 1 usage
    selection = ["fibonacci", "prime", "reader"]
    selection = selection[0]

    fibonacci: Generator[int, None, None] = fibonacci_generator()
    primes: Generator[int, None, None] = prime_generator()
    reader: Generator[str, None, str] = read(r'moon.txt')

    n: int = 10
    line_break: str = "-" * 20

    if selection == "reader":
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
