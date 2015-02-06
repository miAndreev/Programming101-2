def unique_words_count(arr):
    unique_words = []

    for i in range(0, len(arr)):
        if arr[i] not in unique_words:
            unique_words.append(arr[i])

    return len(unique_words)