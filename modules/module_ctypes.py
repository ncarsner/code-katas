import ctypes
from ctypes import c_int, c_double, c_char_p, Structure, c_void_p, c_float, c_long
# from ctypes import CDLL, POINTER, byref, c_char, c_uint, c_size_t, c_wchar_p, c_bool, c_short
# from ctypes import c_longlong, c_ulong, c_ushort, c_uint64, c_int64, c_uint32, c_int32
# from ctypes import c_int8, c_uint8, c_int16, c_uint16, c_int32, c_uint32, c_int64, c_uint64
# from ctypes import c_void, c_size_t, c_ssize_t, c_longdouble, c_longlong, c_ulonglong
# from ctypes import c_wchar, c_wchar_p, c_char16, c_char32
from typing import List
import platform
import random

"""
The `ctypes` module allows calling functions in DLLs/shared libraries and manipulating C data types in Python.

This module demonstrates:
- Interfacing with C libraries for high-performance computations.
- Reading/writing binary data structures (e.g., for custom file formats).
- Efficient memory sharing between Python and C code.
"""


def c_sqrt(value: float) -> float:
    """
    Calculates the square root of a number using the C math library.

    Args:
        value (float): The number to compute the square root of.

    Returns:
        float: The square root of the input value.

    Raises:
        OSError: If the math library cannot be loaded.
    """
    try:
        # Load the standard C math library
        if platform.system() == "Windows":
            math_lib = ctypes.CDLL("msvcrt.dll")
        else:
            math_lib = ctypes.CDLL("libm.so.6")
        sqrt_func = math_lib.sqrt
        sqrt_func.argtypes = [c_double]
        sqrt_func.restype = c_double
        return sqrt_func(value)
    except Exception as e:
        raise OSError(f"Could not load C math library: {e}")


class EmployeeRecord(Structure):
    """
    Represents an employee record as a C struct for efficient binary storage.
    """

    _fields_ = [("id", c_int), ("salary", c_double), ("name", c_char_p)]


def pack_employee(emp_id: int, salary: float, name: str) -> bytes:
    """
    Packs employee data into a binary format using ctypes Structure.

    Args:
        emp_id (int): Employee ID.
        salary (float): Employee salary.
        name (str): Employee name.

    Returns:
        bytes: The packed binary data.
    """
    emp = EmployeeRecord(emp_id, salary, name.encode("utf-8"))
    return bytes(emp)


def unpack_employee(data: bytes) -> EmployeeRecord:
    """
    Unpacks binary data into an EmployeeRecord.

    Args:
        data (bytes): The binary data.

    Returns:
        EmployeeRecord: The unpacked employee record.
    """
    emp = EmployeeRecord.from_buffer_copy(data)
    return emp


def increment_array(arr: List[int]) -> List[int]:
    """
    Simulates passing an array to a C function that increments each element.

    Args:
        arr (List[int]): Input array of integers.

    Returns:
        List[int]: Array with each element incremented by 1.
    """
    # Create a ctypes array
    ArrayType = c_int * len(arr)
    c_array = ArrayType(*arr)

    # Simulate a C function that increments each element
    for i in range(len(arr)):
        c_array[i] += 1

    return list(c_array)


# Using c_void_p to share a memory buffer between Python and C
def allocate_and_fill_buffer(size: int) -> c_void_p:
    """
    Allocates a raw memory buffer and fills it with sequential integers.
    Useful for passing large data blocks to C libraries (e.g., for analytics or ETL).

    Args:
        size (int): Number of integers to allocate.

    Returns:
        c_void_p: Pointer to the allocated buffer.
    """
    # Allocate a buffer of c_ints
    buffer_type = c_int * size
    buffer = buffer_type()
    for i in range(size):
        buffer[i] = i + 1  # Fill with 1, 2, ..., size

    # Cast to void pointer for generic C API compatibility
    return ctypes.cast(buffer, c_void_p)


# Preparing a buffer for a C analytics library
def c_void_p_buffer():
    # In real BI/analytics scenarios, buf_ptr would be passed to a C/C++ DLL for fast processing
    size = 5
    buf_ptr = allocate_and_fill_buffer(size)
    print(f"Allocated buffer of {size} integers at address: {buf_ptr.value}")


def sum_large_numbers(numbers: List[int]) -> int:
    """
    Sums a list of large integers using c_long for compatibility with C libraries.
    Useful for BI/analytics scenarios where integer overflows must be avoided.

    Args:
        numbers (List[int]): List of integers to sum.

    Returns:
        int: The sum as a Python integer.
    """
    total = c_long(0)
    for n in numbers:
        total.value += c_long(n).value
    return total.value


def normalize_floats(data: List[float]) -> List[float]:
    """
    Normalizes a list of floats to the range [0, 1] using c_float for efficient memory usage.
    Useful for BI/analytics scenarios such as preparing data for machine learning or visualization.

    Args:
        data (List[float]): List of float values.

    Returns:
        List[float]: Normalized float values in [0, 1].
    """
    if not data:
        return []

    min_val = c_float(min(data))
    max_val = c_float(max(data))
    range_val = (
        c_float(max_val.value - min_val.value)
        if max_val.value != min_val.value
        else c_float(1.0)
    )

    # Use c_float for each element to simulate C-style float processing
    normalized = []
    for val in data:
        norm = c_float((val - min_val.value) / range_val.value)
        normalized.append(norm.value)
    return normalized


def troubleshoot_ctypes():
    """
    Prints common troubleshooting tips for using ctypes.

    - Ensure correct library path and name.
    - Match argument and return types with C function signatures.
    - Use try/except for error handling.
    - Use Structure for binary data and ensure correct field order and types.
    """
    print("Troubleshooting ctypes:")
    print("- Check library paths and names (platform-specific).")
    print("- Set argtypes and restype for each function.")
    print("- Use try/except to catch OSError or AttributeError.")
    print("- For Structures, ensure field order and types match C definition.")
    print("- Use from_buffer_copy to unpack binary data safely.")


if __name__ == "__main__":
    # Calling a standard C library function (e.g., sqrt from math library)
    base = random.randint(2, 100)
    print(f"\nC sqrt ({base}): {c_sqrt(base)}")

    # Defining and using a C struct for binary data manipulation
    salary = random.randrange(65000, 235001, 500)
    employee = random.choice(["Alex", "Blake", "Chris", "Dylan", "Elliott"])
    packed = pack_employee(101, salary, employee)
    emp = unpack_employee(packed)
    print(f"\nEmployee: id={emp.id}, salary={emp.salary}, name={emp.name.decode()}")

    # Sharing memory with C code (simulate a C function that modifies an array)
    arr = [random.randint(1, 10) for _ in range(3)]
    print(f"\nIncremented {arr} array: {increment_array(arr)}\n")

    # Troubleshooting tips
    troubleshoot_ctypes()
