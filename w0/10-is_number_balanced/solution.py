def is_number_balanced(n):
    n_str = str(n)
    n_len = len(n_str)
    half_len = n_len//2
    sum_left = 0
    sum_right = 0
    
    for i in range(0, half_len):
        sum_right = int(n_str[n_len-1-i]) + sum_right
        sum_left = int (n_str[i]) + sum_left

    if sum_left == sum_right:
        return True
    else:
        return False