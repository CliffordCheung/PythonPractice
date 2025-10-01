def count_down(n):
    # Write code here
    if n == 0:
        print(n)
        return 
    print(n)
    count_down(n-1)
    