# INVENTORY FUNCTIONS

# ✅ Add product function
def add_product(file_name, name, price, quantity, pro_desc):
    name = name.lower()
    with open(file_name, "a") as file:
        file.write(f"{name},{price},{quantity},{pro_desc}\n")
    return f"{name.capitalize()} added to {file_name} successfully!"

# ✅ Update quantity function
def update_product(file_name, target_name, new_quantity):
    target_name = target_name.lower()
    updated_lines = []
    
    file = open(file_name, "r")
    for line in file:
        parts = line.strip().split(",")
        if parts[0] == target_name:
           
            line = f"{parts[0]},{parts[1]},{new_quantity},{parts[3]}\n"
        updated_lines.append(line)
    file.close()
    
    file = open(file_name, "w")
    file.writelines(updated_lines)
    file.close()

# ✅ Remove product function
def remove_product(file_name, name):
    name = name.lower()
    updated_lines = []
    
    file = open(file_name, "r")
    for line in file:
        parts = line.strip().split(",")
        if parts[0] != name:
            updated_lines.append(line)
    file.close()
    
    file = open(file_name, "w")
    file.writelines(updated_lines)
    file.close()

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
        
        if quantity <= threshold:
            print(f"WARNING: {product_name.capitalize()} is low on stock! Only {quantity} left.")
    file.close()

# ✅ File handling (save/read inventory)
def load_inventory(file_name):
    file = open(file_name, "r")
    content = file.read()
    return content
    file.close()
	
def save_inventory(file_name, name, price, quantity, pro_desc):
    name = name.lower()
    file = open(file_name, "a")
    file.write(f"{name},{price},{quantity},{pro_desc}\n")
    file.close()

