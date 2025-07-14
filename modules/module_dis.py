import dis
from typing import Callable, Any

"""
Python's built-in `dis` module disassembles Python bytecode. Practical uses are to optimizing code, understanding performance bottlenecks, and troubleshooting unexpected behavior.
"""


def analyze_function_bytecode(func: Callable[..., Any]) -> None:
    """
    Disassembles and prints the bytecode of a given function.

    Args:
        func: The function to analyze.

    Example:
        def sample():
            return sum([i for i in range(10)])

        analyze_function_bytecode(sample)
    """
    print(f"Disassembly of function: {func.__name__}")
    dis.dis(func)
    print("-" * 40)


def compare_functions(func1: Callable[..., Any], func2: Callable[..., Any]) -> None:
    """
    Compares the bytecode of two functions side by side.

    Args:
        func1: The first function.
        func2: The second function.

    Example:
        def list_sum():
            return sum([i for i in range(100)])

        def gen_sum():
            return sum(i for i in range(100))

        compare_functions(list_sum, gen_sum)
    """
    print(f"Comparing {func1.__name__} and {func2.__name__} bytecode:")
    print(f"\n{func1.__name__}:")
    dis.dis(func1)
    print(f"\n{func2.__name__}:")
    dis.dis(func2)
    print("-" * 40)


def get_instruction_list(func: Callable[..., Any]) -> list[dis.Instruction]:
    """
    Returns a list of dis.Instruction objects for a function.

    Args:
        func: The function to analyze.

    Returns:
        List of dis.Instruction objects.

    Example:
        def foo(x): return x + 1
        instructions = get_instruction_list(foo)
        for instr in instructions:
            print(instr.opname, instr.argval)
    """
    return list(dis.get_instructions(func))


def print_code_info(func: Callable[..., Any]) -> None:
    """
    Prints detailed code object information for a function.

    Args:
        func: The function to analyze.

    Example:
        def foo(x): return x * 2
        print_code_info(foo)
    """
    code = func.__code__
    print(f"Function: {func.__name__}")
    print(f"  Arg count: {code.co_argcount}")
    print(f"  Variable names: {code.co_varnames}")
    print(f"  Constants: {code.co_consts}")
    print(f"  Names: {code.co_names}")
    print(f"  Bytecode length: {len(code.co_code)}")
    print("-" * 40)


def inefficient_sum(data: list[int]) -> int:
    """Sums a list using a for loop (less efficient)."""
    total = 0
    for value in data:
        total += value
    return total


def efficient_sum(data: list[int]) -> int:
    """Sums a list using the built-in sum (more efficient)."""
    return sum(data)


if __name__ == "__main__":
    # Analyze and compare two sum implementations
    analyze_function_bytecode(inefficient_sum)
    analyze_function_bytecode(efficient_sum)
    compare_functions(inefficient_sum, efficient_sum)

    # Get instruction list for troubleshooting
    instructions = get_instruction_list(inefficient_sum)
    print("Instructions for inefficient_sum:")
    for instr in instructions:
        print(f"{instr.opname:20} {instr.argrepr}")

    # Print code object info
    print_code_info(efficient_sum)
