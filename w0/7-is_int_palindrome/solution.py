def is_int_palindrome(n):
    n_string = str(n)
    n_len = len(n_string)
    for i in range(0, n_len//2):
        if n_string[i] != n_string[n_len-1-i]:
            return False

    return True
