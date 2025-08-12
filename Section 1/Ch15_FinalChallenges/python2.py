def find_occurrences(text, pattern):
    # Write your code here
    if pattern in text:
        result1 = True
    else:
        result1 = False
    count = 0
    occ_list = []    
    for i in range (len(text)):
        text1 = str(text[i:])
        if text1.startswith(pattern):
            count += 1
            occ_list.append(i)
    result_tuple = (result1, count, occ_list)
    return (result_tuple)
    
            
            
            
    pass

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)