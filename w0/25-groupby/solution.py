def groupby(func, seq):
    result = {}

    for i in seq:
        key = func(i)
        if key not in result:
            result[key] = [i]
        else:
            result[key].append(i)

    return result