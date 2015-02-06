def count_words(arr):
    words_count = {}

    for i in range(0, len(arr)):
        if words_count.has_key(arr[i]):
            words_count[arr[i]] = words_count[arr[i]] + 1
        else:
            words_count[arr[i]] = 1

    return words_count