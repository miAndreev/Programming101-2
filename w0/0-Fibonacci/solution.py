def nth_fibonacci(n):
    if n <= 2 :
        return 1
    else: 
        return nth_fibonacci(n-2) + nth_fibonacci(n-1)

