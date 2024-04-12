class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            print("Product already exists in inventory.")
        else:
            self.products[product.name] = product

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print("Product not found in inventory.")

    def update_quantity(self, product_name, quantity_change):
        if product_name in self.products:
            self.products[product_name].quantity += quantity_change
            if self.products[product_name].quantity < 0:
                self.products[product_name].quantity = 0
        else:
            print("Product not found in inventory.")

class Accounting:
    def __init__(self):
        self.revenue = 0
        self.expenses = 0

    def record_sale(self, product_price):
        self.revenue += product_price

    def update_expenses(self, expense):
        self.expenses += expense

if __name__ == "__main__":
    # Create instances of Inventory and Accounting classes
    inventory = Inventory()
    accounting = Accounting()

    # Create instances of Product representing different products
    product1 = Product("Apple", 1.50, 50)
    product2 = Product("Banana", 0.75, 100)

    # Add products to inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Update quantity of product
    inventory.update_quantity("Apple", -10)

    # Record sale and update revenue
    accounting.record_sale(product1.price * 10)

    # Display inventory and total revenue
    print("Inventory:")
    for product in inventory.products.values():
        print(f"{product.name}: ${product.price} | Quantity: {product.quantity}")

    print(f"Total Revenue: ${accounting.revenue}")
