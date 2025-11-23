inventory = {"pens": 10,"pencils": 10,"erasers": 10}
#function to display the inventory
def display():
    print("\nProducts and their quantity available in the Inventory - ")
    for product, quantity in inventory.items():
        print(f"{product.title()} - {quantity}")
    print()
#function to add products to the inventory
def adding():
    product = input("Enter product to add - ").lower()
    quantity = int(input("Enter quantity to add -  "))
    if product in inventory:
        inventory[product] += quantity
    else:
        inventory[product] = quantity
    print(f"{quantity} units of {product.title()} have been added in the inventory\n")
#function to sell products from the inventory 
def selling():
    product = input("Enter product to sell - ").lower()
    if product in inventory:
        quantity = int(input("Enter quantity to sell - "))
        if quantity <= inventory[product]:
            inventory[product] -= quantity
            print(f"{quantity} units of {product.title()} have been sold.\n")
            if inventory[product] <= 5:
                print(f"{product.title()} quantity is low, only {inventory[product]} units are left\n")
        else:
            print("Insufficient quantity\n")
    else:
        print("Product not found in inventory\n")
#function for the inventory management system
def main():
    while True:
        print("Inventory Management Menu")
        print("1. Display Inventory")
        print("2. Add Product")
        print("3. Sell Product")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            display()
        elif choice == '2':
            adding()
        elif choice == '3':
            selling()
        elif choice == '4':
            print("Exiting Inventory Management Menu")
            break
        else:
            print("Choose a valid option\n")
main()
