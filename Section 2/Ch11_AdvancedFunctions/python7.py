def sum_nested(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a list
            total += sum_nested(element)  # Recursive call for sublist
        else:
            total += element  # Add the integer directly
    return total
    

nested_list = [1, [2, 3], [4, [5, 6]], 7]
total = sum_nested(nested_list)
print(total)