import warnings
import random


def deprecated_function():
    """Using the warn function to issue a DeprecationWarning."""
    warnings.warn("This function is deprecated", DeprecationWarning, stacklevel=2)


def custom_warning():
    """Using the warn function to issue a custom warning."""

    class CustomWarning(UserWarning):
        pass

    warnings.warn("This is a custom warning", CustomWarning, stacklevel=2)


def filter_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    deprecated_function()

    warnings.filterwarnings("always", category=DeprecationWarning)
    deprecated_function()


def catch_warnings():
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        deprecated_function()
        assert len(w) == 1
        assert issubclass(w[-1].category, DeprecationWarning)
        print(f"Caught warning: {w[-1].message}")


def main():
    print(f"\n{deprecated_function()=}")

    print(f"\n{custom_warning()=}")

    print(f"\n{filter_warnings()=}")

    print(f"\n{catch_warnings()=}")


if __name__ == "__main__":
    main()
