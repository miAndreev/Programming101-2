import sys

def cat(filename):
    try:
        opened_file = open(filename, "r")
        contents = opened_file.read()
        opened_file.close()
    except IOError:
        return False
    
    return contents.rstrip()

def main():
    files_names = []
    try:
        for f_name_index in range(1, len(sys.argv)):
            files_names.append(sys.argv[f_name_index])
    except IndexError:
        return False
    for f_name in files_names:
        print(cat(f_name))
        print("")

if __name__ == '__main__':
    main()
