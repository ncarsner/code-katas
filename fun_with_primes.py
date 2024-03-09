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
    # 150_001,
    # 586_711,
    # 1_053_179,
    # 1_534_853,
    # 2_027_549,
    # 2_529_619,
    # 3_038_039,
    # 3_552_839,
    # 4_070_873,
    # 4_594_489,
    # 5_121_511,
    # 5_653_211,
    # 6_187_457,
    # 6_724_511,
    # 7_263_353,
    # 7_806_661,
    # 8_351_129,
    # 8_897_821,
    # 9_447_539,
    10_000_019,  # 3,010,306 digits / 2:22 time to calculate
    # 10_764_979,
    # 11_535_281,
    # 12_307_487,
    # 13_084_147,
    # 13_862_741,
    # 14_644_709,
    # 15_430_313,
    # 16_215_917,
    # 17_003_663,
    # 17_793_703,
    # 18_587_839,
    # 19_382_959,
    # 20_179_069,
    # 20_979_671,
    # 21_779_497,
    # 22_583_287,
    # 23_386_411,
    # 24_192_737,
    25_000_009,  # 7,525,753 digits / 15:12 time to calculate
    26_290_171,
    27_581_471,  # 8,302,851 digits / 19:03 time to calculate
    # 28_877_153,
    # 30_175_169,
    # 31_478_647,
    32_783_791,  # 9,868,905 / 27:54
    34_092_731,  # 10,262,935 / 28:16
    35_407_283,
    36_723_041,  # 11,054,737 / 33:52
    38_040_749,
    39_355_429,
    40_678_427,
    42_005_273,
    43_333_139,  # 13,044,575 / 43:43
    44_661_829,
    45_990_713,
    47_324_747,
    48_663_887,  # 14,649,290 / 55:17
]


def format_time(milliseconds):
    """Function to format time in suitable increments."""
    if milliseconds >= 60000:
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


x = 25_000_001
y = 50_000_001


def get_primes_in_range(x=x, y=y):
    # Generate all prime numbers between 101 and 5000
    all_primes = primes_in_range(x, y)

    # Select 20 almost-evenly spaced primes from the list of all primes
    almost_even_primes = almost_evenly_spaced_primes(all_primes)
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
