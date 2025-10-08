def process_numbers(numbers):
    positive_numbers = filter(lambda x: x > 0, numbers)
    processed_numbers = map(lambda x: x * 2 if x % 2 == 0 else x * 3, positive_numbers)
    return list(processed_numbers)

numbers_list = [-4, 0, 5, 2, 8, -3, 7]
result = process_numbers(numbers_list)
print(result)