# Singleton is a creational design pattern that lets you ensure that a class has only one instance,
# while providing a global access point to this instance.
from random import random


class Database:
    con = None

    @classmethod
    def get_connection(cls):
        print(cls.con)
        if not cls.con:
            cls.con = random()
        return cls.con


def main():
    Database.get_connection()
    Database.get_connection()
    Database.get_connection()


main()
