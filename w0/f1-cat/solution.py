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
    filename = ""
    try:
        filename = sys.argv[1]
    except IndexError:
        return False
    
    print(cat(filename))

if __name__ == '__main__':
    main()
