lst = input().split()
# Write your code below
lst2 = []
for index, item in enumerate(lst):
    if len(lst[index]) > 3 or item.lower().startswith('a'):
        lst2.append(index)
print(lst2)