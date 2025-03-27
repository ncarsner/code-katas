import random
import statistics


def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    Args:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def sum_of_list(lst):
    """
    Calculate the sum of all elements in a list using recursion.

    Args:
    lst (list): The list of numbers to sum up.

    Returns:
    int: The sum of all elements in the list.
    """
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_of_list(lst[1:])


def find_max(lst):
    """
    Find the maximum element in a list using recursion.

    Args:
    lst (list): The list of numbers to find the maximum from.

    Returns:
    int: The maximum element in the list.
    """
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest


def flatten_list(nested_list):
    """
    Flatten a nested list using recursion.

    Args:
    nested_list (list): The nested list to flatten.

    Returns:
    list: A flattened list.
    """
    if not nested_list:
        return []
    if isinstance(nested_list[0], list):
        return flatten_list(nested_list[0]) + flatten_list(nested_list[1:])
    else:
        return [nested_list[0]] + flatten_list(nested_list[1:])


def has_permission(user_permissions, target_permission):
    """
    Check if a user has a specific permission in a nested permission structure.

    Args:
    user_permissions (list): The list of permissions (can be nested).
    target_permission (str): The permission to check for.

    Returns:
    bool: True if the user has the target permission, False otherwise.
    """
    if not user_permissions:
        return False
    if target_permission in user_permissions:
        return True
    for permission in user_permissions:
        if isinstance(permission, list) and has_permission(
            permission, target_permission
        ):
            return True
    return False


def find_outliers(data, lower_bound, upper_bound):
    """
    Identify outliers in a list of numbers using recursion.

    Args:
    data (list): The list of numbers to check for outliers.
    lower_bound (int): The lower bound of the acceptable range.
    upper_bound (int): The upper bound of the acceptable range.

    Returns:
    list: A list of outliers.
    """
    if not data:
        return []
    head, *tail = data
    if head < lower_bound or head > upper_bound:
        return [head] + find_outliers(tail, lower_bound, upper_bound)
    else:
        return find_outliers(tail, lower_bound, upper_bound)


def find_outliers_std(data, num_std_dev=1, use_median=False):
    """
    Identify outliers in a list of numbers based on standard deviations from the mean or median.

    Args:
    data (list): The list of numbers to check for outliers.
    num_std_dev (int): The number of standard deviations to use for identifying outliers.
    use_median (bool): Whether to use the median instead of the mean for calculating outliers.

    Returns:
    list: A list of outliers.
    """
    if not data:
        return []

    if use_median:
        center = statistics.median(data)
    else:
        center = statistics.mean(data)

    std_dev = statistics.stdev(data)
    lower_bound = center - num_std_dev * std_dev
    upper_bound = center + num_std_dev * std_dev

    return [x for x in data if x < lower_bound or x > upper_bound]



if __name__ == "__main__":
    INT = random.randint(1, 10)
    LIST = [random.randint(1, 100) for _ in range(5)]
    NESTED_LIST = [[random.randint(1, 10) for _ in range(2)] for _ in range(3)]

    print(f"Factorial of {INT}: {factorial(INT):,}")
    print(f"Sum of list {LIST}: {sum_of_list(LIST):,}")
    print(f"Max of list {LIST}: {find_max(LIST):,}")
    print(f"Flatten nested list {NESTED_LIST}:", flatten_list(NESTED_LIST),)

    user_permissions = ["read", ["write", ["execute", "delete"]]]
    print("\nUser has 'delete' permission:", has_permission(user_permissions, "delete"))
    print("User has 'admin' permission:", has_permission(user_permissions, "admin"))

    OUTLIER_LIST = [random.randint(1, 100) for _ in range(10)]
    LOWER_BOUND = 20 * statistics.mean(OUTLIER_LIST) / 100  # 20th percentile 
    UPPER_BOUND = 80 * statistics.mean(OUTLIER_LIST) / 100  # 80th percentile
    print(f"\nOutliers in {OUTLIER_LIST} outside range {LOWER_BOUND}-{UPPER_BOUND}:",
          find_outliers(OUTLIER_LIST, LOWER_BOUND, UPPER_BOUND))

    OUTLIER_LIST_STD = [random.randint(1, 100) for _ in range(10)]
    print(f"\nOutliers in {OUTLIER_LIST_STD} using mean and 1 std dev:",
            sorted(find_outliers_std(OUTLIER_LIST_STD, num_std_dev=1)))
    print(f"Outliers in {OUTLIER_LIST_STD} using median and 1 std dev:",
            find_outliers_std(OUTLIER_LIST_STD, num_std_dev=1, use_median=True))
