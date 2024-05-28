class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

def get_attribute_value(car_instance, attribute_name):
    """
    Get the value of a specified attribute of a Car instance using getattr.

    Parameters:
        car_instance (Car): An instance of the Car class.
        attribute_name (str): The name of the attribute to retrieve.

    Returns:
        The value of the specified attribute, or None if the attribute doesn't exist.
    """
    return getattr(car_instance, attribute_name, None)

# Example usage:
my_car = Car("Toyota", "Camry", 2020)
attribute_name = "make"

print(f"{attribute_name}: {get_attribute_value(my_car, attribute_name)}")

attribute_name = "model"
print(f"{attribute_name}: {get_attribute_value(my_car, attribute_name)}")

attribute_name = "year"
print(f"{attribute_name}: {get_attribute_value(my_car, attribute_name)}")

attribute_name = "color"  # Non-existent attribute
print(f"{attribute_name}: {get_attribute_value(my_car, attribute_name)}")
