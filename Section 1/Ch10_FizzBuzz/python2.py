def fizzbuzz(num):
    if(num%3==0 and num%7==0):
        print("FizzBuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%7==0):
        print("Buzz")
    else:
        print(num)
    
print("Welcome to FizzBuzz!")
num1 = int(input())
fizzbuzz(num1)
