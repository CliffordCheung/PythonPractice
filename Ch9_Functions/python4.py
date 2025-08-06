def sigma(n):
    ans = 0
    for i in range (1,n):
        ans += i
    ans += n
    return (ans)

num1 = int(input())
result = sigma(num1)
print (result)