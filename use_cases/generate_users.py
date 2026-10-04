"""
GOAL: Create test environment users and passwords,
utilizing a subtractive approach to array building by removing characters from a larger array,
as opposed to the most common additive method.
"""

import json
import secrets
import string

from names import first_names, surnames

min_pass_length = 12
max_pass_length = 32
number_of_users = 10

pw_values = string.printable.replace(string.whitespace, "") + " "


def password_generator():
    # Subtractive: start with a max-length array, then remove random characters down to the target length
    chars = [secrets.choice(pw_values) for _ in range(max_pass_length)]
    target_length = min_pass_length + secrets.randbelow(
        max_pass_length - min_pass_length + 1
    )
    while len(chars) > target_length:
        chars.pop(secrets.randbelow(len(chars)))
    return "".join(chars)


def generate_user_names(count):
    max_unique = len(set(first_names)) * len(set(surnames))
    if count > max_unique:
        raise ValueError(f"Cannot generate {count} unique names; max is {max_unique}")

    # Set prevents duplicate names from overwriting each other in the user dict
    user_names = set()
    while len(user_names) < count:
        user_names.add(
            secrets.choice(first_names) + " " + secrets.choice(surnames).title()
        )
    return list(user_names)


# GENERATED AS DICTIONARY
def generate_users(count=number_of_users):
    return {name: password_generator() for name in generate_user_names(count)}


# GENERATED AS LIST
def users_list(users):
    rows = []
    for user, user_pass in users.items():
        user_id = "".join(secrets.choice(string.digits) for _ in range(8))
        first, *rest = user.split()
        user_short_name = f"{first[0].lower()}{''.join(rest).lower()}{user_id}"
        rows.append((user_short_name, user, user_pass))

    uid_width = max(len(row[0]) for row in rows)
    user_width = max(len(row[1]) for row in rows)
    for user_short_name, user, user_pass in rows:
        print(
            f"[UID] {user_short_name:<{uid_width}}  [USER] {user:<{user_width}}  [PASS] {user_pass}"
        )


if __name__ == "__main__":
    # Run from the repo root so `names` is importable:
    #   python3 -m use_cases.generate_users
    user_dict = generate_users()
    users_list(user_dict)
    print("\n", json.dumps(user_dict, indent=4))
