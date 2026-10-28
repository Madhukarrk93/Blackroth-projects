
"""Ten practical Python OOP coding challenges."""


# Challenge 1: Student Class
import math


class Student:
    """Store student details and calculate the average marks."""

    def __init__(self, name: str, marks: list[float]) -> None:
        self.name = name
        self.marks = marks

    def calculate_average(self) -> float:
        """Return the average of the student's marks."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def display_details(self) -> None:
        """Display student details and average marks."""
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Average Marks: {self.calculate_average():.2f}")


def main() -> None:
    print("=== Challenge 1: Student Class ===")

    student = Student("Rahul", [85, 90, 78])
    student.display_details()


if __name__ == "__main__":
    main()


# Challenge 2: Bank Account
class BankAccount:
    """Manage a bank account with deposit and withdrawal operations."""

    def __init__(self, account_holder: str, balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add money to the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.balance += amount
        print(f"Deposited: Rs. {amount:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money if sufficient balance is available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawn: Rs. {amount:.2f}")

    def display_balance(self) -> None:
        """Display the current account balance."""
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: Rs. {self.balance:.2f}")


# Challenge 3: Employee Management
class Employee:
    """Store employee details and calculate annual salary."""

    def __init__(
        self, name: str, employee_id: int, monthly_salary: float
    ) -> None:
        self.name = name
        self.employee_id = employee_id
        self.monthly_salary = monthly_salary

    def calculate_annual_salary(self) -> float:
        """Calculate the employee's annual salary."""
        return self.monthly_salary * 12

    def display_details(self) -> None:
        """Display employee information."""
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Monthly Salary: Rs. {self.monthly_salary:.2f}")
        print(
            f"Annual Salary: Rs. "
            f"{self.calculate_annual_salary():.2f}"
        )


# Challenge 4: Vehicle Inheritance
class Vehicle:
    """Represent a general vehicle."""

    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def display_details(self) -> None:
        """Display vehicle information."""
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Car(Vehicle):
    """Represent a car inherited from Vehicle."""

    def __init__(
        self, brand: str, model: str, doors: int
    ) -> None:
        super().__init__(brand, model)
        self.doors = doors

    def display_details(self) -> None:
        """Display car information."""
        super().display_details()
        print(f"Number of Doors: {self.doors}")


class Motorcycle(Vehicle):
    """Represent a motorcycle inherited from Vehicle."""

    def __init__(self, brand: str, model: str, engine_cc: int) -> None:
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_details(self) -> None:
        """Display motorcycle information."""
        super().display_details()
        print(f"Engine Capacity: {self.engine_cc} cc")


# Challenge 5: Shape Area Calculator


class Shape:
    """Base class for shapes."""

    def area(self) -> float:
        """Return the shape's area."""
        raise NotImplementedError("Subclasses must implement area().")


class Circle(Shape):
    """Calculate the area of a circle."""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    """Calculate the area of a rectangle."""

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


# Challenge 6: Shopping Cart
class ShoppingCart:
    """Manage items and their prices in a shopping cart."""

    def __init__(self) -> None:
        self.items: list[tuple[str, float]] = []

    def add_item(self, name: str, price: float) -> None:
        """Add an item to the cart."""
        if price < 0:
            print("Price cannot be negative.")
            return

        self.items.append((name, price))
        print(f"Added: {name} - Rs. {price:.2f}")

    def calculate_total(self) -> float:
        """Calculate the total price of all items."""
        return sum(price for _, price in self.items)

    def display_cart(self) -> None:
        """Display all items and the total price."""
        print("\nCart Items:")
        for name, price in self.items:
            print(f"{name}: Rs. {price:.2f}")

        print(f"Total: Rs. {self.calculate_total():.2f}")


# Challenge 7: Movie Rating
class Movie:
    """Store movie details and manage ratings."""

    def __init__(self, title: str) -> None:
        self.title = title
        self.ratings: list[float] = []

    def add_rating(self, rating: float) -> None:
        """Add a rating between 1 and 10."""
        if not 1 <= rating <= 10:
            print("Rating must be between 1 and 10.")
            return

        self.ratings.append(rating)
        print(f"Rating {rating:.1f} added for {self.title}.")

    def average_rating(self) -> float:
        """Calculate the average movie rating."""
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)

    def display_details(self) -> None:
        """Display the movie and its average rating."""
        print(f"Movie: {self.title}")
        print(f"Number of Ratings: {len(self.ratings)}")
        print(f"Average Rating: {self.average_rating():.2f}/10")


