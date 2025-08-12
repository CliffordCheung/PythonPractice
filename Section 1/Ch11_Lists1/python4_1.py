def combine_and_filter(lst, threshold):
    # Write code here
    lst2 = []
    for i in range (len(lst)):
        if (lst[i] > threshold):
            lst2.append(lst[i])
    lst2.sort()
    return lst2