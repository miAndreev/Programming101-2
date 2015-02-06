def count_vowels(string): 
    count = 0

    vowels = "aeyuioAEYUIO"

    for i in range(0, len(string)):
        if string[i] in vowels:
            count = count + 1

    return count    