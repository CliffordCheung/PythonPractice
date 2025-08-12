# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
# Your code here
for i in range(30, 81):
    if (i%4 ==0):
        print(i, end=", ")
    else:
        continue

print()  # new line
# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
# Your code here
num = 1
i = 15
while (num <= 8):
    if i%2 == 1:
        print(i, end=", ")
        num += 1
    i += 1
    
print()  # new line
# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
# Your code here
for i in range (50, 9, -1):
    if i%5 == 0:
        print(i, end=", ")
    else:
        continue

print()  # new line
# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
# Your code here
ans = 1
for i in range (1, 31):
    if i%3 == 0:
        ans *= i
    else:
        continue
print(ans)