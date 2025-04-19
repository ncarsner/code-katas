class DatabaseConnection:
    """
    A class to encapsulate database connection details and operations.
    This ensures sensitive information is hidden and access is controlled.
    """

    def __init__(self, host: str, user: str, password: str, database: str):
        # Private attributes to store sensitive connection details
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def connect(self) -> str:
        """
        Simulates connecting to a database.
        Returns a success message if connection details are valid.
        """
        # In a real-world scenario, this would establish a connection to the database
        if self.__host and self.__user and self.__password and self.__database:
            return f"Connected to {self.__database} at {self.__host} as {self.__user}"
        else:
            raise ValueError("Invalid connection details")

    def update_credentials(self, user: str, password: str) -> None:
        """
        Updates the user and password for the database connection.
        """
        self.__user = user
        self.__password = password

    def get_connection_info(self) -> str:
        """
        Provides limited connection information for debugging purposes.
        Does not expose sensitive details like the password.
        """
        return f"Host: {self.__host}, Database: {self.__database}, User: {self.__user}"


class ReportGenerator:
    """
    A class to encapsulate the logic for generating business intelligence reports.
    """

    def __init__(self, db_connection: DatabaseConnection):
        # Private attribute to store the database connection
        self.__db_connection = db_connection

    def generate_sales_report(self) -> str:
        """
        Simulates generating a sales report by querying the database.
        """
        # Simulate using the database connection
        connection_status = self.__db_connection.connect()
        # In a real-world scenario, this would involve executing SQL queries
        return f"{connection_status}\nSales report generated successfully."

    def generate_inventory_report(self) -> str:
        """
        Simulates generating an inventory report by querying the database.
        """
        connection_status = self.__db_connection.connect()
        return f"{connection_status}\nInventory report generated successfully."


if __name__ == "__main__":
    # Encapsulation ensures sensitive details are hidden
    db_conn = DatabaseConnection(
        host="localhost",
        user="admin",
        password="securepassword123",
        database="business_db",
    )

    # Limited access to sensitive information
    print(db_conn.get_connection_info())

    # Business intelligence developer uses the ReportGenerator class
    report_gen = ReportGenerator(db_conn)
    print(report_gen.generate_sales_report())
    print(report_gen.generate_inventory_report())

    # Updating credentials securely
    db_conn.update_credentials(user="new_admin", password="new_secure_password")
    print(report_gen.generate_sales_report())
