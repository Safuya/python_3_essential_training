def main():
    s = 'this is a string'
    for i, c in enumerate(s):
        print(i, c)

    for i, c in enumerate(s):
        if c == 's': print('index {} is an s'.format(i))


if __name__ == "__main__":
    main()
