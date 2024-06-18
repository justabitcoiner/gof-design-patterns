# Abstract Factory is a creational design pattern that lets you produce families of related objects
# without specifying their concrete classes.


class Table:
    pass


class ModernTable(Table):
    def desc(self):
        print("This is modern table")


class ClassicTable(Table):
    def desc(self):
        print("This is classic table")


class Chair:
    pass


class ModernChair(Chair):
    def desc(self):
        print("This is modern chair")


class ClassicChair(Chair):
    def desc(self):
        print("This is classic chair")


class FurnitureFactory:
    def get_table(self):
        pass

    def get_chair(self):
        pass


class ModernFurnitureFactory(FurnitureFactory):
    def get_table(self):
        return ModernTable()

    def get_chair(self):
        return ModernChair()


class ClassicFurnitureFactory(FurnitureFactory):
    def get_table(self):
        return ClassicTable()

    def get_chair(self):
        return ClassicChair()


class FreestyleFurnitureFactory(FurnitureFactory):
    def get_table(self):
        return ModernTable()

    def get_chair(self):
        return ClassicChair()


def main():
    factory = ModernFurnitureFactory()
    factory.get_table().desc()
    factory.get_chair().desc()

    factory = ClassicFurnitureFactory()
    factory.get_table().desc()
    factory.get_chair().desc()

    factory = FreestyleFurnitureFactory()
    factory.get_table().desc()
    factory.get_chair().desc()


main()
