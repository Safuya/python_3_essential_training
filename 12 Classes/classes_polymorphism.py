class Duck:
    def quack(self):
        print("Quaaack!")

    def walk(self):
        print("*waddles*")

    def bark(self):
        print("The duck can't bark.")

    def fur(self):
        print("The duck has feathers")


class Dog:
    def bark(self):
        print("Woof!")

    def fur(self):
        print("The dog has blonde fur.")

    def walk(self):
        print("*runs around in circles*")

    def quack(self):
        print("The dog can't quack.")


def main():
    donald = Duck()
    truffle = Dog()

    for o in (donald, truffle):
        o.quack()
        o.walk()
        o.bark()
        o.fur()


if __name__ == "__main__":
    main()
