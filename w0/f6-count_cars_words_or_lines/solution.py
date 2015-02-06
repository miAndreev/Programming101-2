from sys import argv, exit

def count_chars(file_name):

    file = open(file_name, 'r')
    content = file.read()
    words = content.split(" ")
    count = 0
    for el in content:
        count = count + len(el)

    file.close()
    return count

def count_words(file_name):

    file = open(file_name, 'r')
    count = len(file.read().split())
    file.close()
    return count

def count_lines(file_name):
    file = open(file_name, 'r')
    content = file.read()
    num_lines = content.count("\n") + 1
    file.close()
    return num_lines

def main():
    if argv[1] == 'chars':
        print(count_chars(argv[2]))
    elif argv[1] == 'words':
        print(count_words(argv[2]))
    elif argv[1] == 'lines':
        print(count_lines(argv[2]))



if __name__ == '__main__':
    main()