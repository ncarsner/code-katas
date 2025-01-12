import pickle
import os


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator(n, start=2):
    count = 0
    num = start
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def save_state(filename, state):
    with open(filename, "wb") as f:
        pickle.dump(state, f)


def load_state(filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    return None


def main():
    filename = "prime_state.pkl"
    state = load_state(filename)
    start = state if state is not None else 2

    n = 10  # Number of primes to generate
    primes = list(prime_generator(n, start))

    print(f"Next {n} prime numbers starting from {start}: {primes}")

    # Save the last prime number + 1 as the new start point
    save_state(filename, primes[-1] + 1)


if __name__ == "__main__":
    main()
