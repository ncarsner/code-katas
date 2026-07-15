import re
from string import ascii_letters, digits, punctuation
import random

CHARS = ascii_letters + digits + punctuation + " "


def is_valid_password(password, min_length=8):
    a = re.compile(r"(?=.*\d)")  # at least one digit
    b = re.compile(r"(?=.*[a-z])")  # at least one lowercase letter
    c = re.compile(r"(?=.*[A-Z])")  # at least one uppercase letter
    d = re.compile(r"(?=.*[^a-zA-Z0-9\s])")  # at least one special character
    e = re.compile(r"(?=.*[!@#$%^&*\(\)\[\],\.\\\/])") # at least one specific special character
    f = re.compile(r".{" + str(min_length) + ",}")  # at least 8 characters long

    return bool(
        a.search(password)        # contains digit (0-9)
        and b.search(password)    # contains lowercase letter (a-z)
        and c.search(password)    # contains uppercase letter (A-Z)
        and d.search(password)    # contains special character
        and e.search(password)    # contains a specific special character !@#$%^&*()[],./\
        and f.search(password)    # is 8 or more characters
    )


def main():
    test_passwords = [
        "".join(random.sample(CHARS, random.randint(5, 20))) for _ in range(8)
    ]

    for pwd in test_passwords:
        if is_valid_password(pwd, min_length=8):
            print(f"Valid   | length: {len(pwd):>2} | {pwd:>20}")
        else:
            print(f"INVALID | length: {len(pwd):>2} | {pwd:>20}")


if __name__ == "__main__":
    main()
