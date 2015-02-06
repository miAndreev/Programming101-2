def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]

    if nominator == 1 or denominator == 1:
        return fraction
    
    range_to_check = []
    if nominator < denominator:
        range_to_check = range(2, nominator+1)
    else:   
        range_to_check = range(2, denominator+1)

    for i in range_to_check:
        if nominator%i == 0 and denominator%i == 0:
            nominator = nominator/i
            denominator = denominator/i

    return (nominator, denominator)


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