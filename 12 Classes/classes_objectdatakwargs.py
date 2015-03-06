class Duck:
    def __init__(self, **kwargs):
        self._color = kwargs.get("color", "white")

    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("*waddles*")

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color


def main():
    donald = Duck(color = "blue")
    fergus = Duck()
    print(donald.get_color())
    print(fergus.get_color())


if __name__ == "__main__":
    main()
