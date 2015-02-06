def biggest_difference(arr):
    result_difference = 0

    for i in range(len(arr)):
        for j in range(len(arr)-i):
            difference = arr[i] - arr[j]
            if difference > 0:
                difference = - difference
            if difference < result_difference:
                result_difference = difference

    return result_difference