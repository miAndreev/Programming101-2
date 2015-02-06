def is_prime(number):
    if number <= 1:
        return False
    divisor = 2
    while divisor < number:
        if number % divisor == 0:
            return False
        else:
            divisor += 1
    return True

def goldbach(n):
    goldbach = []
    for number in range(n):
        if is_prime(number) is True:
            if is_prime(n - number) is True:
                goldbach.append((number, n - number))
    for current in goldbach:
        for following in goldbach:
            if current[0] == following[0]:
                if goldbach.index(current) != goldbach.index(following):
                    del goldbach[goldbach.index(following)]
    return goldbach