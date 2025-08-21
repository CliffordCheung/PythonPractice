def check_inventory(products, quantities):
    # Write code here
    if "Apples" in products:
        print("Apples are in stock.")
    if "Oranges" not in products:
        print("Oranges are not in stock.")
    if "Bananas" in quantities:
        print("Bananas quantity is tracked.")
    if "Grapes" not in quantities:
        print("Grapes quantity is not tracked.")