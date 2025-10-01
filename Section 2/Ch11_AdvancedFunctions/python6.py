def fibonacci(n):
    # Write code here
    total = 0
    if n<=2:
        if n==2:
            total += 1
        return total
    return total+fibonacci(n-1)+fibonacci(n-2)