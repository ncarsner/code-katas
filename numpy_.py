import numpy as np

# Example 1: Creating Arrays
array_1d = np.array([1, 2, 3, 4, 5])
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("1D Array:", array_1d)
print("2D Array:\n", array_2d)

# Example 2: Array Operations
array_sum = array_1d + 10
print("Array after adding 10:", array_sum)

array_product = array_1d * 2
print("Array after multiplying by 2:", array_product)

# Example 3: Array Slicing
sliced_array = array_1d[1:4]
print("Sliced Array:", sliced_array)

# Example 4: Array Reshaping
reshaped_array = array_2d.reshape(3, 2)
print("Reshaped Array:\n", reshaped_array)

# Example 5: Array Aggregations
array_mean = np.mean(array_1d)
array_sum = np.sum(array_1d)
# print("Mean of array:", array_mean)
print(f"{array_mean=}")
# print("Sum of array:", array_sum)
print(f"{array_sum=}")

# Example 6: Array Broadcasting
array_broadcast = array_1d + np.array([1, 2, 3, 4, 5])
# print("Broadcasted Array:", array_broadcast)
print(f"{array_broadcast=}")

# Example 7: Boolean Indexing
bool_index = array_1d > 2
filtered_array = array_1d[bool_index]
print("Filtered Array (elements > 2):", filtered_array)
print(f"{filtered_array=}")

# Example 8: Element-wise Operations
array_squared = np.square(array_1d)
print("Squared Array:", array_squared)

# Example 9: Matrix Multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix_a, matrix_b)
print("Matrix Product:\n", matrix_product)

# Example 10: Random Arrays
random_array = np.random.rand(3, 3)
# print("Random Array:\n", random_array)
print(f"{random_array=}")
