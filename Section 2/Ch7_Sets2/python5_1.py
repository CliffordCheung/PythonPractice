def filter_and_square_set(input_set):
    # Write code here
    list1 = []
    for element in input_set:
        if element%2 == 1:
            num = element * element
            list1.append(num)
    new_set = set(list1)
    return(new_set)