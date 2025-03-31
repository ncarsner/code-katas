class Clothing:
    """
    Base class for all types of clothing.
    Attributes:
        name (str): The name of the clothing item.
        size (str): The size of the clothing item.
        color (str): The color of the clothing item.
        price (float): The price of the clothing item.
    """

    def __init__(self, name, size, color, price):
        self.name = name
        self.size = size
        self.color = color
        self.price = price

    def display_info(self):
        """
        Returns a string representation of the clothing item's details.
        """
        return f"{self.name} - Size: {self.size}, Color: {self.color}, Price: ${self.price:.2f}"


class MensWear(Clothing):
    """
    Represents men's clothing, inheriting from the Clothing base class.
    Attributes:
        type_of_clothing (str): The specific type of men's clothing (e.g., Jacket, Shirt).
    """

    def __init__(self, name, size, color, price, type_of_clothing):
        super().__init__(name, size, color, price)
        self.type_of_clothing = type_of_clothing

    def display_info(self):
        """
        Returns a string representation of the men's clothing item's details.
        """
        return f"Men's {self.type_of_clothing}: {super().display_info()}"


class WomensWear(Clothing):
    """
    Represents women's clothing, inheriting from the Clothing base class.
    Attributes:
        type_of_clothing (str): The specific type of women's clothing (e.g., Dress, Blouse).
    """

    def __init__(self, name, size, color, price, type_of_clothing):
        super().__init__(name, size, color, price)
        self.type_of_clothing = type_of_clothing

    def display_info(self):
        """
        Returns a string representation of the women's clothing item's details.
        """
        return f"Women's {self.type_of_clothing}: {super().display_info()}"


class ChildrensWear(Clothing):
    """
    Represents children's clothing, inheriting from the Clothing base class.
    Attributes:
        age_group (str): The age group the clothing is designed for (e.g., "3-5 years").
    """

    def __init__(self, name, size, color, price, age_group):
        super().__init__(name, size, color, price)
        self.age_group = age_group

    def display_info(self):
        """
        Returns a string representation of the children's clothing item's details.
        """
        return (
            f"Children's Wear (Age Group: {self.age_group}): {super().display_info()}"
        )


# Example of polymorphism: Using a list of Clothing objects
if __name__ == "__main__":
    # Creating instances of different clothing types
    mens_jacket = MensWear("Leather Jacket", "L", "Black", 120.00, "Jacket")
    womens_dress = WomensWear("Evening Gown", "M", "Red", 150.00, "Dress")
    kids_shirt = ChildrensWear("Cartoon T-Shirt", "S", "Blue", 20.00, "3-5 years")
    mens_shirt = MensWear("Formal Shirt", "M", "White", 45.00, "Shirt")
    womens_skirt = WomensWear("Pencil Skirt", "S", "Black", 60.00, "Skirt")
    kids_pants = ChildrensWear("Denim Pants", "XS", "Blue", 25.00, "6-8 years")

    # Polymorphic behavior: Storing all clothing items in a single list
    clothing_items = [
        mens_jacket,
        womens_dress,
        kids_shirt,
        mens_shirt,
        womens_skirt,
        kids_pants,
    ]

    # Displaying information for all clothing items
    print("Clothing Inventory:")
    for item in clothing_items:
        print(item.display_info())
