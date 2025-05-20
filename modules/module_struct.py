import struct
from typing import List, Tuple
import random

"""
Python's built-in `struct` module is useful for reading/writing binary data, such as from legacy systems, network streams, or binary files.

This module provides:
- Packing and unpacking of records (e.g., for exporting/importing fixed-width binary data)
- Reading binary files with known record formats
- Writing binary data for interoperability with other systems
"""


def pack_employee_record(emp_id: int, salary: float, name: str) -> bytes:
    """
    Packs an employee record into binary format.

    Args:
        emp_id (int): Employee ID (integer)
        salary (float): Employee salary
        name (str): Employee name (max 20 chars)

    Returns:
        bytes: Packed binary data

    Example:
        >>> pack_employee_record(101, 75000.0, "Alex")
    """
    # 'i' = int (4 bytes), 'd' = double (8 bytes), '20s' = 20-byte string
    name_bytes = name.encode('utf-8')[:20]
    name_bytes = name_bytes.ljust(20, b'\x00')  # pad to 20 bytes
    packed = struct.pack('i d 20s', emp_id, salary, name_bytes)
    return packed


def unpack_employee_record(data: bytes) -> Tuple[int, float, str]:
    """
    Unpacks a binary employee record.

    Args:
        data (bytes): Packed binary data (32 bytes)

    Returns:
        Tuple[int, float, str]: (emp_id, salary, name)

    Example:
        >>> unpack_employee_record(b'...')
    """
    emp_id, salary, name_bytes = struct.unpack('i d 20s', data)
    name = name_bytes.rstrip(b'\x00').decode('utf-8')
    return emp_id, salary, name


def read_employee_records_from_file(filename: str) -> List[Tuple[int, float, str]]:
    """
    Reads all employee records from a binary file.

    Args:
        filename (str): Path to binary file

    Returns:
        List[Tuple[int, float, str]]: List of employee records

    Example:
        >>> read_employee_records_from_file('employees.dat')
    """
    records = []
    record_size = struct.calcsize('i d 20s')
    with open(filename, 'rb') as f:
        while chunk := f.read(record_size):
            records.append(unpack_employee_record(chunk))
    return records


def write_employee_records_to_file(filename: str, records: List[Tuple[int, float, str]]) -> None:
    """
    Writes employee records to a binary file.

    Args:
        filename (str): Path to binary file
        records (List[Tuple[int, float, str]]): List of employee records

    Example:
        >>> write_employee_records_to_file('employees.dat', [(101, 75000.0, 'Alice')])
    """
    with open(filename, 'wb') as f:
        for emp_id, salary, name in records:
            f.write(pack_employee_record(emp_id, salary, name))


def get_struct_format_info(fmt: str) -> None:
    """
    Prints information about a struct format string.

    Args:
        fmt (str): struct format string

    Example:
        >>> get_struct_format_info('i d 20s')
    """
    print(f"Format: {fmt}")
    print(f"Size: {struct.calcsize(fmt)} bytes")
    example_bytes = b'abc'.ljust(20, b'\x00')
    print(f"Example packed: {struct.pack(fmt, 1, 2.0, example_bytes)}")


if __name__ == "__main__":
    EMPLOYEES = ["Alex", "Blake", "Chris", "Dylan", "Elliott"]
    SALARIES = [random.choice(range(50000, 125001, 5000)) for _ in range(5)]
    random.shuffle(EMPLOYEES)
    random.shuffle(SALARIES)

    emp = (101, SALARIES[0], EMPLOYEES[0])
    packed = pack_employee_record(*emp)
    print("Packed bytes:", packed)
    unpacked = unpack_employee_record(packed)
    print("Unpacked record:", unpacked)

    # Write and read records
    employees = [
        (101, SALARIES[0], EMPLOYEES[0]),
        (102, SALARIES[1], EMPLOYEES[1]),
        (103, SALARIES[2], EMPLOYEES[2]),
    ]
    write_employee_records_to_file('employees.dat', employees)
    loaded = read_employee_records_from_file('employees.dat')
    print("Loaded records:", loaded)

    # Struct format info
    get_struct_format_info('i d 20s')