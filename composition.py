class Animal:
    pass


def poop(animal: Animal):
    animal.poop = lambda: print("poop")
    return animal


def bark(animal: Animal):
    animal.bark = lambda: print("bark")
    return animal


def meow(animal: Animal):
    animal.meow = lambda: print("meow")
    return animal


def main():
    dog: Animal = Animal()
    dog = poop(dog)
    dog = bark(dog)
    dog.poop()
    dog.bark()

    cat: Animal = Animal()
    cat = poop(cat)
    cat = meow(cat)
    dog.poop()
    cat.meow()


main()
