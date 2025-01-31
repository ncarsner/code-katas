import random
import time
import tracemalloc


def http_status_code_handler(status_code):
    match status_code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"


def http_status_code_handler_v2(status_code):
    status_codes = {
        200: "OK",
        201: "Created",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
    }
    return status_codes.get(status_code, "Unknown Status Code")


# Function to measure execution time
def measure_execution_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    return result, end_time - start_time


# Function to measure memory usage
def measure_memory_usage(func, *args):
    tracemalloc.start()
    result = func(*args)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result, current, peak


# Example usage
if __name__ == "__main__":
    status_code = random.choice([200, 201, 400, 401, 403, 404, 500, 999])

    # Measure execution time
    result_match, time_match = measure_execution_time(
        http_status_code_handler, status_code
    )
    result_dict, time_dict = measure_execution_time(
        http_status_code_handler_v2, status_code
    )

    print(f"Match-case result: {result_match}, Execution time: {time_match:.10f} seconds")
    print(f"Dictionary result: {result_dict}, Execution time: {time_dict:.10f} seconds")

    # Measure memory usage
    result_match, current_match, peak_match = measure_memory_usage(
        http_status_code_handler, status_code
    )
    result_dict, current_dict, peak_dict = measure_memory_usage(
        http_status_code_handler_v2, status_code
    )

    print(f"""Match-case result: {result_match},
          Current memory usage: {current_match} bytes,
          Peak memory usage: {peak_match} bytes""")
    print(f"""Dictionary result: {result_dict},
          Current memory usage: {current_dict} bytes,
          Peak memory usage: {peak_dict} bytes""")


def user_role_handler(role):
    match role:
        case "admin":
            return "Access to all resources"
        case "editor":
            return "Access to edit content"
        case "viewer":
            return "Access to view content"
        case _:
            return "No access"


def file_extension_handler(extension):
    match extension:
        case "txt":
            return "Text File"
        case "jpg" | "jpeg":
            return "JPEG Image"
        case "png":
            return "PNG Image"
        case "pdf":
            return "PDF Document"
        case _:
            return "Unknown File Type"


# Example usage
if __name__ == "__main__":
    print(http_status_code_handler(200))  # Output: OK
    print(http_status_code_handler(404))  # Output: Not Found
    print(user_role_handler("admin"))  # Output: Access to all resources
    print(user_role_handler("guest"))  # Output: No access
    print(file_extension_handler("txt"))  # Output: Text File
    print(file_extension_handler("mp3"))  # Output: Unknown File Type