# Challenge 8: Hospital Patient Records
class Patient:
    """Store and display hospital patient records."""

    def __init__(
        self,
        patient_id: int,
        name: str,
        diagnosis: str,
        room_number: int,
    ) -> None:
        self.patient_id = patient_id
        self.name = name
        self.diagnosis = diagnosis
        self.room_number = room_number

    def display_record(self) -> None:
        """Display the patient's record."""
        print(f"Patient ID: {self.patient_id}")
        print(f"Patient Name: {self.name}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Room Number: {self.room_number}")


# Challenge 9: School Result Processing
class SchoolResult:
    """Calculate and display a student's school result."""

    def __init__(self, student_name: str, marks: list[float]) -> None:
        self.student_name = student_name
        self.marks = marks

    def calculate_total(self) -> float:
        """Calculate total marks."""
        return sum(self.marks)

    def calculate_percentage(self) -> float:
        """Calculate percentage assuming each subject is out of 100."""
        if not self.marks:
            return 0.0
        return self.calculate_total() / len(self.marks)

    def get_result(self) -> str:
        """Return Pass if every subject has at least 35 marks."""
        if not self.marks:
            return "No marks available"
        if all(mark >= 35 for mark in self.marks):
            return "Pass"
        return "Fail"

    def display_result(self) -> None:
        """Display the student's result."""
        print(f"Student Name: {self.student_name}")
        print(f"Total Marks: {self.calculate_total():.0f}")
        print(f"Percentage: {self.calculate_percentage():.2f}%")
        print(f"Result: {self.get_result()}")


# Challenge 10: Online Course Management
class OnlineCourse:
    """Manage an online course and its enrolled students."""

    def __init__(self, course_name: str, instructor: str) -> None:
        self.course_name = course_name
        self.instructor = instructor
        self.students: list[str] = []

    def enroll_student(self, student_name: str) -> None:
        """Enroll a student if they are not already enrolled."""
        if student_name in self.students:
            print(f"{student_name} is already enrolled.")
            return

        self.students.append(student_name)
        print(f"{student_name} enrolled successfully.")

    def display_course(self) -> None:
        """Display course details and enrolled students."""
        print(f"Course: {self.course_name}")
        print(f"Instructor: {self.instructor}")
        print(f"Total Enrolled Students: {len(self.students)}")
        print(f"Students: {', '.join(self.students)}")


def main() -> None:
    print("=== Challenge 1: Student Class ===")
    student = Student("Rahul", [85, 90, 78])
    student.display_details()

    print("\n=== Challenge 2: Bank Account ===")
    account = BankAccount("Rahul", 1000.00)
    account.deposit(500.00)
    account.withdraw(200.00)
    account.display_balance()

    print("\n=== Challenge 3: Employee Management ===")
    employee = Employee("Priya", 101, 25000.00)
    employee.display_details()

    print("\n=== Challenge 4: Vehicle Inheritance ===")

    car = Car("Toyota", "Innova", 4)
    car.display_details()

    print("\nMotorcycle Details:")
    bike = Motorcycle("Yamaha", "R15", 155)
    bike.display_details()

    print("\n=== Challenge 5: Shape Area Calculator ===")

    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print(f"Circle Area: {circle.area():.2f}")
    print(f"Rectangle Area: {rectangle.area():.2f}")

    print("\n=== Challenge 6: Shopping Cart ===")

    cart = ShoppingCart()
    cart.add_item("Keyboard", 1200.00)
    cart.add_item("Mouse", 500.00)
    cart.add_item("Headphones", 800.00)
    cart.display_cart()

    print("\n=== Challenge 7: Movie Rating ===")

    movie = Movie("RRR")
    movie.add_rating(9.0)
    movie.add_rating(8.5)
    movie.add_rating(9.5)
    movie.display_details()

    print("\n=== Challenge 8: Hospital Patient Records ===")

    patient = Patient(1001, "Ravi", "Fever", 205)
    patient.display_record()

    print("\n=== Challenge 9: School Result Processing ===")

    result = SchoolResult("Rahul", [85, 90, 78])
    result.display_result()

    print("\n=== Challenge 9: School Result Processing ===")

    result = SchoolResult("Anjali", [85, 78, 92, 88, 90])
    result.display_result()

    print("\n=== Challenge 10: Online Course Management ===")

    course = OnlineCourse("Python OOP", "Mr. Kumar")
    course.enroll_student("Rahul")
    course.enroll_student("Priya")
    course.enroll_student("Anjali")
    course.display_course()


if __name__ == "__main__":
    main()
