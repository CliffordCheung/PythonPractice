def prod(lst):
    ans = 1
    for i in range (len(lst)):
        ans *= lst[i]
    return ans