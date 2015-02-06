from sys import argv, exit
from random import randint

def sum_of_ints_from_file(file_name):
    file = open(file_name, "r")
    summ = 0
    for line in file:
        int_list = line.split()
        for i in int_list:
            summ = summ + int(i)
    file.close()
    return summ

def main():
    print(sum_of_ints_from_file(argv[1]))


if __name__ == '__main__':
    main()