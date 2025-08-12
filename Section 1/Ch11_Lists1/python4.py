def merge(lst1, lst2):
    # Write code here
    for i in range (len(lst2)):
        lst1.append(lst2[i])
    lst1.sort()
    return (lst1)