def value_error():
    """ValueError is raised when function receives correct argument but inappropriate value."""
    try:
        int("abc")
    except ValueError as e:
        print(f"\nValueError caught: {e}")

    try:
        int("123")
        print("No ValueError raised")
    except ValueError as e:
        print(f"ValueError caught: {e}")


def attribute_error():
    """AttributeError is raised when an invalid attribute reference is made."""

    class MyClass:
        pass

    obj = MyClass()
    try:
        obj.some_attribute
    except AttributeError as e:
        print(f"\nAttributeError caught: {e}")

    obj.some_attribute = "value"
    print("No AttributeError raised")


def type_error():
    """TypeError is raised when an operation or function is applied to an object of inappropriate type."""
    try:
        "abc" + 123
    except TypeError as e:
        print(f"\nTypeError caught: {e}")

    try:
        "abc" + "123"
        print("No TypeError raised")
    except TypeError as e:
        print(f"TypeError caught: {e}")


def index_error():
    """IndexError is raised when a sequence subscript is out of range."""
    my_list = [1, 2, 3]
    try:
        my_list[5]
    except IndexError as e:
        print(f"\nIndexError caught: {e}")

    try:
        my_list[2]
        print("No IndexError raised")
    except IndexError as e:
        print(f"IndexError caught: {e}")


def key_error():
    """KeyError is raised when a dictionary key is not found."""
    my_dict = {"a": 1, "b": 2}
    try:
        my_dict["c"]
    except KeyError as e:
        print(f"\nKeyError caught: {e}")

    try:
        my_dict["a"]
        print("No KeyError raised")
    except KeyError as e:
        print(f"KeyError caught: {e}")


def zero_division_error():
    """ZeroDivisionError is raised when the second argument of a division or modulo
    operation is zero.
    """
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"\nZeroDivisionError caught: {e}")

    try:
        1 / 1
        print("No ZeroDivisionError raised")
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught: {e}")


class OutOfRangeError(Exception):
    """Custom exception for out of range errors."""

    def __init__(self, value, min_value, max_value):
        self.value = value
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(f"Value {value} is out of range ({min_value}, {max_value})")


def out_of_range_error(value, min_value, max_value):
    """Raise OutOfRangeError if value is out of the specified range."""
    if not (min_value <= value <= max_value):
        raise OutOfRangeError(value, min_value, max_value)
    else:
        print(f"Value {value} is within the range ({min_value}, {max_value})")


if __name__ == "__main__":
    value_error()
    attribute_error()
    type_error()
    index_error()
    key_error()
    zero_division_error()

    try:
        out_of_range_error(10, 1, 5)
    except OutOfRangeError as e:
        print(f"OutOfRangeError caught: {e}")

    try:
        out_of_range_error(3, 1, 5)
    except OutOfRangeError as e:
        print(f"OutOfRangeError caught: {e}")
