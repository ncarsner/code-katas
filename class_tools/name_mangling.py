import random
import string


class BankAccount:
    """
    A class to represent a bank account with name mangling demonstration.

    Attributes:
        account_holder (str): The name of the account holder.
        _balance (float): The protected balance of the account.
        __pin (str): The private PIN code that will be name-mangled.
    """

    def __init__(self, account_holder: str, balance: float, pin: str) -> None:
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = pin

    def get_pin(self) -> str:
        """
        Access the private PIN using name mangling.

        Returns:
            str: The value of the private PIN.
        """
        return self.__pin

    def set_pin(self, value: str) -> None:
        """
        Set the private PIN using name mangling.

        Args:
            value (str): The new value for the private PIN.
        """
        self.__pin = value

    def __private_method(self) -> str:
        """
        A private method that will be name-mangled.

        Returns:
            str: A message indicating the private method was called.
        """
        return "Private method called"

    def call_private_method(self) -> str:
        """
        Call the private method using name mangling.

        Returns:
            str: The result of the private method.
        """
        return self.__private_method()


if __name__ == "__main__":
    first_name = ["Alex", "Blake", "Chris", "Dylan", "Elliott"]
    last_name = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Martinez", "Young"]
    account_holder = f"{random.choice(first_name)} {random.choice(last_name)}"
    pin = "".join(random.choices(string.digits, k=4))

    account = BankAccount(account_holder, round(random.uniform(20, 1000), 2), pin)

    # Accessing public and protected variables directly
    print(f"{account.account_holder=}")
    print(f"{account._balance=}")

    # Accessing private variable using getter method
    print(f"{account.get_pin()=}")

    # Setting private variable using setter method
    account.set_pin("".join(random.choices(string.digits, k=4)))
    print(f"After setting private variable: {account.get_pin()=}")

    # Calling private method using public method
    print(f"{account.call_private_method()=}")

    # Directly accessing the name-mangled private variable (not recommended)
    print(f"{account._BankAccount__pin=}")

    # Directly accessing the name-mangled private method (not recommended)
    print(f"{account._BankAccount__private_method()=}")

new_account = BankAccount("Alex", 1000, "1234")
new_account.account_holder = "Blake"
new_account.set_pin("5678")
print(f"{new_account.account_holder=}")
print(f"{new_account.get_pin()=}")
