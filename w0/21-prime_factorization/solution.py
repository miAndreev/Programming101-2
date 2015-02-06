def prime_factorization(n):
    factorization = []
    factors = []
    for i in range(2,n+1):
        if is_prime(i):
            count = 0
            while n%i == 0:
                count = count + 1
                n = n / i
            if count > 0:    
                factors.append((i, count))
                
    return factors


def is_prime(n):
    if n < 0:
        n = -n
    if n == 1:
        return False

    for i in range(2,n-1):
        if (n%i)==0:
            return False

    return True