class Duck:
    def __init__(self, color = "white"):
        self._color = color

    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("*waddles*")

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


def main():
    donald = Duck()
    print(donald.get_color())
    donald.set_color("blue")
    print(donald.get_color())


if __name__ == "__main__":
    main()
