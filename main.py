from inventory_functions import (
    add_product,
    update_price,
    update_quantity,
    update_desc,
    remove_product,
    search_product,
    low_stock,
    load_inventory,
)

def exit_inventory ():
    choice = input("Yes / No : ")
    if choice.lower() == "yes":
        print("Thank you for using IMS(Inventory Management System)")
        return True
    else:
        return False

inventory = {}

while True:
    print("\n Inventory Management System")
    print("1. Add Product")
    print("2. Update Price")
    print("3. Update Quantity")
    print("4. Update Description")
    print("5. Remove Product")
    print("6. Search Product")
    print("7. Stock Alert")
    print("8. Load Inventory")
    print("9. Exit")
    print("Select from above options 1-9 to add, update, remove, search products, check stock alerts, save or load inventory.")

    option = int(input("Enter option: "))

    if option == 1:
        file_name = "inventory.txt"
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        pro_desc = input("Enter Product description: ")

        result = add_product(
            file_name, 
            name, 
            price, 
            quantity, 
            pro_desc
        )
        print(result)
    
    elif option == 2:
        file_name = "inventory.txt"
        target_name = input("Enter the name of the product to update: ")
        new_price = float(input("Enter the new price: "))

        update = update_price(
            file_name, 
            target_name, 
            new_price
        )
        print(update)

    elif option == 3:
        file_name = "inventory.txt"
        target_name = input("Enter the name of the product to update: ")
        new_quantity = int(input("Enter the new quantity: "))

        update = update_quantity(
            file_name, 
            target_name, 
            new_quantity
        )
        print(update)

    elif option == 4:
        file_name = "inventory.txt"
        target_name = input("Enter the name of the product to update: ")
        new_desc = input("Enter the new description: ")

        update = update_desc(
            file_name, 
            target_name, 
            new_desc
        )
        print(update)
    
    elif option == 5:
        file_name = "inventory.txt"
        name = input("enter the name of product to remove/delete: ")

        remove = remove_product(
            file_name,
            name
        )
        print(remove)

    elif option == 6:
        file_name = "inventory.txt"
        search_name = input("Enter the name of the product to search: ")
        search = search_product(
            file_name,
            search_name
        )
        if search:
            print(f"Product found: {search[0].capitalize()}, Price: {search[1]}, Quantity: {search[2]}, Description: {search[3]}")
        else:
            print("Product not found")
                
    elif option == 7:
        file_name = "inventory.txt"
        
        low_stock(file_name)

    elif option == 8:
        file_name = "inventory.txt"
        load = load_inventory( 
            file_name
        )
        print(load)
        
    elif option == 9:
        print("Are you sure you want to exit this inventory management system?")
        if exit_inventory():
            break
    else:
        print("Invalid option selected. Please choose 1, 2, 3, 4, 5, 6, 7, 8, or 9.")