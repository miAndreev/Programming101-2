def calculate_coins(summ):
    coins = {}
    summ = summ*100

    for i in [100, 50, 20, 10, 5, 2, 1]:
        count = 0
        while summ >= i:
            count = count + 1
            summ = summ - i

        coins[i] = count

    return coins

