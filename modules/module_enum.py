from enum import Enum, IntEnum, Flag, auto, unique, CONTINUOUS
import random


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print("Enum:")
for color in Color:
    print(f"{color.name} = {color.value}")


class StatusCode(IntEnum):
    SUCCESS = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


print("\nIntEnum:")
for status in StatusCode:
    print(f"{status.name} = {status.value}")


class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


print("\nFlag:")
permissions = list(Permission)
user_permission = random.choice(permissions)
for _ in range(random.randint(1, len(permissions) - 1)):
    user_permission |= random.choice(permissions)
print(f"User Permission: {user_permission}")


@unique
class BusinessEntity(Enum):
    CUSTOMER = 1
    PRODUCT = 2
    SALES = 3
    REGION = 4
    EMPLOYEE = 5


print("\nUnique Enum:")
for entity in BusinessEntity:
    print(f"{entity.name} = {entity.value}")


def check_status(status_code):
    if status_code == StatusCode.SUCCESS:
        return "Request was successful."
    elif status_code == StatusCode.NOT_FOUND:
        return "Resource not found."
    elif status_code == StatusCode.SERVER_ERROR:
        return "Server encountered an error."
    else:
        return "Unknown status code."


print(f"\n{check_status(StatusCode.SUCCESS)=}")
print(f"{check_status(StatusCode.NOT_FOUND)=}")
print(f"{check_status(StatusCode.SERVER_ERROR)=}")


class SalesCategory(Enum):
    CONTINUOUS = CONTINUOUS

    LOW = 1
    MEDIUM = 2
    HIGH = 3


def categorize_sales(sales_amount):
    if sales_amount < 1000:
        return SalesCategory.LOW
    elif 1000 <= sales_amount < 5000:
        return SalesCategory.MEDIUM
    else:
        return SalesCategory.HIGH


print("\nSales Categorization:")
sales_data = [random.randint(1, 20) * 500 for _ in range(5)]
for sales in sales_data:
    category = categorize_sales(sales)
    print(f"Sales Amount: {sales}, Category: {category.name}")
