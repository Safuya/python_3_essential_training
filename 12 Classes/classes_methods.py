class Duck:
    def __init__(self, value):
        self._v = value

    def quack(self):
        print("Quaaack!", self._v)

    def walk(self):
        print("*waddles*", self._v)


def main():
    donald = Duck(42)
    frank = Duck(151)
    donald.quack()
    donald.walk()
    frank.quack()
    frank.walk()


if __name__ == "__main__":
    main()
