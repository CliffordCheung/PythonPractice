numbers = input().split(',')
# Write your code below
ans = 0
for i in range(len(numbers)):
    num = int(numbers[i])
    if num%2 == 0:
        ans += int(numbers[i])
print(ans)