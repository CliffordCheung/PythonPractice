def not_mutual_friends(list1, list2):
    # Write your code below
    list3 = []
    for i in range (len(list1)):
        if list1[i] not in list2:
            list3.append(list1[i])
    for j in range (len(list2)):
        if list2[j] not in list1:
            list3.append(list2[j])
    return list3