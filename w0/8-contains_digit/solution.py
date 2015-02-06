def contains_digit(number, digit):
    number_s = str(number)
    digit_s = str(digit)
    for i in range(0,len(number_s)):
        if number_s[i] == digit_s:
            return True

    return False