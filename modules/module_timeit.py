import timeit
import traceback


def timeit_simple():
    setup_code = "from math import sqrt"
    test_code = """
def test():
    for i in range(100):
        sqrt(i)
"""
    times = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
    print(f"times= {round(times, 8)} seconds")


def timeit_multiple():
    setup_code = "from math import sqrt"
    test_code = """
def test():
    for i in range(100):
        sqrt(i)
"""
    times = timeit.repeat(stmt=test_code, setup=setup_code, repeat=5, number=1000)
    print(f"times={[round(t, 8) for t in times]}")


def timer_object():
    setup_code = "from math import sqrt"
    test_code = """
def test():
    for i in range(100):
        sqrt(i)
"""
    timer = timeit.Timer(stmt=test_code, setup=setup_code)
    times = timer.timeit(number=1000)
    print(f"times={round(times, 8)} seconds")


def time_multiple():
    setup_code = "from math import sqrt"
    test_code = """
def test():
    for i in range(100):
        sqrt(i)
"""
    timer = timeit.Timer(stmt=test_code, setup=setup_code)
    times = timer.repeat(repeat=5, number=1000)
    print(f"time={[round(t, 8) for t in times]}")


def timeit_default_timer():
    """
    Use default_timer to measure elapsed time.
    """
    start_time = timeit.default_timer()
    for i in range(1_000_000):
        pass
    elapsed = timeit.default_timer() - start_time
    print(f"default_timer elapsed time: {round(elapsed, 8)} seconds")


def timeit_autorange():
    """
    Automatically determine the number of loops.
    """
    setup_code = "from math import sqrt"
    test_code = """
def test():
    for i in range(100):
        sqrt(i)
"""
    timer = timeit.Timer(stmt=test_code, setup=setup_code)
    number, time_taken = timer.autorange()
    print(
        f"autorange determined number={number:,}, time_taken={round(time_taken, 8)} seconds"
    )


def timeit_print_exc():
    """
    Advantage over the standard traceback is that source lines in the compiled template will be displayed.
    The optional file argument directs where the traceback is sent; it defaults to sys.stderr
    """
    try:
        1 / 0
    except ZeroDivisionError:
        traceback.print_exc()


if __name__ == "__main__":
    timeit_simple()
    timeit_multiple()
    timer_object()
    time_multiple()
    timeit_autorange()
    timeit_print_exc()
    timeit_default_timer()
