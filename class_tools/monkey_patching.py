from typing import Callable
import random


class WeatherService:
    def get_temperature(self, city: str) -> float:
        return round(random.uniform(15.0, 25.0), 1)

    def get_humidity(self, city: str) -> float:
        return round(random.uniform(40.0, 60.0), 1)


def get_temperature_from_backup(self, city: str) -> float:
    return round(random.uniform(10.0, 20.0), 1)


def monkey_patch_method(cls: type, method_name: str, method: Callable) -> None:
    """
    Monkey patch a method into a class.

    Args:
        cls (type): The class to patch.
        method_name (str): The name of the method to patch.
        method (Callable): The method to patch into the class.
    """
    setattr(cls, method_name, method)


if __name__ == "__main__":
    weather_service = WeatherService()

    city = ["New York", "London", "Tokyo", "Sydney", "Paris", "Nashville", "Los Angeles"]
    city = random.choice(city)

    print(f"Temp: {weather_service.get_temperature(city)}\N{DEGREE SIGN}")
    print(f"Humidity: {weather_service.get_humidity(city)}\N{DEGREE SIGN}")

    monkey_patch_method(WeatherService, "get_temperature", get_temperature_from_backup)

    print(f"Temp (Backup): {weather_service.get_temperature(city)}\N{DEGREE SIGN}")
