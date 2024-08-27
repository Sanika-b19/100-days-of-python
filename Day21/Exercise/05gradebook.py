# Exercise 5: Create a Student Gradebook Class

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, name):
        self.students[name] = {}

    def update_grade(self, name, subject, grade):
        if name in self.students:
            self.students[name][subject] = grade

    def average_grade(self, name):
        grades = self.students.get(name, {}).values()
        return sum(grades) / len(grades) if grades else 0

gradebook = Gradebook()
gradebook.add_student("Alice")
gradebook.update_grade("Alice", "Math", 90)
gradebook.update_grade("Alice", "Science", 85)
print(f"Alice's average grade: {gradebook.average_grade('Alice')}")  # Output: Alice's average grade: 87.5
