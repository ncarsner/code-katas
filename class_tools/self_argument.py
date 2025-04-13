import random

RAND_INTS = [random.randint(10, 100) for _ in range(5)]
print(f"{RAND_INTS=}")


class SalesReport:
    """
    A class to represent and manage sales data for a business.

    The `self` keyword in Python is used to represent the instance of the class.
    It allows access to the attributes and methods of the class within its scope.
    """

    def __init__(self, sales_data):
        """
        Initialize the SalesReport object with sales data.

        :param sales_data: A dictionary where keys are product names
                           and values are sales figures (e.g., {'Product A': 100, 'Product B': 150}).
        """
        # Use `self` to assign instance attributes
        self.sales_data = sales_data

    def add_sales(self, product, amount):
        """
        Add sales data for a product.

        :param product: The name of the product to add sales for.
        :param amount: The amount of sales to add.
        """
        # Use `self` to access and modify instance attributes
        if product in self.sales_data:
            self.sales_data[product] += amount
        else:
            self.sales_data[product] = amount
        print(f"Sales for {product} updated to {self.sales_data[product]}.")

    def total_sales(self):
        """
        Calculate and return the total sales across all products.

        :return: The total sales as an integer.
        """
        # Use `self` to access instance attributes
        return sum(self.sales_data.values())

    def display_sales(self):
        """
        Display the sales data for all products in a readable format.
        """
        # Use `self` to access instance attributes
        print("Sales Report:")
        for product, sales in self.sales_data.items():
            print(f"  {product}: {sales} units")


# How the `self` keyword works

# Create an instance of the SalesReport class
sales_data = {"Product A": RAND_INTS[0], "Product B": RAND_INTS[1]}
report = SalesReport(sales_data)  # `self` in __init__ refers to this instance

# Add sales for an existing product
report.add_sales("Product A", RAND_INTS[0])  # `self` in add_sales refers to the same instance

# Add sales for a new product
report.add_sales("Product C", RAND_INTS[2])

# Calculate the total sales
total = report.total_sales()  # `self` in total_sales refers to the instance
print(f"Total Sales: {total} units")

# Display the sales data
report.display_sales()  # `self` in display_sales refers to the instance

# `self` is automatically passed as the first argument to instance methods.
# It allows each method to access and modify the instance's attributes and call other methods.
# Without `self`, methods would not know which instance's data to operate on.
