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
    for i in range(generate_N_numbers):
        rand_number = randint(0, 1001)
    file.write(str(rand_number))
    file.write("\n")
    file.close()
# PROGRAM RUN
if __name__ == '__main__':
    main()