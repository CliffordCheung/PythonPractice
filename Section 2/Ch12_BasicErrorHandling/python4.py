def handle_shopping_cart(orders):
    # Create an empty dictionary for the shopping cart
    cart = {}
    # Process each order in the list
    for order in orders:
        try:
            # Split the order and add to cart
            test = order.split(":")
            print(test[0])
            print(test[1])
            if int(test[1]) < 0:
                print(f'Negative quantity not allowed: {order}')
            else:
                if test[0] not in cart:
                    cart[test[0]] = int(test[1])
                else:
                    temp = cart[test[0]]
                    temp += int(test[1])
                    cart.update({test[0]: temp})
                    
            # Handle potential errors
            
        except ValueError:
            # Handle value errors
            
            print(f'Invalid quantity: {order}')
        except Exception as e:
            # Handle unexpected errors
            print(f'Invalid format: {order}')
            #print(f'Invalid quantity: {order}')
            
    # Return the completed cart
    return(cart)
    
order_list = ["broccoli:0","snacks:10","cheese:2","snacks:5"]
new_list = handle_shopping_cart(order_list)
print(new_list)