def main():
    testfunc(one = 1, two = 2, four = 42)


def testfunc(**kwargs):
    print("This is a test function", kwargs["one"], kwargs["four"])
    print("Must be named, tuple then keywords in that order.")


if __name__ == "__main__":
    main()
