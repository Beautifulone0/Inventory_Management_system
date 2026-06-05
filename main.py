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
    if choice.lower() == "yes" or "y":
        print("Thank you for using IMS(Inventory Management System)")
        return True
    else:
        return False

# def load_inventory(file_name):
#     inventory = {}

#     file = open(file_name, "r")
#     for line in file:
#         lines = line.strip().split(",")

#         name = lines[0]
#         price = lines[1]
#         quantity = lines[2]
#         description = lines[3]

#         inventory[name] = (price, quantity, description)

#     file.close()
#     return inventory

inventory = {}

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Price")
    print("3. Update Quantity")
    print("4. Update Description")
    print("5. Remove Product")
    print("6. Search Product")
    print("7. Stock Alert")
    print("8. Load Inventory")
    print("9. Exit")
    # print("Select from above options 1-9 to * add,\n * update price,\n * update quantity,\n * update description,\n * remove,\n * search products,\n * check stock alerts,\n * or load inventory.")

    try:
        option = int(input("Enter option 1-9: "))

        if option < 1 or option > 9:
            print("Please input numbers from 1-9")
            continue
    except ValueError:
        print("Please input numbers from 1-9")

    print("\n")

    if option == 1:
        file_name = "inventory.txt"
        name = input("Enter product name: ")
        price = input("Enter product price: ")
        quantity = input("Enter product quantity: ")
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
        new_price = input("Enter the new price: ")

        update = update_price(
            file_name, 
            target_name, 
            new_price
        )
        print(update)

    elif option == 3:
        file_name = "inventory.txt"
        target_name = input("Enter the name of the product to update: ")
        new_quantity = input("Enter the new quantity: ")

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
            print(
                f"Product Found:\n"
                f"Product Name: {search[0].capitalize()}\n" 
                f"Price: ₦{int(float(search[1])):,}\n" 
                f"Quantity: {search[2]}, units of {search[3]}\n" 
                f"Description: {search[3]}\n")
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
        if load :
            print("\nLoaded Inventory: ")
            for name, details in load.items():
                price = details[0]
                quantity = details[1]
                description =details[2]

                print(
                    f"Product Name: {name.capitalize()}\n" 
                    f"Price: ₦{int(float(price)):,}\n" 
                    f"Quantity: {quantity}pcs\n" 
                    f"Description: {description}\n"
                )
        else:
            print("Inventory is empty")
        
    elif option == 9:
        print("Are you sure you want to exit this inventory management system?")
        if exit_inventory():
            break
    else:
        print("Invalid option selected. Please choose 1, 2, 3, 4, 5, 6, 7, 8, or 9.")
