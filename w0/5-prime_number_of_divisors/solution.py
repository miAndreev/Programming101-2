def prime_number_of_divisors(n):
    count = 0
    for devisor in range(1,n+1):
        if n%devisor == 0:
            count = count + 1

    if count == 2:
        return True
    if is_prime(count):
        return True
    else:
        return False



def is_prime(n):
    if n < 0:
        n = -n
    if n == 1:
        return False

    for i in range(2,n-1):
        if (n%i)==0:
            return False

    return True


def main():
    print()