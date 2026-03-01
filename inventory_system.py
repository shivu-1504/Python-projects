"""
How can we design an Inventory Management System in Python using multiple classes and polymorphism?

The system should include a base Product class and specialized subclasses like Electronics and Grocery that override tax calculation methods, store products in a list, and compute the total inventory value dynamically.
"""

print("====== Inventory Management System ======")

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_tax(self):
        return 0

    def total_price(self):
        tax = self.calculate_tax()
        return (self.price + tax) * self.quantity


class Electronics(Product):
    def calculate_tax(self):
        return self.price * 0.18

class Grocery(Product):
    def calculate_tax(self):
        return self.price * 0.05


if __name__ == "__main__":

    inventory = [
        Electronics("Laptop", 50000, 2),
        Electronics("Mobile", 20000, 3),
        Grocery("Rice Bag", 1200, 5),
        Grocery("Milk", 50, 20)
    ]

    total_inventory_value = 0

    print("\nProduct Details:\n")

    for product in inventory:
        product_total = product.total_price()
        total_inventory_value += product_total

        print(f"Name: {product.name}")
        print(f"Price: ₹{product.price}")
        print(f"Quantity: {product.quantity}")
        print(f"Tax per unit: ₹{product.calculate_tax():.2f}")
        print(f"Total Value: ₹{product_total:.2f}")
        print("-" * 40)

    print(f"\nTotal Inventory Value: ₹{total_inventory_value:.2f}")