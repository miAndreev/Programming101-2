def list_to_number(digits):
    result_number = 0
    for i in range(0, len(digits)):
        result_number = result_number*10 + digits[i]

    return result_number