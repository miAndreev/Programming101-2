def sum_of_digits(n):
    if n < 0:
        n = -n
    leng_of_number = len(str(n))
    output_sum = 0
    '''for i in range(leng_of_number): '''
    while n>0:
        
        output_sum = output_sum + n %10
        n = n //10

    return output_sum