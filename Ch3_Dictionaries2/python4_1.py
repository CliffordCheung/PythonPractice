def print_product_details(product_data):
    # Write code here
    if len(product_data) == 0:
        print("No product information available")
    else:
        for key, value in product_data.items():
            name1 = key.capitalize()
            print(f'{name1}: {value}')