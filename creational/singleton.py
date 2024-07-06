# Singleton is a creational design pattern that lets you ensure that a class has only one instance,
# while providing a global access point to this instance.


class DatabaseConnection:
    pass


class Database:
    __connection: DatabaseConnection = None

    @classmethod
    def get_connection(cls):
        if not cls.__connection:
            cls.__connection = DatabaseConnection()
        return cls.__connection


def main():
    print(Database.get_connection())
    print(Database.get_connection())
    print(Database.get_connection())


main()
