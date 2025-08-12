lst = input().split(",")
# Write your code below
length  = len(lst)
if length%2 == 0:
    start = length//2 - 1
    print (lst[start:start+2])
else:
    start = length//2-1
    print (lst[start:start+3])
    
###
lst = input().split(",")
if len(lst) % 2 == 0:
    lst_mid = lst[len(lst)//2-1:len(lst)//2+1]
else:
    lst_mid = lst[len(lst)//2-1:len(lst)//2+2]
print(lst_mid)