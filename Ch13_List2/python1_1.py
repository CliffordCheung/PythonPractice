input_list = input().split(', ')
# Write your code belowinput_list = input().split(', ')
# Write your code below
length = len(input_list)
if length >= 5:
    print(input_list[:2] + input_list[-2:])
else:
    print([input_list[0], input_list[-1]])