import random
import sys
import time


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_distances():
    primes = [p for p in range(1, 501) if is_prime(p)]

    for i, prime in enumerate(primes):
        prev_distance = prime - primes[i - 1] if i > 0 else 0
        next_distance = primes[i + 1] - prime if i < len(primes) - 1 else 0
        tot_distance = prev_distance + next_distance

        print(
            f"{i+1} - Prime: {prime}, Prev: {prev_distance}, Next: {next_distance}, Total: {tot_distance}"
        )


# prime_distances()


def count_primes_up_to_500():
    prime_count = 0
    for num in range(1, 501):
        if is_prime(num):
            prime_count += 1
        if num % 10 == 0:
            range_start = num - 9
            range_end = num
            print(f"Range {range_start}-{range_end}: {prime_count} primes")
            prime_count = 0


# count_primes_up_to_500()


def print_incremental_primes(n, increment):
    for num in range(1, n + 1):
        if num % increment == 1:
            primes = []
            range_start = num
        if is_prime(num):
            primes.append(num)
        if num % increment == 0:
            # range_start = num - 9
            range_end = num
            print(
                f"Range {range_start}-{range_end}: Primes - {', '.join(map(str,primes))}"
            )


# print_incremental_primes(500, 50)


# 13_466_917 contains 4,053,946 digits

x = 150_001
y = 10_000_001

primes = [
    6_384_211,
    26_284_211,
    31521053,
    41994737,
    45136843,
    47231_579,
    71321_053,
    80747_369,
    85984_211,
    99600_001,
    101_694_737,
    106_931_579,
    115_310_527,
    145_684_211,
    180_247_369,
    184_436_843,
    206_431_579,
    224_236_843,
    226_331_579,
    238_900_001,
]


def format_time(milliseconds):
    """Function to format time in suitable increments."""
    if milliseconds >= 60000:
        minutes, seconds = divmod(milliseconds / 1000, 60)
        return f"{int(minutes)} minutes {seconds:.2f} seconds"
    elif milliseconds >= 1000:
        return f"{milliseconds / 1000:.2f} seconds"
    else:
        return f"{milliseconds:.3f} milliseconds"


def generate_primes(n, start, end):
    """Function to generate n prime numbers within the range [start, end]."""
    primes = []
    num = start
    while len(primes) < n and num <= end:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def primes_in_range(start, end):
    """Function to generate all prime numbers between start and end."""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def almost_evenly_spaced_primes(primes_list, n=20):
    """Function to select almost-evenly spaced primes from a list of primes."""
    if len(primes_list) <= n:
        return primes_list  # Return all primes if the list is smaller than or equal to 20
    else:
        selected_primes = []
        interval = len(primes_list) / (n - 1)
        for i in range(n):
            index = int(round(i * interval))
            if index < len(primes_list):
                selected_primes.append(primes_list[index])
        return selected_primes


# Generate all prime numbers between 101 and 5000
all_primes = primes_in_range(x, y)

# Select 20 almost-evenly spaced primes from the list of all primes
almost_even_primes = almost_evenly_spaced_primes(all_primes)
print(almost_even_primes)






# Function to calculate the length of the prime number
def digit_length_of_prime(num):
    result = 2**num - 1
    result = str(result)
    return len(result)


# Set the maximum number of digits allowed for integer string conversion
sys.set_int_max_str_digits(100_000_000)

# Loop through the exponents and measure time for each iteration
# for exponent in generate_primes(20, x, y):
#     start_time = time.time()
#     prime_check = is_prime(exponent)
#     length = digit_length_of_prime(exponent)
#     duration = time.time() - start_time
#     print(f"{exponent:,} {prime_check} -- len: {length:,} -- {format_time(duration * 1000)}")
