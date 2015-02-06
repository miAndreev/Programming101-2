def nth_fib_lists(listA, listB, n):
    position = 2
    
    while position < n + 1:
        following = listA + listB
        listA = listB
        listB = following
        position += 1

    return listA