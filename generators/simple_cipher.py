from string import ascii_lowercase
from datetime import datetime
import random


def create_cipher_dict():
    current_day = datetime.now().day
    letters = list(ascii_lowercase)
    offset = current_day % len(letters) - 1
    offset_letters = letters[offset:] + letters[:offset]

    cipher_dict = {}

    for i in range(len(offset_letters)):
        char_1 = offset_letters[i]
        char_2 = offset_letters[-(i + 1)]
        cipher_dict[char_1] = char_2

    return cipher_dict


def cipher_string(input_string, cipher_dict):
    return "".join(cipher_dict[char] for char in input_string if char in cipher_dict)


if __name__ == "__main__":
    user_input = input("ENTER USER INITIALS: ").lower()
    cipher_dict = create_cipher_dict()
    ciphered_value = cipher_string(user_input, cipher_dict)

    # Generate three incorrect values
    incorrect_values = []
    while len(incorrect_values) < 3:
        random_value = "".join(random.choice(list(cipher_dict.values())) for _ in range(len(ciphered_value)))
        if random_value != ciphered_value and random_value not in incorrect_values:
            incorrect_values.append(random_value)

    # Combine correct and incorrect values and shuffle them
    options = incorrect_values + [ciphered_value]
    random.shuffle(options)

    # Present options to the user
    print("\nSelect the correct ciphered value:")
    for i, option in enumerate(options):
        print(f"{i + 1}: {option}")

    # Get user selection
    user_selection = int(input("Enter the number of your choice: ")) - 1

    # Check if the user selected the correct value
    if options[user_selection] == ciphered_value:
        print("Correct!")
    else:
        print("Incorrect. Access denied.")
