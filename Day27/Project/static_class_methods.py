# Project: Implement Static and Class Methods in Your Student Class

class Student:
    student_count = 0  # Class variable to keep track of the number of students

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.student_count += 1  # Increment student count for each new student

    # Instance method to display student details
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    # Class method to create a student from a dictionary
    @classmethod
    def from_dict(cls, student_dict):
        return cls(student_dict['name'], student_dict['age'], student_dict['grade'])

    # Static method to validate a grade
    @staticmethod
    def is_valid_grade(grade):
        return 0 <= grade <= 100

    # Class method to get the total number of students
    @classmethod
    def get_student_count(cls):
        return cls.student_count


student_data = {'name': 'Alice', 'age': 20, 'grade': 85}
student1 = Student.from_dict(student_data)
print(student1.display_info())

print(f"Is 105 a valid grade? {Student.is_valid_grade(105)}")
print(f"Is 90 a valid grade? {Student.is_valid_grade(90)}")

student2 = Student('Bob', 22, 92)
print(student2.display_info())

print(f"Total number of students: {Student.get_student_count()}")
