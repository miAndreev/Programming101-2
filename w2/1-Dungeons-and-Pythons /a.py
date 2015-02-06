def main():
    f = open("basic_dungeon.txt", "r")
    a = f.read().split()
    b = [list(i) for i in a]
    print ("".join(b))
    print (str(b[0]))

if __name__ == '__main__':
    main()