class Duck:
    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("*waddles*")


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == "__main__":
    main()
