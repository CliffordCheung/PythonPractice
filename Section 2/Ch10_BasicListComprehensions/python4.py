def sum_positive_evens(numbers):
    # Write code here
    total = sum([number for number in numbers if (number%2==0 and number>0)])
    return total