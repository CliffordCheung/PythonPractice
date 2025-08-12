lst = list(map(int, input().split(",")))
# Write your code below
lst2 = []
for index, item in enumerate(lst):
    if int(item) < 50 or int(item)%5==0:
        lst2.append(index)
print(lst2)
 