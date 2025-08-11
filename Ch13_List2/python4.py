lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
length_list1 = len(lst1)
lst3 = []
for i in range (len(lst1)):
    if lst1[i] not in lst2:
        lst3.append(lst1[i])
print(lst3)