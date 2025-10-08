inventory = {}
def add_item(name, price, stock):
    if name not in inventory:
        inventory[name] = {"price" : price, "stock": stock}
        print(f"Item '{name}' added successfully.")
    else:
        print(f"Error: Item '{name}' already exists.")

def update_stock(name, stock):
    if name not in inventory:
        print(f"Error: Item '{name}' not found.")
    else:
        existing_stock = inventory[name]["stock"]
        #print(existing_stock, stock)
        new_stock = existing_stock + stock
        if(new_stock < 0):
            print(f"Error: Insufficient stock for '{name}'.")
        else:
            inventory[name]["stock"] = new_stock
            print(f"Stock for '{name}' updated successfully.")
            
def check_availability(name):
    if name not in inventory:
        return("Item not found")
    else:
        return(inventory[name]["stock"])
        

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
update_stock("Apple", -20)
update_stock("Banana", 30)
print(check_availability("Apple"))  # Should return 80
print(check_availability("Banana"))  # Should return 80
print(check_availability("Orange"))  # Should return "Item not found"