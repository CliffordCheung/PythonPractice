lst = input().split(",")
# Write your code below
lst2 = []
for i in range (len(lst)):
    if len(lst[i]) > 5:
        lst2.append(lst[i])
print (lst2)