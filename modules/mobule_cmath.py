import cmath
from typing import List, Tuple

"""
Python's built-in `cmath` module is used for complex number mathematics, which can be useful in signal processing, Fourier transforms, and advanced analytics involving complex numbers.
"""


def calculate_magnitude_phase(numbers: List[complex]) -> List[Tuple[float, float]]:
    """
    Calculate the magnitude and phase (in radians) for a list of complex numbers.

    Args:
        numbers (List[complex]): List of complex numbers.

    Returns:
        List[Tuple[float, float]]: List of (magnitude, phase) tuples.
    """
    return [(abs(z), cmath.phase(z)) for z in numbers]


def polar_to_rect(magnitude: float, phase: float) -> complex:
    """
    Convert polar coordinates to a complex number (rectangular form).

    Args:
        magnitude (float): The magnitude (radius).
        phase (float): The phase angle in radians.

    Returns:
        complex: The corresponding complex number.
    """
    return cmath.rect(magnitude, phase)


def calculate_roots_of_unity(n: int) -> List[complex]:
    """
    Calculate the n-th roots of unity, useful in Fourier analysis and signal processing.

    Args:
        n (int): The degree of the root.

    Returns:
        List[complex]: List of n-th roots of unity.
    """
    return [cmath.rect(1, 2 * cmath.pi * k / n) for k in range(n)]


def safe_log(z: complex) -> complex:
    """
    Compute the natural logarithm of a complex number, handling edge cases.

    Args:
        z (complex): The complex number.

    Returns:
        complex: The natural logarithm of z.
    """
    try:
        return cmath.log(z)
    except ValueError as e:
        print(f"Error computing log({z}): {e}")
        return complex(float("nan"), float("nan"))


def quadratic_roots(a: float, b: float, c: float) -> Tuple[complex, complex]:
    """
    Solve a quadratic equation ax^2 + bx + c = 0 using the quadratic formula.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        Tuple[complex, complex]: The two roots (may be complex).
    """
    discriminant = cmath.sqrt(b**2 - 4 * a * c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2


if __name__ == "__main__":
    # Magnitude and phase of complex numbers
    numbers = [3 + 4j, 1 - 1j, -2 + 2j]
    mag_phase = calculate_magnitude_phase(numbers)
    print("Magnitude and phase:", mag_phase)

    # Convert polar to rectangular
    z = polar_to_rect(5, cmath.pi / 4)
    print("Polar to rectangular:", z)

    # Roots of unity (useful in DFT/FFT)
    roots = calculate_roots_of_unity(4)
    print("4th roots of unity:", roots)

    # Safe logarithm
    log_val = safe_log(-1 + 0j)
    print("Logarithm of -1:", log_val)

    # Quadratic roots (may be complex)
    roots = quadratic_roots(1, 2, 5)
    print("Quadratic roots:", roots)

"""
Troubleshooting Tips:
- Ensure input types are correct (e.g., use complex numbers where required).
- For phase, output is in radians; use math.degrees() if degrees are needed.
- cmath functions never raise ValueError for domain errors; they return complex NaN or inf.
- Use try/except for robust error handling in production code.

Efficiency Tips:
- Use list comprehensions for batch processing.
- Avoid unnecessary conversions between polar and rectangular forms.
- For large datasets, consider using numpy for vectorized operations.
"""
