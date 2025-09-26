def iterate_and_filter_set(input_set):
    # Write code here
    list1 = []
    for element in input_set:
        if element <= 10:
            list1.append(element)
    new_set = set(list1)
    return(new_set)