def calculate_discount(price, discount_percentage):
    # Write code here
    discount_amount = price * float((discount_percentage/100.0))
    new_price = price - discount_amount
    new_price = round(new_price, 2)
    return (new_price)