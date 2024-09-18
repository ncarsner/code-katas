import decorators

num = 100_000

@decorators.timer
def primes_filters(num):
    primes = [
        x for x in range(2, num)
        if not any(x % y == 0 for y in range(2, int(x / 2) + 1))
    ]
    return primes


print(primes_filters(num)[-3:])
print(f"{len(primes_filters(num)):,}")
