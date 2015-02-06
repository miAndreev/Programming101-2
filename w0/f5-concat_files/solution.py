from sys import argv, exit

def conat_file(files):
    out_file = open('MEGATRON', 'w')

    for f in files:
        in_file = open(f, 'r')
        for line in in_file:
            out_file.write(line)
        out_file.write('\n\n')
        in_file.close()
    out_file.close()


def main():
    files = []
    for f in range(1, len(argv)):
        files.append(argv[f])

    conat_file(files)


if __name__ == '__main__':
    main()