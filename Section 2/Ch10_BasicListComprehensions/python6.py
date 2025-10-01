def house_of_lists(list_of_lists):
    # Write code here
    filtered = [lst for lst in list_of_lists if sum(lst) < 50]
    # print(filtered)
    final = [num for nums in filtered for num in nums if num<5]
    #print(final)
    return final