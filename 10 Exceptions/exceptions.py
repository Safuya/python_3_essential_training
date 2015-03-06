def main():
    try:
        fh = open('xlines.txt')
    except IOError as e:
        print('Could not open the file:', e)
    else:
        for line in fh: print(line.strip())


if __name__ == "__main__":
    main()
