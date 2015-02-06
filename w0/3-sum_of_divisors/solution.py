def sum_of_divisors(n):
    output_sum = 0
    current_n = n
    for i in range(1,n+1):
        if (n % i) == 0:
            output_sum = output_sum + i
    return output_sum