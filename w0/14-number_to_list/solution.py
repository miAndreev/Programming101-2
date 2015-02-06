def number_to_list(n):
    list_result = []
    while n > 0:
        list_result.append(n%10)
        n = n//10

    list_result.reverse()
    return list_result