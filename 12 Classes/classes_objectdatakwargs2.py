class Duck:
    def __init__(self, **kwargs):
        self._variables = kwargs

    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("*waddles*")

    def set_variable(self, k, v):
        self._variables[k] = v

    def get_variable(self, k):
        return self._variables.get(k, None)


def main():
    donald = Duck(color = "blue", feet = 2)
    fergus = Duck(feet = 2)
    print(donald.get_variable("color"))
    print(donald.get_variable("feet"))
    print(fergus.get_variable("color"))
    print(fergus.get_variable("feet"))

    print(donald.set_variable("color", "pink"))
    print(donald.get_variable("color"))


if __name__ == "__main__":
    main()
