numbers = input().split()
# Write your code below
new_numbers = numbers + numbers[::-1]
new_numbers2 =  [numbers[0]] + new_numbers + [numbers[len(numbers)-1]]
final_numbers = new_numbers2 *2
print(final_numbers)