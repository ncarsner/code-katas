import time


def fibonacci(n):
    """Recursive function to calculate Fibonacci numbers."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def exponential_time_calculation(n):
    """Function that increases exponentially in time needed to calculate."""
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def format_time(milliseconds):
    """Function to format time in suitable increments."""
    if milliseconds >= 60000:
        minutes, seconds = divmod(milliseconds / 1000, 60)
        return f"{int(minutes)} minutes {seconds:.2f} seconds"
    elif milliseconds >= 1000:
        return f"{milliseconds / 1000:.2f} seconds"
    else:
        return f"{milliseconds:.4f} milliseconds"


for i in range(15,50,5):
    result, execution_time = exponential_time_calculation(i)
    print(f"Fibonacci({i}) = {result:,} | Execution Time: {format_time(execution_time * 1000)}")


n = 30  # Fibonacci sequence number to calculate
# result, execution_time = exponential_time_calculation(n)
# print(f"Fibonacci({n}) = {result}")
# print("Execution Time:", format_time(execution_time * 1000))  # Convert to milliseconds
