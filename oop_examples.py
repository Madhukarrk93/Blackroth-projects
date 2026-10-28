
"""Practical examples of Python OOP concepts."""

from abc import ABC, abstractmethod


# 1. Encapsulation
class BankAccount:
    """Store account data and control withdrawals."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance


# 2. Single inheritance and method overriding
class Animal:
    """Base class for animals."""

    def speak(self) -> str:
        return "Animal makes a sound."


class Dog(Animal):
    """Dog inherits from Animal."""

    def speak(self) -> str:
        return "Dog barks."


# 3. Multiple inheritance
class Camera:
    def take_photo(self) -> str:
        return "Photo captured."


class Phone:
    def make_call(self) -> str:
        return "Call connected."


class SmartPhone(Camera, Phone):
    """Inherits features from Camera and Phone."""


# 4. Multilevel inheritance
class Vehicle:
    def move(self) -> str:
        return "Vehicle is moving."


class Car(Vehicle):
    pass


class ElectricCar(Car):
    def charge(self) -> str:
        return "Battery charging."


# 5. Hierarchical inheritance
class Shape:
    def describe(self) -> str:
        return "This is a shape."


class Circle(Shape):
    pass


class Rectangle(Shape):
    pass


# 6. Polymorphism through a common interface
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        """Send a notification."""


class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SMSNotification(Notification):
    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


# 7. Method overloading using default arguments
class Calculator:
    def add(self, a: float, b: float, c: float = 0) -> float:
        """Add two or three numbers."""
        return a + b + c


# 8. Composition: Car owns its Engine object
class Engine:
    def start(self) -> str:
        return "Engine started."


class VehicleWithEngine:
    def __init__(self) -> None:
        self.engine = Engine()

    def start(self) -> str:
        return self.engine.start()


# 9. Aggregation: a Library uses an external Book object
class Book:
    def __init__(self, title: str) -> None:
        self.title = title


class Library:
    def __init__(self, books: list[Book]) -> None:
        # Books are created outside and passed into the library.
        self.books = books

    def show_books(self) -> list[str]:
        return [book.title for book in self.books]


def main() -> None:
    """Run demonstrations of the OOP concepts."""

    print("1. Encapsulation")
    account = BankAccount("Vinith", 1000)
    account.deposit(500)
    print(account.get_balance())

    print("\n2. Inheritance and overriding")
    print(Dog().speak())

    print("\n3. Multiple inheritance")
    phone = SmartPhone()
    print(phone.take_photo())
    print(phone.make_call())

    print("\n4. Multilevel inheritance")
    print(ElectricCar().move())
    print(ElectricCar().charge())

    print("\n5. Hierarchical inheritance")
    print(Circle().describe())
    print(Rectangle().describe())

    print("\n6. Polymorphism")
    notifications: list[Notification] = [
        EmailNotification(),
        SMSNotification(),
    ]
    for notification in notifications:
        print(notification.send("Task completed"))

    print("\n7. Default arguments")
    calculator = Calculator()
    print(calculator.add(10, 20))
    print(calculator.add(10, 20, 30))

    print("\n8. Composition")
    print(VehicleWithEngine().start())

    print("\n9. Aggregation")
    books = [Book("Python Basics"), Book("Learning OOP")]
    library = Library(books)
    print(library.show_books())


if __name__ == "__main__":
    main()
