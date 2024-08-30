# Project: Create Subclasses for Different Types of Students

class StudentRecord:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

class GraduateStudent(StudentRecord):
    def __init__(self, name, roll_number, marks, thesis_title):
        super().__init__(name, roll_number, marks)
        self.thesis_title = thesis_title

    def display(self):
        super().display()
        print(f"Thesis Title: {self.thesis_title}")

class UndergraduateStudent(StudentRecord):
    def __init__(self, name, roll_number, marks, major):
        super().__init__(name, roll_number, marks)
        self.major = major

    def display(self):
        super().display()
        print(f"Major: {self.major}")

class HighSchoolStudent(StudentRecord):
    def __init__(self, name, roll_number, marks, grade_level):
        super().__init__(name, roll_number, marks)
        self.grade_level = grade_level

    def display(self):
        super().display()
        print(f"Grade Level: {self.grade_level}")

grad_student = GraduateStudent("Alice", 101, 90, "AI in Education")
undergrad_student = UndergraduateStudent("Bob", 102, 85, "Computer Science")
high_school_student = HighSchoolStudent("Charlie", 103, 88, "12th Grade")

grad_student.display()
undergrad_student.display()
high_school_student.display()
