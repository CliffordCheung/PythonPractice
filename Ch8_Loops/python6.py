def print_range(start, end, step):
    # Write your code here
    for i in range(start, end, step):
        print (i)
    pass

# Get input from user
start = int(input())
end = int(input())
step = int(input())

# Call the function
print_range(start, end, step)