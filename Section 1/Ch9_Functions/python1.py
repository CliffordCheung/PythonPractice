def cal():
    num1 = int(input())
    for i in range (num1):
        ans = 0
        for j in range (1, 10001):
            ans += j
        print (ans)

cal()
