def magic_square(matrix):
    summ_in_the_sqare = 0
    test_summ = 0

    for line in matrix:
        for i in line:
            test_summ = test_summ + i
            
        if summ_in_the_sqare == 0:
            summ_in_the_sqare = test_summ

        if summ_in_the_sqare != test_summ:
             return False

        test_summ = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            test_summ = test_summ + matrix[j][i]

        if summ_in_the_sqare == 0:
            summ_in_the_sqare = test_summ

        if summ_in_the_sqare != test_summ:
             return False
        test_summ = 0

    for i in range(0, len(matrix)):
        test_summ = test_summ + matrix[i][i]

    if test_summ != summ_in_the_sqare:
        return False
    summ_in_the_sqare = test_summ
    test_summ = 0

    for i in range(0, len(matrix)):
        test_summ = test_summ + matrix[i][-i+2]

    if test_summ != summ_in_the_sqare:
        return False

    return True

def main():
    print(magic_square([[4,9,2], [3,5,7], [8,1,6]]))


if __name__ == '__main__':
    main()