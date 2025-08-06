def print_pattern(rows, cols):
    # Write your code here
    for i in range (rows):
        for i in range (cols):
            print('*', end = "")
        print()
    pass

# Get input for rows and columns
rows = int(input())
cols = int(input())

# Call the function
print_pattern(rows, cols)