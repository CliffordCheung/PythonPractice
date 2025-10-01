def elements_of_freedom(elements):
    # Your solution here
    
    # Step 1: Filter elements with length >= 5
    filtered = [lst for lst in elements if len(lst) >= 5]
    print(filtered)
    # Step 2: Convert filtered elements to uppercase
    upper = [word.upper() for word in filtered]
    print(upper)
    # Step 3: Create a list of unique elements
    new_list = list(dict.fromkeys(upper))
    print(new_list)
    
    # Step 4: Return the final result
    #return new_list
    
print("Here is the start of program")
elements_of_freedom(["apple", "banana", "cherry", "date", "apple", "banana", "grape", "fig"])