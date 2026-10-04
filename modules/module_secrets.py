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

choices = ["apple", "banana", "cherry", "date", "eggplant", "fig", "grape", "honeydew"]
secure_random_choice = secrets.choice(choices)
print(f"{secure_random_choice=}")

# Compare two strings in a secure manner
string1 = "password123"
string2 = "password123"
secure_compare = secrets.compare_digest(string1, string2)
print(f"{secure_compare=}")

# compare_digest also accepts bytes; mismatches return False (str and bytes cannot be mixed)
secure_compare_bytes = secrets.compare_digest(b"token-abc", b"token-xyz")
print(f"{secure_compare_bytes=}")

# randbelow(n) returns 0..n-1; add an offset for an inclusive min..max range
MIN_LENGTH, MAX_LENGTH = 12, 32
secure_random_in_range = MIN_LENGTH + secrets.randbelow(MAX_LENGTH - MIN_LENGTH + 1)
print(f"{secure_random_in_range=}")

# Token functions default to DEFAULT_ENTROPY bytes when no size is given
print(f"{secrets.DEFAULT_ENTROPY=}")

default_token_hex = secrets.token_hex()
print(f"{default_token_hex=} ({len(default_token_hex)} hex chars)")

default_token_urlsafe = secrets.token_urlsafe()
print(f"{default_token_urlsafe=}")

# SystemRandom exposes the full random.Random API, backed by os.urandom
sys_random = secrets.SystemRandom()

secure_randint = sys_random.randint(1, 6)  # inclusive on both ends
print(f"{secure_randint=}")

secure_randrange = sys_random.randrange(0, 100, 5)  # step of 5, stop excluded
print(f"{secure_randrange=}")

secure_uniform = sys_random.uniform(0.0, 1.0)
print(f"{secure_uniform=}")

# choices = with replacement (any element can be chosen more than once)
secure_choices = sys_random.choices(choices, k=3)
print(f"{secure_choices=}")

# sample = without replacement (each element can only be chosen once)
secure_sample = sys_random.sample(choices, k=3)
print(f"{secure_sample=}")

shuffled = choices.copy()
sys_random.shuffle(shuffled)  # in place
print(f"{shuffled=}")

# seed() is a no-op on SystemRandom, so results are never reproducible
sys_random.seed(42)
print(f"{sys_random.randint(1, 100)=} (differs every run despite seed)")
