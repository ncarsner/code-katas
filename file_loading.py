import time
import mmap

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def read_file_regular(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            pass  # Process each line if needed

@timing_decorator
def read_file_mmap(file_path):
    with open(file_path, 'r+b') as file:
        mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        for line in iter(mmapped_file.readline, b""):
            pass  # Process each line if needed
        mmapped_file.close()

if __name__ == "__main__":
    file_path = 'path_to_your_file.txt'
    read_file_regular(file_path)
    read_file_mmap(file_path)