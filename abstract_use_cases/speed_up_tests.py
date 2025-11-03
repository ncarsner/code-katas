from collections import defaultdict, Counter
import dis
import timeit
import random


# defaultdict implementation
def frequency_defaultdict(text):
    ret = defaultdict(int)
    for char in text.lower():
        ret[char] += 1
    return ret


# Counter implementation
def frequency_counter(text):
    return Counter(text.lower())


if __name__ == "__main__":
    with open("./data/raw/large_file.txt", "r") as file:
        test_text = file.read()

    sample_size = 10**random.randint(2, 5)  # Random sample size between 10^2 and 10^6
    test_text = test_text[:sample_size]  # Use a smaller sample for testing

    # Ensure results are the same
    assert frequency_defaultdict(test_text) == frequency_counter(test_text)

    # Benchmark
    print(f"Benchmarking sample size: {sample_size:,}")
    print(f"Default dict: {timeit.timeit(lambda: frequency_defaultdict(test_text), number=10000):.5f}")
    print(f"Counter: {timeit.timeit(lambda: frequency_counter(test_text), number=10000):.5f}")

    # Bytecode disassembly
    disassembly = False
    if disassembly:
        print("\nFrequency DefaultDict Disassembly:")
        dis.dis(frequency_defaultdict)

        print("\nFrequency Counter Disassembly:")
        dis.dis(frequency_counter)
