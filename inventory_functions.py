# INVENTORY FUNCTIONS

# ✅ Add product function
def add_product(file_name, name, price, quantity, pro_desc):
    if search_product(file_name, name) is not None:
        return f"Error: {name.capitalize()} already exists! Use the update function instead."
        
    name = name.lower()
    with open(file_name, "a") as file:
        file.write(f"{name},{price},{quantity},{pro_desc}\n")
    return f"{name.capitalize()} added to {file_name} successfully!"

#product update functions.
# ✅ Update price function
def update_price(file_name, target_name, new_price):
    try:
        new_price = float(new_price)
    except ValueError:
        return f"Error: '{new_price}' is not valid. Please use a number."
        
    target_name = target_name.lower()
    updated_lines = []
    product_found = False
    
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if not parts or parts[0] == "": 
                continue
                
            if parts[0] == target_name:
                line = f"{parts[0]},{new_price},{parts[2]},{parts[3]}\n"
                product_found = True  
            updated_lines.append(line)
            
    with open(file_name, "w") as file:
        file.writelines(updated_lines)
       
    if product_found:
        return f"Oh yeah we have updated the price of {target_name.capitalize()} to {new_price}"
    else:
        return f"The Product '{target_name.capitalize()}' was not found in inventory."
  

# ✅ Update quantity function 
def update_quantity(file_name, target_name, new_quantity):
    try:
        new_quantity = int(new_quantity)
    except ValueError:
        return f"Error: '{new_quantity}' is not a valid quantity. Please use a number."
        
    target_name = target_name.lower()
    updated_lines = []
    product_found = False 
    
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if not parts or parts[0] == "":
                continue
                
            if parts[0] == target_name:
                line = f"{parts[0]},{parts[1]},{new_quantity},{parts[3]}\n"
                product_found = True  
            updated_lines.append(line)
            
    with open(file_name, "w") as file:
        file.writelines(updated_lines)
        
    if product_found:
        return f"Oh yeah we have updated the quantity of {target_name.capitalize()} to {new_quantity}."
    else:
        return f"The Product '{target_name.capitalize()}' was not found in inventory."



# ✅ Update product description function
def update_desc(file_name, target_name, new_desc):
    target_name = target_name.lower()
    updated_lines = []
    product_found = False
    
    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if not parts or parts[0] == "":  
                continue
                
            if parts[0] == target_name:
                line = f"{parts[0]},{parts[1]},{parts[2]},{new_desc}\n"
                product_found = True  
            updated_lines.append(line)
            
    with open(file_name, "w") as file:
        file.writelines(updated_lines)

    if product_found:
        return f"Oh yeah we have updated the description of {target_name.capitalize()} to {new_desc}"
    else:
        return f"The Product '{target_name.capitalize()}' was not found in inventory."


# ✅ Remove product function
def remove_product(file_name, name):
    name = name.lower()
    updated_lines = []
    if search_product(file_name, name) is not None:
        return f"Error: {name.capitalize()} doesn't' exist!"
    
    file = open(file_name, "r")
    for line in file:
        parts = line.strip().split(",")
        if parts[0] != name:
            updated_lines.append(line)
    file.close()
    
    file = open(file_name, "w")
    file.writelines(updated_lines)
    file.close()
    
    return f"Oh yeah we have deleted the product {name.capitalize()}!"
    
# ✅ Search product function
def search_product(file_name, search_name):
    search_name = search_name.lower()
    file = open(file_name, "r")
    for line in file:
        parts = line.strip().split(",")
        if parts[0] == search_name:
            return parts
    file.close()

# ✅ Low stock warning
def low_stock(file_name, threshold=5):
    file = open(file_name, "r")
    for line in file:
        parts = line.strip().split(",")
        quantity = int(parts[2])
        product_name = parts[0]
        
        try:
           quantity = int(parts[2])
        except ValueError:
                print(f"Skipping corrupted line for '{parts[0]}': Quantity must be a number.")
                continue
        
        if quantity <= threshold:
            print(f"WARNING: {product_name.capitalize()} is low on stock! Only {quantity} left.")
                      
        else:
        	print(f"{product_name.capitalize()}'' is in stock with {quantity} units.")
    file.close()

# ✅ File handling (save/read inventory)
def load_inventory(file_name):
    file = open(file_name, "r")
    content = file.read()
    return content
    file.close()
    
    
