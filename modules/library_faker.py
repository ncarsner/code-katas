from typing import List, Dict, Any, Optional
from faker import Faker
import random
import json


# Initialize a Faker generator (can set locale for region-specific data)
fake = Faker(locale="en_US")

# Set a seed for reproducibility (optional)
Faker.seed(42)


def generate_fake_customers(num_customers: int = 10, locale: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Generate a list of fake customer records.

    Args:
        num_customers (int): Number of customer records to generate.
        locale (Optional[str]): Locale for data (e.g., 'en_US', 'de_DE').
            If None, uses the default locale.

    Returns:
        List[Dict[str, Any]]: List of customer dictionaries.

    Example:
        customers = generate_fake_customers(5, locale='en_GB')
    """
    generator = Faker(locale) if locale else fake
    customers = []
    for _ in range(num_customers):
        customer = {
            "customer_id": generator.uuid4(),
            "name": generator.name(),
            "email": generator.email(),
            "address": generator.address().replace("\n", ", "),
            "phone": generator.phone_number(),
            "dob": generator.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
            "created_at": generator.date_time_this_decade().isoformat(),
        }
        customers.append(customer)
    return customers


def generate_fake_products(num_products: int = 10, categories: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """
    Generate a list of fake product records.

    Args:
        num_products (int): Number of products to generate.
        categories (Optional[List[str]]): List of product categories.
            If None, uses a default set.

    Returns:
        List[Dict[str, Any]]: List of product dictionaries.

    Example:
        products = generate_fake_products(3, categories=['Books', 'Electronics'])
    """
    default_categories = ["Electronics", "Books", "Clothing", "Home", "Toys"]
    categories = categories or default_categories
    products = []
    for _ in range(num_products):
        product = {
            "product_id": fake.unique.ean(length=13),
            "name": fake.catch_phrase(),
            "category": random.choice(categories),
            "price": round(random.uniform(5.0, 500.0), 2),
            "in_stock": random.randint(0, 1000),
        }
        products.append(product)
    return products


def generate_fake_transactions(
    customers: List[Dict[str, Any]],
    products: List[Dict[str, Any]],
    num_transactions: int = 20,
) -> List[Dict[str, Any]]:
    """
    Generate a list of fake transaction records.

    Args:
        customers (List[Dict[str, Any]]): List of customer records.
        products (List[Dict[str, Any]]): List of product records.
        num_transactions (int): Number of transactions to generate.

    Returns:
        List[Dict[str, Any]]: List of transaction dictionaries.

    Example:
        transactions = generate_fake_transactions(customers, products, 50)
    """
    transactions = []
    for _ in range(num_transactions):
        customer = random.choice(customers)
        product = random.choice(products)
        quantity = random.randint(1, 5)
        transaction = {
            "transaction_id": fake.uuid4(),
            "customer_id": customer["customer_id"],
            "product_id": product["product_id"],
            "quantity": quantity,
            "total_price": round(product["price"] * quantity, 2),
            "transaction_date": fake.date_time_this_year().isoformat(),
        }
        transactions.append(transaction)
    return transactions

def generate_fake_employees(
    num_employees: int = 10,
    departments: Optional[List[str]] = None,
    titles: Optional[List[str]] = None,
    locale: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    Generate a list of fake employee records.

    Args:
        num_employees (int): Number of employee records to generate.
        departments (Optional[List[str]]): List of department names.
        titles (Optional[List[str]]): List of job titles.
        locale (Optional[str]): Locale for data.

    Returns:
        List[Dict[str, Any]]: List of employee dictionaries.

    Example:
        employees = generate_fake_employees(5, departments=['HR', 'IT'])
    """
    generator = Faker(locale) if locale else fake
    default_departments = ["HR", "IT", "Sales", "Marketing", "Finance", "Operations"]
    default_titles = ["Manager", "Engineer", "Analyst", "Specialist", "Director", "Coordinator"]
    departments = departments or default_departments
    titles = titles or default_titles
    employees = []
    for _ in range(num_employees):
        department = random.choice(departments)
        title = random.choice(titles)
        salary = random.randrange(50000, 350001, 150)
        employee = {
            "employee_id": generator.uuid4(),
            "name": generator.name(),
            "dob": generator.date_of_birth(minimum_age=21, maximum_age=65).isoformat(),
            "title": title,
            "department": department,
            "salary": salary,
            "email": generator.email(),
            "phone": generator.phone_number(),
            "hire_date": generator.date_between(start_date='-15y', end_date='today').isoformat(),
            "address": generator.address().replace("\n", ", "),
        }
        employees.append(employee)
    return employees


if __name__ == "__main__":
    # Generate 5 customers with German locale
    customers = generate_fake_customers(5, locale="de_DE")
    print("Sample Customers:", json.dumps(customers[:2], indent=2))

    # Generate 3 products in custom categories
    products = generate_fake_products(3, categories=["Software", "Hardware"])
    print("Sample Products:", json.dumps(products[:2], indent=4))

    # Generate 5 transactions
    transactions = generate_fake_transactions(customers, products, 5)
    print("Sample Transactions:", json.dumps(transactions[:2], indent=2))

    # Generate 5 employees with US locale
    employees = generate_fake_employees(5, locale="en_US")
    print("Sample Employees:", json.dumps(employees[:2], indent=4))

"""
TROUBLESHOOTING TIPS:
- If you see repeated data, use `fake.unique` for unique values.
- For locale errors, ensure the locale string is valid (see Faker docs).
- For reproducible results, set a seed: `Faker.seed(1234)`
- For large datasets, consider writing to CSV or database for BI workflows.
"""
