def count_consonants(string):
    count = 0

    consonants = "bcdfghjklmnpqrstvwxzBCDEFGHJKLMNPQRSTVWXZ"

    for i in range(0, len(string)):
        if string[i] in consonants:
            count = count + 1

    return count
    