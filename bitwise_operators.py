from datetime import datetime as dt


# Basic bitwise operations
def basic_bitwise_operations(a, b):
    print(f"{a=}, {bin(a)=})")
    print(f"{b=}, {bin(b)=})")
    print(f"{a & b=}, {bin(a & b)=})")
    print(f"{a | b=}, {bin(a | b)=})")
    print(f"{a ^ b=}, {bin(a ^ b)=})")
    print(f"{~a=}, {bin(~a)=})")
    print(f"{a << 2=}, {bin(a << 2)=})")
    print(f"{a >> 2=}, {bin(a >> 2)=})")


# Example:
# basic_bitwise_operations(5, 3)


# Check odd or even using bitwise AND
def check_odd_even(number):
    if number & 1:
        print(f"{number} is Odd")
    else:
        print(f"{number} is Even")


# Example
# check_odd_even(10)
# check_odd_even(15)


# Swap two numbers using XOR
def swap_numbers(a, b):
    print(f"Before Swap: {a=}, {b=}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After Swap: {a=}, {b=}")


# Example
# swap_numbers(7, 12)


# Find the unique element in a list where every other element appears twice
def find_unique(arr):
    result = 0
    for num in arr:
        result ^= num
    print(f"The unique element is: {result}")


# Example
# find_unique([2, 3, 5, 3, 2, 5, 7])


# Masking specific bits
def mask_bits(number, mask):
    print(f"Original number: {number} (binary: {bin(number)})")
    print(f"Mask: {mask} (binary: {bin(mask)})")
    masked_number = number & mask
    print(f"Masked number: {masked_number} (binary: {bin(masked_number)})")


# Example
# mask_bits(0b110101, 0b111000)


# Setting specific bits
def set_bits(number, mask):
    print(f"Original number: {number}, {bin(number)=})")
    print(f"{mask=}, {bin(mask)=})")
    new_number = number | mask
    print(f"{new_number=}, {bin(new_number)=})")


# Example
# set_bits(0b1001, 0b0100)


# Check if a number is a power of 2
def is_power_of_two(number):
    if number & (number - 1) == 0 and number != 0:
        print(f"{number} is a power of 2")
    else:
        print(f"{number} is not a power of 2")


# Example
# is_power_of_two(8)
# is_power_of_two(10)


# Toggle a specific bit
def toggle_bit(number, position):
    print(f"Original number: {number}, {bin(number)=})")
    toggle_mask = 1 << position
    toggled_number = number ^ toggle_mask
    print(
        f"Number after toggling bit at position {position}: {toggled_number} (binary: {bin(toggled_number)})"
    )


# Example
# toggle_bit(0b1011, 2)


# Permissions system using bit flags
READ = 0b001
WRITE = 0b010
EXECUTE = 0b100


def check_permission(user_permission, required_permission):
    if user_permission & required_permission:
        print(f"Permission granted for {bin(required_permission)}")
    else:
        print(f"Permission denied for {bin(required_permission)}")


# Example
user_permission = READ | EXECUTE
print(f"User permissions: {bin(user_permission)}")
# check_permission(user_permission, READ)
# check_permission(user_permission, WRITE)
# check_permission(user_permission, EXECUTE)


# # Bitwise shift a string
# def xor_encrypt_decrypt(text, key):
#     encrypted = "".join(chr(ord(char) ^ key) for char in text)
#     return encrypted


# # Example
# raw_text = "this is a string"
# key = int(dt.today().strftime("%d"))

# # Encrypt the string
# encrypted_text = xor_encrypt_decrypt(raw_text, key)
# print(f"{encrypted_text=}")

# # Decrypt the string
# decrypted_text = xor_encrypt_decrypt(encrypted_text, key)
# print(f"{decrypted_text=}")


def xor_encrypt_decrypt(text, key, space_replacement="`%"):
    if space_replacement in text:
        raise ValueError(
            f"The space replacement '{space_replacement}' must not be part of the input text."
        )

    if " " in text:
        # Replace spaces with the declared value
        text = text.replace(" ", space_replacement)

    # Encrypt or decrypt the text using XOR with the key
    transformed = "".join(chr(ord(char) ^ key) for char in text)
    return transformed


def decrypt_transformed(encrypted_text, key, space_replacement="`%"):
    # Decrypt the text using XOR with the same key
    decrypted = "".join(chr(ord(char) ^ key) for char in encrypted_text)

    # Restore the spaces if the replacement value is found
    if space_replacement in decrypted:
        decrypted = decrypted.replace(space_replacement, " ")
    return decrypted


# Example usage
original_text = "Would you like a piña colada?"
key = 5  # Simple XOR key
key = int(dt.today().strftime("%d"))
key = 7
space_placeholder = "`%"

# Encrypt the string
encrypted_text = xor_encrypt_decrypt(original_text, key)
print(f"{encrypted_text=}")

# Decrypt the string
decrypted_text = decrypt_transformed(encrypted_text, key)
print(f"{decrypted_text=}")
