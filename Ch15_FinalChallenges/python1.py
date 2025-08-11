n = int(input())
str1 = "*"
for i in range (n):
    if i%2 == 1:
        print(str1)
        str1 += "**"
print(str1)

n = int(input())
rows = int(n/2)+1
for i in range(rows):
    stars = ""
    stars += "*"*(2*(i+1)-1)
    print(stars)