def filter_and_square(numbers):
    # Write code here
    new_numbers = [number**2 for number in numbers if number>0]
    return new_numbers