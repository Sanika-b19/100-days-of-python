# Project: Extend the Student Class with More Attributes and Methods

class StudentRecord:
    def __init__(self, name, roll_number, marks, address, phone_number, email):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'

    def update_address(self, new_address):
        self.address = new_address

    def update_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def update_email(self, new_email):
        self.email = new_email

    def has_passed(self, passing_grade=60):
        return self.marks >= passing_grade

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")
        print(f"Address: {self.address}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")

student = StudentRecord("John Doe", 101, 85, "123 Main St", "555-1234", "john.doe@example.com")
student.display()
print(f"Passed: {student.has_passed()}")  # Output: Passed: True
