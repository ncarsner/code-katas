from decimal import Decimal, getcontext  # , ROUND_DOWN
from prettytable import PrettyTable


def decimal_to_binary_fraction(decimal, max_bits=20):
    """Convert a decimal fraction to its binary representation."""
    binary = []
    fraction = decimal
    while fraction and len(binary) < max_bits:
        fraction *= 2
        bit = int(fraction)
        binary.append(str(bit))
        fraction -= bit
    return "".join(binary)


def find_smallest_repeating_sequence(binary):
    """Find the smallest repeating sequence in the binary string."""
    for i in range(1, len(binary) // 2 + 1):
        if len(binary) % i == 0:  # Check if the length is a multiple of i
            if binary[:i] * (len(binary) // i) == binary:
                return binary[:i]  # Return the repeating sequence
    return binary  # No repeating sequence found


# Define the decimal amounts
decimals = [i / 10 for i in range(1, 10)]

# Create a PrettyTable object
table = PrettyTable()
table.field_names = ["Decimal", "Binary Representation", "Least Repeat Bits"]

# Populate the table with calculated values
for decimal in decimals:
    binary_rep = decimal_to_binary_fraction(decimal)
    repeating_sequence = find_smallest_repeating_sequence(binary_rep)

    # Format the binary representation with '0.' prefix
    formatted_binary = f"0.{binary_rep}"
    smallest_repeating_bits = (
        f"{repeating_sequence} ({len(repeating_sequence)} bits)"
        if repeating_sequence != binary_rep
        else float("inf")
    )

    table.add_row([decimal, formatted_binary, smallest_repeating_bits])

# Set table attributes
table.align = "l"  # Align left
table.title = "Decimal to Binary Representation Table"

# Print the table
print(table)


# getcontext().prec = 64
# a = 0.1
# b = 0.2
# res1 = a + b

# print(a + b) # print 1
# res2 = Decimal(a) + Decimal(b)
# print(res2) # print 2

# output_style = Decimal("0.0")
# conformed_output = res2.quantize(output_style)

# print(conformed_output) # print 3
