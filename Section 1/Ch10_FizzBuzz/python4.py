def fizzbuzz(num):
    if(num%3==0 and num%7==0):
        print("FizzBuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%7==0):
        print("Buzz")
    else:
        char1 = str(num)
        if "3" in char1:
            print("Almost Fizz")
        else:
            print(num)
    
print("Welcome to FizzBuzz!")
num1 = int(input())
for i in range (num1):
    fizzbuzz(i+1)