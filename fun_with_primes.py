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


print_incremental_primes(500, 50)
