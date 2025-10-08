inventory = {}
def add_item(name, price, stock):
    if name not in inventory:
        inventory[name] = {"price" : price, "stock": stock}
        print(f"Item '{name}' added successfully.")
    else:
        print(f"Error: Item '{name}' already exists.")

add_item("Apple", 0.5, 100)
add_item("Banana", 0.2, 50)
add_item("Apple", 0.6, 30)  # Should print an error
print(inventory) 