from inventory_functions import (
    add_product,
    update_product,
    remove_product,
    search_product,
    low_stock,
    save_inventory,
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
    print("2. Update Product")
    print("3. Remove Product")
    print("4. Search Product")
    print("5. Stock Alert")
    print("6. Save Inventory")
    print("7. Load Inventory")
    print("8. Exit")
    print("Select from above options 1-8 to add, update, remove, search products, check stock alerts, save or load inventory.")

    option = input("Enter option: ")

    if option == 1:
        add_product(inventory)
    elif option == 2:
        update_product(inventory)
    elif option == 3:
        remove_product(inventory)
    elif option == 4:
        search_product(inventory)
    elif option == 5:
        low_stock(inventory)
    elif option == 6:
        save_inventory(inventory)
    elif option == 7:
        load_inventory(inventory)
    elif option == 8:
        print("Are you sure you want to exit this inventory management system?")
        exit_inventory()
    else:
        print("Invalid option selected. Please choose 1, 2, 3, 4, 5, 6, 7, or 8.")
        if exit_inventory() == False:
            break

