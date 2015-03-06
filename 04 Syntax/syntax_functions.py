def main():
    func(1, 11)
    func(3, 7)
    func(5, 12)


def func(a, b):
    for i in range(a, b):
        print(i, end=" ")
    print()

if __name__ == "__main__":
    main()
