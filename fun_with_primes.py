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

        print(f"{i+1} - Prime: {prime}, Prev: {prev_distance}, Next: {next_distance}, Total: {tot_distance}")

prime_distances()



# def is_prime(n):
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

def count_primes_up_to_500():
    prime_count = 0
    for num in range(1, 501):
        if is_prime(num):
            prime_count += 1
        if num % 10 == 0:
            start_range = num - 9
            end_range = num
            print(f"Range {start_range}-{end_range}: {prime_count} primes")
            prime_count = 0

count_primes_up_to_500()
