from sys import argv, exit
from random import randint

def main():
    if len(argv) < 3:
        exit("Error: Not enough arguments given!")

    filename = argv[1]
    generate_N_numbers = 0
    try:
        generate_N_numbers = int(argv[2])
    except ValueError:
        exit("Error: Make sure you provide numbers as 3rd argument!")
    
    file = open(filename, "w")
    print (generate_N_numbers)
    rand_number = []
    for i in range(0,generate_N_numbers):
        rand_number.append(str(randint(0, 1001)))

    file.write(" ".join(rand_number))
    file.write("\n")
    file.close()
# PROGRAM RUN
if __name__ == '__main__':
    main()