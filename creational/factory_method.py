# Factory Method is a creational design pattern that provides an interface for creating objects in a superclass,
# but allows subclasses to alter the type of objects that will be created.
# SOLID Open-Closed Principle: Open for extension but closed for modification


class Transport:  # Interface
    def deliver():
        pass


class Truck(Transport):
    def deliver(self):
        print("Road")


class Ship(Transport):
    def deliver(self):
        print("Sea")


class Plane(Transport):
    def deliver(self):
        print("Air")


class Logistic:
    def plan_delivery(self):
        transport = self.create_transport()
        transport.deliver()

    def create_transport(self) -> Transport:
        pass


class RoadLogistic(Logistic):
    def create_transport(self):
        return Truck()


class SeaLogistic(Logistic):
    def create_transport(self):
        return Ship()


class AirLogistic(Logistic):
    def create_transport(self):
        return Plane()


def main():
    method = "air"

    if method == "road":
        logistic = RoadLogistic()
    elif method == "sea":
        logistic = SeaLogistic()
    elif method == "air":
        logistic = AirLogistic()

    logistic.plan_delivery()


main()
