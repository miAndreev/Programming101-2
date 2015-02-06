def sevens_in_a_row(arr, n):
    count = 0
    for index in range(len(arr)):
        if arr[index] == 7:
            count=+1
            if count == n:
                return True
        else:
            count = 0
    if count >= n:
        return True
    else:
        return False

