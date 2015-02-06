def count_numbers(numbers_list):
    c = 0
    for a in numbers_list:
        for b in numbers_list:
            if b != 0:
                if a > b:
                    c = a // b
                if c not in numbers_list:
                    numbers_list.append(c)
    return len(numbers_list)-1