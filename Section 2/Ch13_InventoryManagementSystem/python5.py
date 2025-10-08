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
    
def reduce_stock(name, stock):
    existing_stock = inventory[name]["stock"]
    #print(existing_stock, stock)
    new_stock = existing_stock - stock
    inventory[name]["stock"] = new_stock
    
def sales_report(sales):
    total = 0.0
    for key,value in sales.items():
        #print(key, value)
        if key not in inventory:
            print(f"Error: Item '{key}' not found.")
        else:
            if value < inventory[key]["stock"]:
                item_cost = inventory[key]["price"]
                total += (float(item_cost * value))
                reduce_stock(key, value)
            else:
                print(f"Error: Insufficient stock for '{key}'.")
    return(f"Total revenue: ${total:.2f}")        
        

add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  # Orange should print an error
print(sales_report(sales))  # Should output: 19.0
print(inventory)