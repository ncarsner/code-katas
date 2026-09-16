"""Turn a decimal percentage into a simple whole-number ratio."""

from fractions import Fraction
import random


def percentage_to_ratio(percentage):
    """Return a percentage as an ``"x in y"`` ratio."""
    ratio = Fraction(str(percentage))
    return f"{ratio.numerator:,} in {ratio.denominator:,}"


if __name__ == "__main__":
    a, b, c, d = (round(random.uniform(0, 0.15), random.randint(1, 5)) for _ in range(4))

    print(f"Random percentage: {a}")
    print(percentage_to_ratio(a))  # e.g., 7 in 33
    print(f"{a * 100_000:,.1f} per 100,000")

    print(f"\nRandom percentage: {b}")
    print(percentage_to_ratio(b))  # e.g., 1 in 8
    print(f"{b * 100_000:,.1f} per 100,000")

    print(f"\nRandom percentage: {c}")
    print(percentage_to_ratio(c))  # e.g., 2 in 5
    print(f"{c * 100_000:,.1f} per 100,000")

    print(f"\nRandom percentage: {d}")
    print(percentage_to_ratio(d))  # e.g., 3 in 7
    print(f"{d * 100_000:,.1f} per 100,000")

    # print("\nPercentage: 0.04")
    # print(percentage_to_ratio(0.04))  # 1 in 25
    # print(f"{0.04 * 100_000:,.1f} per 100,000")

    # print("\nPercentage: 0.72")
    # print(percentage_to_ratio(0.72))  # 18 in 25
    # print(f"{0.72 * 100_000:,.1f} per 100,000")
