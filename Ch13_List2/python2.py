lst = input().split(",")
# Write your code below
print(lst[1::3])
print(lst[5::-1])
length = len(lst)
length = length//2
print(lst[length::2])