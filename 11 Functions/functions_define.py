def main():
    testfunc(42, 54, 72, 13)


def testfunc(number, *args):
    print("This is a test function", number, args)


if __name__ == "__main__":
    main()
