# Exercise 3: Create Employees Using Class Methods

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_string(cls, employee_str):
        name, age, salary = employee_str.split('-')
        return cls(name, int(age), float(salary))

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

emp_str = "John-30-50000"
employee = Employee.from_string(emp_str)
print(employee.display_info())  # Output: Name: John, Age: 30, Salary: 50000.0
