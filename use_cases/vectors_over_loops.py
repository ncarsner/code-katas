# import random
import sys
from pathlib import Path

# Add parent directory for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import numpy as np
from decorators import timer


def create_large_nested_array(rows=2_000, cols=2_000):
    """Create a large nested array for performance testing."""
    return [[i * cols + j for j in range(cols)] for i in range(rows)]


array_A = create_large_nested_array()
array_B = create_large_nested_array()


@timer
def list_comprehension_loop():
    # array_A = [[1, 2], [3, 4]]
    # array_B = [[5, 6], [7, 8]]
    result = [
        [array_A[i][0] * array_B[0][j] for j in range(len(array_B[0]))]
        for i in range(len(array_A))
    ]
    # print("Result:", result)


@timer
def vectorized_operations():
    vectored_array_A = np.array(array_A)
    vectored_array_B = np.array(array_B)
    results = vectored_array_A @ vectored_array_B
    # print("Matrix Product:\n", results)


def main():
    list_comprehension_loop()
    vectorized_operations()


if __name__ == "__main__":
    main()
