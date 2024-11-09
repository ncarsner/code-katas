import numpy as np
import time
from functools import wraps


# Define a timing decorator
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds"
        )
        return result

    return wrapper


# Create an A x B dimension array of tuples
A = 200
B = 200
array_of_tuples = [(i, i + 1, i + 2) for i in range(1, A * B * 3 + 1, 3)]

# Reshape the array of tuples into A x B x 3
reshaped_array_of_tuples = [array_of_tuples[i * B : (i + 1) * B] for i in range(A)]

# Convert to a numpy array
array_2d = np.array(reshaped_array_of_tuples)

# Print the numpy array and its shape
# print(f"2D numpy array:\n{array_2d}\n")
print(f"Shape of array: {array_2d.shape}")


# Define a calculation function
@timing_decorator
def calculation_on_tuples(arr):
    result = []
    for row in arr:
        result_row = []
        for tup in row:
            result_row.append(tuple(x * 2 for x in tup))
        result.append(result_row)
    return result


@timing_decorator
def calculation_on_numpy_array(arr):
    return arr * 2


# Apply the calculation function to both objects
result_tuples = calculation_on_tuples(reshaped_array_of_tuples)
# print(f"Calculation result on array of tuples:\n{result_tuples}\n")

result_numpy_array = calculation_on_numpy_array(array_2d)
# print(f"Calculation result on numpy array:\n{result_numpy_array}\n")
