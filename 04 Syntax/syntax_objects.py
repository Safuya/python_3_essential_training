class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind

    def what_kind(self):
        return self.kind


def main():
    fried = Egg()
    scrambled = Egg("scrambled")
    print(fried.what_kind())
    print(scrambled.what_kind())

if __name__ == "__main__":
    main()
