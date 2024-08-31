# Project: Use Polymorphism in Your Student Classes

class StudentRecord:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def study_method(self):
        print("Study method: General study practices.")

class GraduateStudent(StudentRecord):
    def __init__(self, name, roll_number, marks, thesis_title):
        super().__init__(name, roll_number, marks)
        self.thesis_title = thesis_title

    def study_method(self):
        print(f"Study method: Research and thesis writing. Thesis title: {self.thesis_title}")

class UndergraduateStudent(StudentRecord):
    def __init__(self, name, roll_number, marks, major):
        super().__init__(name, roll_number, marks)
        self.major = major

    def study_method(self):
        print(f"Study method: Focused on coursework and major subjects. Major: {self.major}")

class HighSchoolStudent(StudentRecord):
    def __init__(self, name, roll_number, marks, grade_level):
        super().__init__(name, roll_number, marks)
        self.grade_level = grade_level

    def study_method(self):
        print(f"Study method: High school curriculum focus. Grade Level: {self.grade_level}")
 
students = [
    GraduateStudent("Alice", 101, 90, "AI in Education"),
    UndergraduateStudent("Bob", 102, 85, "Computer Science"),
    HighSchoolStudent("Charlie", 103, 88, "12th Grade")
]

for student in students:
    student.display()
    student.study_method()
    print()  # Blank line for better readability
