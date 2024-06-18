# Builder is a creational design pattern that lets you construct complex objects step by step.
# The pattern allows you to produce different types and representations of an object using the same construction code.


class Car:
    number_of_seats = None
    engine = None
    self_driving = False


class Builder:
    def add_seats(self):
        pass

    def add_engine(self):
        pass

    def add_self_driving():
        pass


class CarBuilder(Builder):
    car: Car = None

    def __init__(self):
        self.car = Car()

    def add_seats(self, number_of_seats):
        self.car.number_of_seats = number_of_seats

    def add_engine(self, engine):
        self.car.engine = engine

    def add_self_driving(self):
        self.car.self_driving = True

    def get_product(self):
        return self.car


def main():
    # You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called director.
    builder = CarBuilder()
    builder.add_seats(2)
    builder.add_engine("Sport engine")
    car = builder.get_product()
    print(car.number_of_seats, car.engine, car.self_driving)

    builder = CarBuilder()
    builder.add_seats(7)
    builder.add_engine("Self-driving engine")
    builder.add_self_driving()
    car = builder.get_product()
    print(car.number_of_seats, car.engine, car.self_driving)


main()
