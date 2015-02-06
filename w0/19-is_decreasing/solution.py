def is_decreasing(seq):
    leng_seq = len(seq)
    if leng_seq < 2:
        return True

    for i in range(0, leng_seq-1):
        if seq[i] <= seq[i+1]:
            return False

    return True