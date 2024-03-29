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


primes = [
    150_001,  # 45,155 digits / ~30ms time to calculate
    586_711,  # 176,618 digits / ~ 550ms time to calculate
    1_053_179,  # 317,039 digits / ~ 1.75 seconds to calculate
    # 1_534_853,
    # 2_529_619,
    # 5_121_511,
    # 10_000_019,  # 3,010,306 digits / 2:22 time to calculate
    # 25_000_009,  # 7,525,753 digits / 15:12 time to calculate
    # 27_581_471,  # 8,302,851 digits / 19:03 time to calculate
    # 34_092_731,  # 10,262,935 / 28:16
    # 36_723_041,  # 11,054,737 / 33:52
    # 43_333_139,  # 13,044,575 / 43:43
    # 48_663_887,  # 14,649,290 / 55:17
    # 50_000_017,  # 15,051,505 / 1:06:55
    # 62_315_479,  # 18,758,829 / 1:44:14
    # 74_763_967,  # 22,506,197 / 2:30:17
    # 87_332_057,  # 26,289,569 / 3:25:14
    # 100_000_007,  # 30,103,002 / 4:30:40
    # 112_389_727,  # 33,832,680 / 5:40:38
    # 124_865_857, # 37,588,369 / 6:16:17
    # 137_402_539, # 41,362,286 / 7:54:29
    # 150_000_001, # 45,154,500 / 8:45:45
    186_968_443,
    # 224_335_357,
    # 262_022_639,
]

# print(is_prime(150_000_001))

def format_time(milliseconds):
    """Function to format time in suitable increments."""
    if milliseconds >= 3600000:
        hours, remainder = divmod(milliseconds / 1000, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours == 1:
            hour_str = "hour"
        else:
            hour_str = "hours"
        return f"{int(hours)} {hour_str} {int(minutes)} minutes {seconds:.2f} seconds"
    elif milliseconds >= 60000:
        minutes, seconds = divmod(milliseconds / 1000, 60)
        if minutes == 1:
            return f"{int(minutes)} minute {seconds:.2f} seconds"
        else:
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
        return (
            primes_list  # Return all primes if the list is smaller than or equal to 20
        )
    else:
        selected_primes = []
        interval = len(primes_list) / (n - 1)
        for i in range(n):
            index = int(round(i * interval))
            if index < len(primes_list):
                selected_primes.append(primes_list[index])
        return selected_primes


# Function to calculate the length of the prime number
def digit_length_of_prime(num):
    result = 2**num - 1
    result = str(result)
    return len(result)


# Set the maximum number of digits allowed for integer string conversion
sys.set_int_max_str_digits(100_000_000)

x = 150_000_001
y = 300_000_001


def get_primes_in_range(x=x, y=y):
    # Generate all prime numbers between 101 and 5000
    all_primes = primes_in_range(x, y)

    # Select 20 almost-evenly spaced primes from the list of all primes
    almost_even_primes = almost_evenly_spaced_primes(all_primes, n=5)
    return almost_even_primes


# print(get_primes_in_range())


# Loop through the exponents and measure time for each iteration
for exponent in primes:
    start_time = time.time()
    prime_check = is_prime(exponent)
    length = digit_length_of_prime(exponent)
    duration = time.time() - start_time
    print(
        f"{exponent:,} {prime_check} -- len: {length:,} -- {format_time(duration * 1000)}"
    )
