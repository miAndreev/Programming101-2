def is_an_bn(word):
    word_len = len(word)

    if word == "" or word_len == 1:
        return True
    
    if word_len %2 != 0:
        return False

    middle = len(word) // 2
    first_half = word[:middle]
    second_half = word[middle:]

    if word == 'a'* middle + 'b'*middle:
        return True
    else:
        return False

   