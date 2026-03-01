"""
How can we design a secure and structured Bank Account Management System using
Object-Oriented Programming in Python?

The system should implement encapsulation by keeping the balance private, use
@property for controlled access, and provide features like deposit, withdrawal,
and interest calculation using a @staticmethod.
"""

print("====== Bank Account System ======")

class BankAccount:
    bank_name = "Global Bank" 

    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.__balance = balance   # Private

    @property
    def balance(self):
        return self.__balance

    @staticmethod
    def calculate_interest(principal: float, rate: float, time: float):
        return (principal * rate * time) / 100

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient funds. Withdrawal denied.")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.__balance}")

    def check_balance(self):
        """Returns formatted balance string."""
        return f"Current balance: ₹{self.__balance}"


# Creating Objects 
if __name__ == "__main__":

    account1 = BankAccount("Shiv", 10000)
    account2 = BankAccount("Rahul", 5000)

    print("\n--- Account 1 Details ---")
    print("Account Holder:", account1.account_holder)
    print(account1.check_balance())

    account1.deposit(2000)
    account1.withdraw(1500)

    print("\n--- Account 2 Details ---")
    print("Account Holder:", account2.account_holder)
    print(account2.check_balance())

    account2.withdraw(6000)

    interest = BankAccount.calculate_interest(10000, 5, 2)
    print(f"\nCalculated Interest on ₹10000 for 2 years at 5%: ₹{interest}")