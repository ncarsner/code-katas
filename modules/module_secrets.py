import secrets

secure_random_number = secrets.randbelow(100)
print(f"{secure_random_number=}")

secure_random_bit = secrets.randbits(4)
print(f"{secure_random_bit=}")

secure_random_bytes = secrets.token_bytes(16)
print(f"{secure_random_bytes=}")

secure_random_urlsafe = secrets.token_urlsafe(16)
print(f"{secure_random_urlsafe=}")

secure_random_hex = secrets.token_hex(16)
print(f"{secure_random_hex=}")

choices = ['apple', 'banana', 'cherry', 'date', 'eggplant', 'fig', 'grape', 'honeydew']
secure_random_choice = secrets.choice(choices)
print(f"{secure_random_choice=}")

# Compare two strings in a secure manner
string1 = 'password123'
string2 = 'password123'
secure_compare = secrets.compare_digest(string1, string2)
print(f"{secure_compare=}")
