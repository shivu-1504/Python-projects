import csv

print("====== Expense Tracker ======")

FILE_NAME = "expenses.csv"

class ExpenseTracker:

    @staticmethod
    def add_expense(category, amount):
        try:
            with open(FILE_NAME, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([category, amount])
            print("Expense added successfully.")
        except Exception as e:
            print("Error adding expense:", e)

    @staticmethod
    def read_expenses():
        expenses = []

        try:
            with open(FILE_NAME, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    category, amount = row
                    expenses.append({"category": category, "amount": float(amount)})
        except FileNotFoundError:
            print("No expense file found.")
        except Exception as e:
            print("Error reading file:", e)

        return expenses

    @staticmethod
    def total_spending(expenses):
        return sum(expense["amount"] for expense in expenses)

    @staticmethod
    def category_wise_spending(expenses):
        category_totals = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        return category_totals

if __name__ == "__main__":

    ExpenseTracker.add_expense("Food", 250)
    ExpenseTracker.add_expense("Transport", 100)
    ExpenseTracker.add_expense("Food", 150)

    expenses = ExpenseTracker.read_expenses()

    total = ExpenseTracker.total_spending(expenses)
    print(f"\nTotal Spending: ₹{total:.2f}")

    print("\nCategory-wise Spending:")
    category_data = ExpenseTracker.category_wise_spending(expenses)

    for category, amount in category_data.items():
        print(f"{category}: ₹{amount:.2f}")
