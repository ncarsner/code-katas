from typing import Any, Type

class SingletonMeta(type):
    """
    A metaclass for creating Singleton classes.
    Ensures that only one instance of the class exists.
    Useful for scenarios like database connections or configuration managers.
    """
    _instances: dict[Type, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # If no instance exists, create one and store it
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BusinessConfig(metaclass=SingletonMeta):
    """
    A configuration manager class for business intelligence applications.
    Ensures that only one configuration manager exists throughout the application.
    """
    def __init__(self, database_url: str, api_key: str):
        self.database_url = database_url
        self.api_key = api_key

    def display_config(self) -> None:
        """Print the current configuration."""
        print(f"Database URL: {self.database_url}")
        print(f"API Key: {self.api_key}")


# Example usage of SingletonMeta
config1 = BusinessConfig(database_url="https://db.example.com", api_key="12345")
config2 = BusinessConfig(database_url="https://other-db.example.com", api_key="67890")

# Both config1 and config2 point to the same instance
assert config1 is config2

config1.display_config()
# Output:
# Database URL: https://db.example.com
# API Key: 12345


class FieldValidationMeta(type):
    """
    A metaclass for adding field validation to classes.
    Useful for ensuring data integrity in business intelligence models.
    """
    def __new__(cls, name, bases, dct):
        # Automatically add a validate_fields method to the class
        def validate_fields(self) -> None:
            for field, value in self.__dict__.items():
                if value is None:
                    raise ValueError(f"Field '{field}' cannot be None.")
        dct['validate_fields'] = validate_fields
        return super().__new__(cls, name, bases, dct)


class BIModel(metaclass=FieldValidationMeta):
    """
    A base class for business intelligence models with field validation.
    """
    def __init__(self, name: str, value: float):
        self.name = name
        self.value = value


# Example usage of FieldValidationMeta
try:
    model = BIModel(name="Revenue", value=None)
    model.validate_fields()  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: Field 'value' cannot be None.

# Correct usage
model = BIModel(name="Revenue", value=1000.0)
model.validate_fields()  # No error
print(f"Model: {model.name}, Value: {model.value}")
# Output: Model: Revenue, Value: 1000.0