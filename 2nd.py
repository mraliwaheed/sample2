class Shop:
    def __init__(self):
        self.inventory = {}  # Dictionary to store item inventory (item_name: quantity)
        self.prices = {}  # Dictionary to store item prices (item_name: price)

    def add_item(self, item_name, price, quantity):
        """
        Add an item to the shop's inventory.

        Args:
            item_name (str): Name of the item.
            price (float): Price of the item.
            quantity (int): Initial quantity of the item in stock.
        """
        self.inventory[item_name] = quantity
        self.prices[item_name] = price

    def purchase_item(self, item_name, quantity):
        """
        Purchase an item from the shop.

        Args:
            item_name (str): Name of the item.
            quantity (int): Quantity to purchase.
        """
        if item_name in self.inventory and self.inventory[item_name] >= quantity:
            self.inventory[item_name] -= quantity
            total_cost = self.prices[item_name] * quantity
            print(f"Purchased {quantity} {item_name}(s) for ${total_cost:.2f}")
        else:
            print(f"Item {item_name} is out of stock or insufficient quantity.")

    def display_inventory(self):
        """
        Display the current inventory of the shop.
        """
        print("Current Inventory:")
        for item_name, quantity in self.inventory.items():
            print(f"{item_name}: {quantity} in stock")

# Example usage
if __name__ == "__main__":
    my_shop = Shop()
    my_shop.add_item("Apple", price=1.0, quantity=10)
    my_shop.add_item("Banana", price=0.75, quantity=15)

    my_shop.display_inventory()

    my_shop.purchase_item("Apple", quantity=5)
    my_shop.purchase_item("Banana", quantity=20)
    my_shop.purchase_item("Cherry", quantity=3)  # Non-existent item
