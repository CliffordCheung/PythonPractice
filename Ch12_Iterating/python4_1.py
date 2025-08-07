numbers = input()
prefix = input()
# Write your code below
numbers_new = numbers.split()
for index, item in enumerate(numbers_new):
    numbers_new[index] = prefix+item
print(numbers_new)
numbers = ' '.join(numbers_new)
print(numbers)

###
numbers = input()
prefix = input()
nums = numbers.split()
result_nums  = []
for num in nums:
    result_nums .append(prefix + num)
result = ' '.join(result_nums)
print(result)