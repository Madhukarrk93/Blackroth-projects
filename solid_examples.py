
"""Examples of the five SOLID principles in Python."""

from abc import ABC, abstractmethod


# ============================================================
# S - Single Responsibility Principle (SRP)
# A class should have one main responsibility.
# ============================================================

class Invoice:
    """Store invoice details."""

    def __init__(self, customer: str, amount: float) -> None:
        self.customer = customer
        self.amount = amount


class InvoicePrinter:
    """Handle invoice printing."""

    @staticmethod
    def print_invoice(invoice: Invoice) -> None:
        print(
            f"Invoice for {invoice.customer}: "
            f"Rs. {invoice.amount:.2f}"
        )


# ============================================================
# O - Open/Closed Principle (OCP)
# Classes should be open for extension but closed for
# modification.
# ============================================================

class Discount(ABC):
    """Define the discount interface."""

    @abstractmethod
    def calculate(self, amount: float) -> float:
        """Calculate the discounted amount."""
        raise NotImplementedError


class NoDiscount(Discount):
    """Apply no discount."""

    def calculate(self, amount: float) -> float:
        return amount


class TenPercentDiscount(Discount):
    """Apply a ten percent discount."""

    def calculate(self, amount: float) -> float:
        return amount * 0.90


class Checkout:
    """Calculate the final price using a discount strategy."""

    def __init__(self, discount: Discount) -> None:
        self.discount = discount

    def final_price(self, amount: float) -> float:
        return self.discount.calculate(amount)


# ============================================================
# L - Liskov Substitution Principle (LSP)
# Subclasses should be usable wherever their base class
# is expected, without breaking the expected behavior.
# ============================================================

class Bird(ABC):
    """Define the behavior expected of a bird."""

    @abstractmethod
    def move(self) -> str:
        """Describe how the bird moves."""
        raise NotImplementedError


class FlyingBird(Bird):
    """Represent a bird that can fly."""

    def move(self) -> str:
        return "Flying in the sky"


class Penguin(Bird):
    """Represent a bird that swims instead of flying."""

    def move(self) -> str:
        return "Swimming in the water"


def describe_movement(bird: Bird) -> None:
    """Use any bird according to its movement contract."""
    print(bird.move())


# ============================================================
# I - Interface Segregation Principle (ISP)
# Clients should not be forced to implement methods they
# do not need.
# ============================================================

class Printer(ABC):
    """Define printing behavior."""

    @abstractmethod
    def print_document(self, document: str) -> str:
        """Print a document."""
        raise NotImplementedError


class Scanner(ABC):
    """Define scanning behavior."""

    @abstractmethod
    def scan_document(self, document: str) -> str:
        """Scan a document."""
        raise NotImplementedError


class SimplePrinter(Printer):
    """A printer that only prints."""

    def print_document(self, document: str) -> str:
        return f"Printed: {document}"


class MultiFunctionPrinter(Printer, Scanner):
    """A device that prints and scans."""

    def print_document(self, document: str) -> str:
        return f"Printed: {document}"

    def scan_document(self, document: str) -> str:
        return f"Scanned: {document}"


# ============================================================
# D - Dependency Inversion Principle (DIP)
# High-level modules should depend on abstractions, not
# concrete implementations.
# ============================================================

class MessageSender(ABC):
    """Define a message-sending abstraction."""

    @abstractmethod
    def send(self, message: str) -> str:
        """Send a message."""
        raise NotImplementedError


class EmailSender(MessageSender):
    """Send messages by email."""

    def send(self, message: str) -> str:
        return f"Email sent: {message}"


class SMSSender(MessageSender):
    """Send messages by SMS."""

    def send(self, message: str) -> str:
        return f"SMS sent: {message}"


class NotificationService:
    """Send notifications through an injected sender."""

    def __init__(self, sender: MessageSender) -> None:
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)


# ============================================================
# Run all examples
# ============================================================

def main() -> None:
    """Demonstrate all five SOLID principles."""

    print("\n--- S: Single Responsibility Principle ---")
    invoice = Invoice("Rahul", 1500.00)
    InvoicePrinter.print_invoice(invoice)

    print("\n--- O: Open/Closed Principle ---")
    original_amount = 1000.00
    checkout = Checkout(TenPercentDiscount())
    print(f"Original price: Rs. {original_amount:.2f}")
    print(f"After discount: Rs. {checkout.final_price(original_amount):.2f}")

    print("\n--- L: Liskov Substitution Principle ---")
    describe_movement(FlyingBird())
    describe_movement(Penguin())

    print("\n--- I: Interface Segregation Principle ---")
    printer = SimplePrinter()
    print(printer.print_document("SOLID Principles"))
    device = MultiFunctionPrinter()
    print(device.print_document("OOP Notes"))
    print(device.scan_document("OOP Notes"))

    print("\n--- D: Dependency Inversion Principle ---")
    email_service = NotificationService(EmailSender())
    sms_service = NotificationService(SMSSender())
    print(email_service.notify("Welcome to the library!"))
    print(sms_service.notify("Your book is due soon!"))

    print("\nAll SOLID examples completed successfully!")


if __name__ == "__main__":
    main()
