import numpy as np
from typing import Any, Tuple


def numpy_random(seed: int = 42) -> np.ndarray:
    """
    Generate a random array using numpy's random module.

    Args:
        seed (int): Seed for the random number generator. Setting the seed ensures
                    that the random numbers generated are reproducible. This is useful
                    for debugging and testing purposes.

    Returns:
        np.ndarray: Random array of shape (3, 3).
    """
    np.random.seed(seed)
    return np.random.rand(3, 3)


def numpy_linspace(start: float, stop: float, num: int) -> np.ndarray:
    """
    Generate a linearly spaced array using numpy's linspace module.

    Args:
        start (float): Start of the interval.
        stop (float): End of the interval.
        num (int): Number of samples to generate.

    Returns:
        np.ndarray: Linearly spaced array.
    """
    return np.linspace(start, stop, num)


def numpy_arange(start: int, stop: int, step: int) -> np.ndarray:
    """
    Generate an array with a range of values using numpy's arange module.

    Args:
        start (int): Start of the interval.
        stop (int): End of the interval.
        step (int): Step size between values.

    Returns:
        np.ndarray: Array with a range of values.
    """
    return np.arange(start, stop, step)


def numpy_array(data: Any) -> np.ndarray:
    """
    Create a numpy array from a given data.

    Args:
        data (Any): Input data to convert to numpy array.

    Returns:
        np.ndarray: Numpy array created from input data.
    """
    return np.array(data)


def numpy_reshape(array: np.ndarray, new_shape: Tuple[int, int]) -> np.ndarray:
    """
    Reshape a given numpy array to a new shape.

    Args:
        array (np.ndarray): Input array to reshape.
        new_shape (Tuple[int, int]): New shape for the array.

    Returns:
        np.ndarray: Reshaped array.
    """
    return array.reshape(new_shape)


def numpy_dot(array1: np.ndarray, array2: np.ndarray) -> np.ndarray:
    """
    Compute the dot product of two arrays.

    Args:
        array1 (np.ndarray): First input array.
        array2 (np.ndarray): Second input array.

    Returns:
        np.ndarray: Dot product of the two arrays.
    """
    return np.dot(array1, array2)


def numpy_sum(array: np.ndarray) -> float:
    """
    Compute the sum of all elements in a numpy array.

    Args:
        array (np.ndarray): Input array.

    Returns:
        float: Sum of all elements in the array.
    """
    return np.sum(array)


def numpy_mean(array: np.ndarray) -> float:
    """
    Compute the mean of all elements in a numpy array.

    Args:
        array (np.ndarray): Input array.

    Returns:
        float: Mean of all elements in the array.
    """
    return np.mean(array)


def numpy_std(array: np.ndarray) -> float:
    """
    Compute the standard deviation of all elements in a numpy array.

    Args:
        array (np.ndarray): Input array.

    Returns:
        float: Standard deviation of all elements in the array.
    """
    return np.std(array)


def numpy_transpose(array: np.ndarray) -> np.ndarray:
    """
    Compute the transpose of a numpy array.

    Args:
        array (np.ndarray): Input array.

    Returns:
        np.ndarray: Transposed array.
    """
    return np.transpose(array)


if __name__ == "__main__":
    print(f"\n{numpy_random()=}")
    print(f"\n{numpy_linspace(0, 10, 5)=}")
    print(f"\n{numpy_arange(0, 10, 2)=}")
    print(f"\n{numpy_array([1, 2, 3, 4, 5])=}")
    print(f"\n{numpy_reshape(np.array([1, 2, 3, 4, 5, 6]), (2, 3))=}")
    print(f"\n{numpy_dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))=}")
    print(f"\n{numpy_sum(np.random.rand(5))=}")
    print(f"\n{numpy_mean(np.random.rand(5))=}")
    print(f"\n{numpy_std(np.random.rand(5))=}")
    print(f"\n{numpy_transpose(np.random.rand(2, 3))=}")
