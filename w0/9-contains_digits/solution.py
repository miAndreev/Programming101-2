def contains_digits(number, digits):
    number_s = str(number)
    digits_s = str(digits)
    for i in range(0,len(digits)):
        if str(digits[i]) not in number_s:
            return False

    return True