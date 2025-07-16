from enum import Enum, IntEnum, Flag, auto, unique, CONTINUOUS
from enum import StrEnum  # type: ignore
import random


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class StatusCode(IntEnum):
    SUCCESS = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


@unique
class BusinessEntity(Enum):
    CUSTOMER = 1
    PRODUCT = 2
    SALES = 3
    REGION = 4
    EMPLOYEE = 5


def check_status(status_code):
    match status_code:
        case StatusCode.SUCCESS:
            return "Request was successful."
        case StatusCode.NOT_FOUND:
            return "Resource not found."
        case StatusCode.SERVER_ERROR:
            return "Server encountered an error."
        case _:
            return "Unknown status code."


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


class Direction_Enum(Enum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


class Direction_StrEnum(StrEnum):
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"


if __name__ == "__main__":

    print("Enum:")
    for color in Color:
        print(f"{color.name} = {color.value}")

    print("\nIntEnum:")
    for status in StatusCode:
        print(f"{status.name} = {status.value}")

    print("\nFlag:")
    permissions = list(Permission)
    user_permission = random.choice(permissions)
    for _ in range(random.randint(1, len(permissions) - 1)):
        user_permission |= random.choice(permissions)
    print(f"User Permission: {user_permission}")

    print("\nUnique Enum:")
    for entity in BusinessEntity:
        print(f"{entity.name} = {entity.value}")

    print(f"\n{check_status(StatusCode.SUCCESS)=}")
    print(f"{check_status(StatusCode.NOT_FOUND)=}")
    print(f"{check_status(StatusCode.SERVER_ERROR)=}")

    print("\nSales Categorization:")
    sales_data = [random.randint(1, 20) * 500 for _ in range(5)]
    for sales in sales_data:
        category = categorize_sales(sales)
        print(f"Sales Amount: {sales}, Category: {category.name}")

    try:
        print("\nStrEnum:")
        for direction in Direction_StrEnum:
            print(f"{direction.name} = {direction.value}")
    except TypeError:
        # Fallback for Python < 3.11 where StrEnum may not be available
        class StrEnum(str, Enum):
            pass

        print("\nStrEnum (fallback):")
        for direction in Direction_StrEnum:
            print(f"{direction.name} = {direction.value}")

    assert Direction_Enum.NORTH != "north", "Enum should not behave like a string"
    print("\nEnum Assertion passed: Direction.NORTH is not equal to 'north'")

    assert Direction_StrEnum.NORTH == "north", "StrEnum should behave like a string"
    print("StrEnum Assertion passed: Direction.NORTH is equal to 'north'")
