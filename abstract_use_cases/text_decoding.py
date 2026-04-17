import random
from string import ascii_letters, digits
from datetime import datetime


def generate_random_string(length=10):
    characters = ascii_letters + digits
    result = "".join(random.choice(characters) for _ in range(length))
    return result


def decode_string(encoded_str):
    # Simple Caesar cipher with a shift of 3
    shift = 3
    shift = int(datetime.now().date().strftime("%d"))
    decoded_str = ""

    for char in encoded_str:
        if char.isalpha():
            # Shift character back by 'shift' positions
            offset = ord("A") if char.isupper() else ord("a")
            decoded_char = chr((ord(char) - offset - shift) % 26 + offset)
            decoded_str += decoded_char
        elif char.isdigit():
            # Shift digit back by 'shift' positions
            decoded_char = chr((ord(char) - ord("0") - shift) % 10 + ord("0"))
            decoded_str += decoded_char
        else:
            # Non-alphanumeric characters are not changed
            decoded_str += char

    return decoded_str


def random_string_as_bytes(length=10):
    random_str = generate_random_string(length)
    return random_str.encode("utf-8")


def random_string_as_bits(length=10):
    random_str = generate_random_string(length)
    return "".join(format(ord(char), "08b") for char in random_str)


if __name__ == "__main__":
    random_string = generate_random_string()
    random_string = "This is a random string"
    print(f"Encoded String: {random_string}")

    decoded_string = decode_string(random_string)
    print(f"Decoded String: {decoded_string}")

    random_bytes = random_string_as_bytes()
    print(f"Random String as Bytes: {random_bytes}")

    random_bits = random_string_as_bits()
    print(f"Random String as {len(random_bits) // 8} Bits: {random_bits}")
