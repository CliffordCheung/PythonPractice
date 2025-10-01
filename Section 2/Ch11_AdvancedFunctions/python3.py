# Read a number from input
number = int(input())

# Define your lambda function here
categorize_number = lambda ans: "Positive" if number > 0 else "Negative" if number<0 else "Zero"

# Call your lambda function with the input number and print the result
print(categorize_number(number))
