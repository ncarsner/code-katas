def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_distances():
    primes = [p for p in range(1, 550) if is_prime(p)]

    for i, prime in enumerate(primes):
        prev_distance = prime - primes[i - 1] if i > 0 else 0
        next_distance = primes[i + 1] - prime if i < len(primes) - 1 else 0
        tot_distance = prev_distance + next_distance

        print(f"{i+1} - Prime: {prime}, Prev: {prev_distance}, Next: {next_distance}, Total: {tot_distance}")

prime_distances()
