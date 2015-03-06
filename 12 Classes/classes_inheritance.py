class Animal:
    def talk(self):
        print("I have something to say!")

    def walk(self):
        print("Hey! I'm walkin' here!")

    def clothes(self):
        print("I have nice clothes.")


class Duck(Animal): # Duck is an Animal. Has access to animal methods
    def quack(self):
        print("Quaaack!")

    def walk(self):
        super().walk()
        print("*waddles*")


class Dog(Animal):
    def clothes(self):
        print("I have blonde fur.")


def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.clothes()

    truffle = Dog()
    truffle.clothes()
    truffle.walk()


if __name__ == "__main__":
    main()
