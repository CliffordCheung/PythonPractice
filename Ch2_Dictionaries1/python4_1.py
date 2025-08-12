def update_inventory(inventory_dict, item, quantity):
    # Write code here
    if item in inventory_dict:
        inventory_dict[item] += quantity
    else:
        inventory_dict[item] = quantity
    print(inventory_dict)