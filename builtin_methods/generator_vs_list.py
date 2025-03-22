import sys
import time

# Using a list
start_time = time.time()
list_comp = [i for i in range(100_000_000)]
list_time = time.time() - start_time
list_size = sys.getsizeof(list_comp)

# Using a generator
start_time = time.time()
gen_exp = (i for i in range(100_000_000))
gen_time = time.time() - start_time
gen_size = sys.getsizeof(gen_exp)

print(f"List comprehension took {list_time:.2f} seconds and uses {list_size:,} bytes")
print(f"Generator expression took {gen_time:.2f} seconds and uses {gen_size:,} bytes")
