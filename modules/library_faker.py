from typing import List, Dict, Any, Optional
from faker import Faker
from faker.providers import BaseProvider, DynamicProvider
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


# Custom provider using BaseProvider (see Faker docs)
class BusinessUnitProvider(BaseProvider):
    def business_unit(self):
        units = [
            "Sales", "Marketing", "Finance", "Operations", "IT", "DevOps",
            "Engineering", "Research", "Analytics", "Supply Chain", "Logistics",
            "Human Resources", "Customer Support", "Product", "Legal", "R&D"
        ]
        return self.random_element(units)

# Add the custom provider to the Faker instance
fake.add_provider(BusinessUnitProvider)

def generate_fake_business_data(num_records: int = 10, min_date='-2y', max_date='today') -> List[Dict[str, Any]]:
    """
    Generate a list of fake business records.

    Args:
        num_records (int): Number of business records to generate.

    Returns:
        List[Dict[str, Any]]: List of business data dictionaries.
    """
    records = []
    for _ in range(num_records):
        record = {
            "record_id": fake.uuid4(),
            "business_unit": fake.business_unit(),
            "region": fake.state(),
            "manager": fake.name(),
            "revenue": round(random.uniform(10000, 500000), 2),
            "expenses": round(random.uniform(5000, 300000), 2),
            "profit": 0,  # calculated below
            "report_date": fake.date_between(start_date=min_date, end_date=max_date).isoformat(),
        }
        record["profit"] = round(record["revenue"] - record["expenses"], 2)
        records.append(record)
    return records


# Custom Lorem Provider for BI/Analytics
class BILoremProvider(BaseProvider):
    # Custom BI/Analytics vocabulary
    bi_lorem_word_list = [
        "dashboard", "KPI", "pipeline", "ETL", "data lake", "warehouse", "insight",
        "metric", "visualization", "aggregation", "dimension", "drilldown", "forecast",
        "trend", "anomaly", "segmentation", "normalization", "schema", "query", "model",
        "predictive", "cluster", "regression", "outlier", "transformation", "integration",
        "snapshot", "cube", "fact", "measure", "report", "scorecard", "benchmark",
        "automation", "stream", "real-time", "batch", "API", "dataset", "mapping"
    ]

    def bi_lorem_words(self, nb=3, ext_word_list=None):
        word_list = ext_word_list or self.bi_lorem_word_list
        return [self.generator.random_element(word_list) for _ in range(nb)]

    def bi_lorem_sentence(self, nb_words=6, variable_nb_words=True, ext_word_list=None):
        word_list = ext_word_list or self.bi_lorem_word_list
        if variable_nb_words:
            nb_words = self.generator.random.randint(max(1, nb_words - 2), nb_words + 2)
        words = self.bi_lorem_words(nb=nb_words, ext_word_list=word_list)
        sentence = " ".join(words).capitalize() + "."
        return sentence
    
    def bi_lorem_paragraph(self, nb_sentences=3, variable_nb_sentences=True, ext_word_list=None):
        if variable_nb_sentences:
            nb_sentences = self.generator.random.randint(max(1, nb_sentences - 1), nb_sentences + 2)
        return " ".join(self.bi_lorem_sentence(ext_word_list=ext_word_list) for _ in range(nb_sentences))

# Add the custom BI Lorem provider to the Faker instance
fake.add_provider(BILoremProvider)

# Add the custom DynamicProvider for city names
city_provider = DynamicProvider(
    provider_name="city", # overrides the default city provider
    elements=[
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Nashville",
        "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
    ]
)
fake.add_provider(city_provider)


if __name__ == "__main__":
    print(fake.sentence())

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

    # Example: Generate 5 business data records
    business_data = generate_fake_business_data(5)
    print("Sample Business Data:", json.dumps(business_data[:2], indent=2))

    # Example: Use the custom BI Lorem provider
    print("\nSample Standard Lorem Sentence:", fake.sentence())
    print("Sample BI Lorem Sentence:", fake.bi_lorem_sentence())
    print("Sample BI Lorem Paragraph:", fake.bi_lorem_paragraph())

"""
TROUBLESHOOTING TIPS:
- If you see repeated data, use `fake.unique` for unique values.
- For locale errors, ensure the locale string is valid (see Faker docs).
- For reproducible results, set a seed: `Faker.seed(1234)`
- For large datasets, consider writing to CSV or database for BI workflows.
"""
