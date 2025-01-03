import time
from tqdm import tqdm
import json
from datetime import datetime


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time:.3f} seconds")
        return result

    return wrapper


def progress_bar(func):
    def wrapper(*args, **kwargs):
        # Assuming func returns an iterable
        result = func(*args, **kwargs)
        total_iterations = len(result) if hasattr(result, "__len__") else None
        with tqdm(total=total_iterations, desc=f"{func.__name__} Progress") as pbar:
            for item in result:
                yield item
                pbar.update(1)

    return wrapper


def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Args: {args}, Kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Value returned: {result}")
        return result

    return wrapper


def log_to_json(func):
    def wrapper(*args, **kwargs):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "function": func.__name__,
            "args": args,
            "kwargs": kwargs,
        }
        result = func(*args, **kwargs)
        log_entry["result"] = result

        with open("logging.json", "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")

        return result

    return wrapper
