def print_sequence(n):
    # Write code here
    if n==0:
        print("Blast off!")
        return
    print("T-minus",n)
    print_sequence(n-1)