"""
Use of a bit register for tracking the status of multiple flags in a BI context. A bit register is useful for efficiently storing and manipulating binary states (e.g., true/false, on/off) for multiple conditions.

Example Use Case:
Tracking the status of various data quality checks on a dataset.
Each bit in the register represents whether a specific check has passed (1) or failed (0).
"""

import random

NUM_A, NUM_B, NUM_C = map(int, random.sample(range(9), 3))


class BitRegister:
    """
    A class to manage a bit register for tracking binary states.
    """

    def __init__(self, num_bits: int):
        """
        Initialize the bit register with a specified number of bits.

        :param num_bits: The number of bits to allocate in the register.
        """
        if num_bits <= 0:
            raise ValueError("Number of bits must be greater than zero.")
        self.num_bits = num_bits
        self.register = 0  # Initialize all bits to 0

    def set_bit(self, position: int) -> None:
        """
        Set a specific bit to 1.

        :param position: The position of the bit to set (0-indexed).
        """
        if position < 0 or position >= self.num_bits:
            raise ValueError("Bit position out of range.")
        self.register |= 1 << position

    def clear_bit(self, position: int) -> None:
        """
        Clear a specific bit (set it to 0).

        :param position: The position of the bit to clear (0-indexed).
        """
        if position < 0 or position >= self.num_bits:
            raise ValueError("Bit position out of range.")
        self.register &= ~(1 << position)

    def toggle_bit(self, position: int) -> None:
        """
        Toggle a specific bit (flip its value).

        :param position: The position of the bit to toggle (0-indexed).
        """
        if position < 0 or position >= self.num_bits:
            raise ValueError("Bit position out of range.")
        self.register ^= 1 << position

    def check_bit(self, position: int) -> bool:
        """
        Check the value of a specific bit.

        :param position: The position of the bit to check (0-indexed).
        :return: True if the bit is 1, False if it is 0.
        """
        if position < 0 or position >= self.num_bits:
            raise ValueError("Bit position out of range.")
        return (self.register & (1 << position)) != 0

    def __str__(self) -> str:
        """
        Return a string representation of the bit register.
        """
        return f"{self.register:0{self.num_bits}b}"


if __name__ == "__main__":

    num_checks = random.randint(4, 8)
    data_quality_register = BitRegister(num_checks)
    print("Empty Register:", data_quality_register)

    # Randomly set bits to 1
    for i in range(num_checks):
        if random.choice([True, False]):
            data_quality_register.set_bit(i)

    # Current state of the register
    print("DQ Register:", data_quality_register)

    # Status of a specific check
    some_bit = random.randint(0, num_checks - 1)
    print(f"Check {some_bit + 1} passed:", data_quality_register.check_bit(some_bit))

    # Clear first bit, Toggle last bit
    data_quality_register.clear_bit(0)  # Clear Check 1
    print("Cleared Check 1")
    data_quality_register.toggle_bit(num_checks - 1)  # Toggle the last bit
    print(f"Toggled Check {num_checks}")

    # Updated state of the register
    print("DQ Register:", data_quality_register)
