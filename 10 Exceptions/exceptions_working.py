def main():
    try:
        for line in read_file('lines.doc'):
            print(line.strip())
    except IOError as e:
        print("Can't read file:", e)
    except ValueError as e:
        print("Bad filename:", e)


def read_file(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')


if __name__ == "__main__":
    main()
