n = int(input())
end = n+1
for i in range (1, end):
    if n%i == 0:
        ans = int(n/i)
        print(f'{i} {ans}')
    else:
        continue