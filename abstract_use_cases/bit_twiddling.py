"""Bit -> Slice -> Index -> Tiny String use cases"""

import random
from string import digits

def bitmask_n_bits(n):
    return (1 << n) - 1  # fast way to get a bitmask of n bits

def bitmask_n_bits_slow(n):
    mask = 0
    for i in range(n):
        mask |= (1 << i)
    return mask

def bitmask_slice_step(n):
    return "ab"[::(1 << n) - 1]  # fast way to get a slice of n bits

def eight_way_choice_from_n_bits(n):
    nums = "01234567"
    return nums[n & 7]  # fast way to get a choice from 8 options based on n bits


def two_char_state_from_n_bits(n):
    return "abcd"[(n & 1)*1 + ((n <1) & 1)*2]  # fast way to get a two-character state based on n bits

def two_bit_class_from_stepped_slice(n):
    return "0123"[(n & 3)::4]  # fast way to get a two-bit class from a stepped slice based on n bits


if __name__ == "__main__":
    # Example usage of bitmask_n_bits
    n = random.randint(1, 10)  # Randomly choose a number of bits between 1 and 10
    mask = bitmask_n_bits(n)
    print(f"Bitmask for {n} bits: {bin(mask)}")  # Output: 0b11111

    # Generate a random integer and apply the bitmask
    random_int = random.randint(0, 100)
    masked_value = random_int & mask
    print(f"Random integer: {random_int}, Masked value: {masked_value}")

    # Example usage of bitmask_n_bits_slow
    slow_mask = bitmask_n_bits_slow(n)
    print(f"Slow bitmask for {n} bits: {bin(slow_mask)}")  # Output: 0b11111

    # Example usage of bitmask_slice_step
    slice_result = bitmask_slice_step(n)
    print(f"Slice result for {n} bits: {slice_result}")  # Output: 'a' or 'ab' depending on n

    # Example usage of eight_way_choice_from_n_bits
    choice = eight_way_choice_from_n_bits(n)
    print(f"Eight-way choice from {n} bits: {choice}")  # Output: a digit from '0' to '7' based on n bits

    # Example usage of two_char_state_from_n_bits
    state = two_char_state_from_n_bits(n)
    print(f"Two-character state from {n} bits: {state}")  # Output: a character from 'a', 'b', 'c', or 'd' based on n

    # Example usage of two_bit_class_from_stepped_slice
    bit_class = two_bit_class_from_stepped_slice(n)
    print(f"Two-bit class from stepped slice for {n} bits: {bit_class}")  # Output: a character from '0', '1', '2', or '3 based on n
