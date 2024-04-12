class Shop:
    def __init__(self):
        self.inventory = {}
        self.prices = {}
    
    def add_item(self,item_name,quantity,price):
        self.inventory[item_name]=quantity
        self.prices[item_name]=price

    def buy_item(self,item_name,quantity):
        if item_name in self.inventory and self.inventory[item_name]>=quantity:
            self.inventory[item_name] -= quantity
            total_cost=self.prices[item_name]*quantity
        else :
            print(f"item" + item_name + "is out of stock")    

    def display_inventory(self):
        print("Current Inventory:")
        for item_name, quantity in self.inventory.items():
            print(f"{item_name}: {quantity} in stock")  


    def calculate_revenue(self):
        total_revenue = 0
        for item_name, quantity_sold in self.inventory.items():
            total_revenue += self.prices.get(item_name, 0) * quantity_sold
        return total_revenue   
    def calculate_expenses(self):
        total_expenses = 0
        for item_name, quantity_purchased in self.inventory.items():
            total_expenses += self.prices.get(item_name, 0) * quantity_purchased
        return total_expenses
    

if __name__=="__main__":
        my_shop=Shop()
        my_shop.add_item("apple",10,12)
        my_shop.add_item("banana",20,15)

        my_shop.display_inventory()

        my_shop.buy_item("apple",5)
        my_shop.buy_item("banana",11)


        revenue = my_shop.calculate_revenue()
        expenses = my_shop.calculate_expenses()

        print(f"Total revenue: ${revenue:.2f}")
        print(f"Total expenses: ${expenses:.2f}")
        print(f"Profit (Revenue - Expenses): ${revenue - expenses:.2f}")


# Taking input as an integer
user_input = int(input("Enter an integer: "))

# Displaying the integer provided by the user
print("You entered:", user_input)





    


